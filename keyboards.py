from telegram import ReplyKeyboardMarkup
from countries import COUNTRIES
from cities import CITIES


def country_keyboard():
    keyboard = []

    row = []

    for country in COUNTRIES:
        row.append(country)

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


def city_keyboard(country):
    keyboard = []

    cities = CITIES.get(country, [])

    row = []

    for city in cities:
        row.append(city["name"])

        if len(row) == 2:
            keyboard.append(row)
            row = []

    if row:
        keyboard.append(row)

    keyboard.append(
        ["🌍 انتخاب کشور دیگر"]
    )

    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )


def action_keyboard():
    return ReplyKeyboardMarkup(
        [
            ["🔄 انتخاب شهر دیگر"],
            ["🌍 انتخاب کشور دیگر"]
        ],
        resize_keyboard=True
    )
