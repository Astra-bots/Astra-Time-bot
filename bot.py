from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import BOT_TOKEN
from countries import COUNTRIES
from cities import CITIES
from keyboards import country_keyboard, city_keyboard, action_keyboard
from utils import get_time_info

user_country = {}
WELCOME_TEXT = """
🕒 Astra Time

━━━━━━━━━━━━━━

🌍 به Astra Time خوش آمدید.

لطفاً کشور موردنظر خود را انتخاب کنید.

━━━━━━━━━━━━━━

✨ Astra Project
"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        WELCOME_TEXT,
        reply_markup=country_keyboard()
    )
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = update.effective_user.id

    if text == "🌍 انتخاب کشور دیگر":
        user_country.pop(user_id, None)
        await update.message.reply_text(
            "🌍 کشور موردنظر را انتخاب کنید:",
            reply_markup=country_keyboard()
        )
        return

    if text in COUNTRIES:
        user_country[user_id] = text

        await update.message.reply_text(
            f"🏙 شهرهای {text}",
            reply_markup=city_keyboard(text)
        )
        return

    if user_id in user_country:

        country = user_country[user_id]

        for city in CITIES[country]:

            if city["name"] == text:

                info = get_time_info(city["timezone"])

                result = f"""
🕒 Astra Time

🌍 کشور: {country}
🏙 شهر: {city['name']}

🕐 ساعت: {info['time']}

📅 میلادی:
{info['gregorian']}

🇮🇷 شمسی:
{info['shamsi']}

🌙 قمری:
{info['hijri']}
"""

                await update.message.reply_text(
                    result,
                    reply_markup=action_keyboard()
                )
                return

    await update.message.reply_text(
        "❌ لطفاً از دکمه‌های ربات استفاده کنید."
    )
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print("Error:", context.error)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    app.add_error_handler(error_handler)

    print("🕒 Astra Time is Running...")

    app.run_polling()


if __name__ == "__main__":
    main()
