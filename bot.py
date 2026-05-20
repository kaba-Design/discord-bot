import os
import re
import logging
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
BANNED_FILE = "banned_words.txt"

if TOKEN is None:
    raise RuntimeError("DISCORD_TOKEN is not set in .env")

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_MESSAGE = (
    "ようこそ。ここは何も説明しなくていい場所です\n"
    "ご参加ありがとうございます！"
)


def load_banned_words(filename):
    if not os.path.exists(filename):
        log.warning("%s が見つかりません。デフォルトNGワードを使用します。", filename)
        return [
            "ばか",
            "くそ",
            "死ね",
            "ぶす",
            "しね",
            "アホ",
            "うざい",
            "キモい",
            "殺す",
            "氏ね",
        ]

    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.strip().startswith("#")]
        if not lines:
            log.warning("%s にNGワードが書かれていません。デフォルトNGワードを使用します。", filename)
            return [
                "ばか",
                "くそ",
                "死ね",
                "ぶす",
                "しね",
                "アホ",
                "うざい",
                "キモい",
                "殺す",
                "氏ね",
            ]
        return lines


BANNED_WORDS = load_banned_words(BANNED_FILE)
BANNED_PATTERN = re.compile(
    "|".join(re.escape(word) for word in BANNED_WORDS),
    re.IGNORECASE,
)


@bot.event
async def on_ready():
    log.info("Logged in as %s (%s)", bot.user, bot.user.id)
    log.info("Bot is ready.")


@bot.event
async def on_member_join(member: discord.Member):
    try:
        await member.send(WELCOME_MESSAGE)
        log.info("Sent welcome DM to %s", member)
    except Exception as e:
        log.warning("Failed to send DM to %s: %s", member, e)


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.guild is None:
        return

    if BANNED_PATTERN.search(message.content):
        try:
            await message.delete()
            log.info("Deleted NG message from %s: %s", message.author, message.content)
            warning = f"{message.author.mention} さん、その言葉はここでは使えません。"
            await message.channel.send(warning, delete_after=8)
        except Exception as e:
            log.warning("Failed to delete message: %s", e)
        return

    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run(TOKEN)
