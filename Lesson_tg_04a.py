import asyncio
from aiogram import  F
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
import keyboards as kb
from aiogram import Bot, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message




bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
   await callback.answer("Новости подгружаются", show_alert=True)
   await callback.message.answer('Вот свежие новости!')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет', reply_markup=kb.main)

@dp.message(F.text == 'Привет')
async def test(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}')

@dp.message(F.text == 'Пока')
async def test(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}')

@dp.message(Command('links'))
async def links(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.links)


@dp.message(Command('dynamic'))
async def dynamic(message: Message):
   await message.answer(f'Показать больше', reply_markup=kb.callback_keyboard)







async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
