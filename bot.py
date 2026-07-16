from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

TOKEN = "توکن_ربات_خودت_اینجا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "به ربات Crypto Hunter خوش اومدی.\n\n"
        "دستورهای موجود:\n"
        "/btc - قیمت بیت‌کوین\n"
        "/eth - قیمت اتریوم"
    )

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    data = requests.get(url).json()
    price = data["bitcoin"]["usd"]
    await update.message.reply_text(f"💰 قیمت بیت‌کوین: {price}$")

async def eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    data = requests.get(url).json()
    price = data["ethereum"]["usd"]
    await update.message.reply_text(f"💎 قیمت اتریوم: {price}$")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("btc", btc))
app.add_handler(CommandHandler("eth", eth))

print("Bot Started...")
app.run_polling()
