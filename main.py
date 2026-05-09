import random
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from telethon import TelegramClient

# 🔑 ضع بياناتك هنا
BOT_TOKEN = "8775989237:AAHAVAZxvfk8a5V-65ksnjxBSTWize7HkbM"
API_ID = 1234567
API_HASH = "8812f044a8b766c3f492d919976a8f03"
CHANNEL = "https://t.me/l_mahmoud_khaled_oraby_l"  # بدون @

# 📡 تشغيل Telethon
client = TelegramClient("session", API_ID, API_HASH)

# 📸 جلب صورة عشوائية من القناة
async def get_random_image():
    messages = await client.get_messages(CHANNEL, limit=50)
    photos = [m for m in messages if m.photo]

    if not photos:
        return None

    return random.choice(photos)

# 📤 أمر /random
async def random_pic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    img = await get_random_image()

    if img:
        file = await client.download_media(img)
        await update.message.reply_photo(
            photo=file,
            caption="📸 صورة عشوائية من القناة"
        )
    else:
        await update.message.reply_text("لا توجد صور في القناة")

# 🚀 تشغيل البوت
async def main():
    await client.start()

    app = Application.builder().token(8775989237:AAHAVAZxvfk8a5V-65ksnjxBSTWize7HkbM).build()
    app.add_handler(CommandHandler("random", random_pic))

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
