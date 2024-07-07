from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import asyncio

# Основное меню с дополнительными кнопками
main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет")],
        [KeyboardButton(text="Пока")],

    ],
    resize_keyboard=True
)

# Ссылки на ресурсы
links = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новости", url='https://ria.ru/')],
        [InlineKeyboardButton(text="Музыка", url='https://101.ru/radio/channel/85')],
        [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/?app=desktop&hl=ru&gl=RU')]
    ]
)

# Inline клавиатура с callback данными
callback_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Опция 1", url='https://lenta.ru/rubrics/culture/kino/')],
        [InlineKeyboardButton(text="Опция 2", url='https://lenta.ru/rubrics/culture/series/')]
    ]
)











