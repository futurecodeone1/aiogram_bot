import logging  # библиотека для логирования (отображение статусной информации)
from aiogram import Bot, Dispatcher, types, executor

TOKEN = '6266124846:AAHaJIiqr7WbwL2KR2ufzSNMHEkuGymfgNA'

logging.basicConfig(level=logging.INFO)  # отображение в консоль любых действий в боте

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)


if __name__ == '__main__':
	executor.start_polling(dp)
