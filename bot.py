from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from keyboards.client_keyboard import kbcl
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from bd.bd import botBD

#bot = Bot(token=os.getenv('TOKEN'))
bot = Bot(token="5569216235:AAFQeoXnUjjAcTlwU8AryJkps2TUbXRu5xA")
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)
botBD = botBD()


class FSMzap(StatesGroup):
    os_raxunok = State()
    pib = State()
    address =State()
    pokaznik = State()

@dp.message_handler(commands=['start', 'help'],state= None)
async def send_welcome(message: types.Message):
    await message.reply("Вітаю! Щоб розпочати натисніть кнопку внизу!",reply_markup=kbcl )

@dp.message_handler(commands=['Подати_показник'],state=None)
async def echo(message : types.Message):
    #await message.reply(message.text)
    await FSMzap.os_raxunok.set()
    await message.answer("Напишіть ваш особовий рахунок: ",reply_markup=ReplyKeyboardRemove())

@dp.message_handler(state=FSMzap.os_raxunok)
async def get_os_raxunok(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['os_raxunok'] = message.text
    print(f"Особовий рахунок - {message.text}")
    await FSMzap.next()
    await message.reply("Введіть ПІБ:")

@dp.message_handler(state=FSMzap.pib)
async def get_pib(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pib'] = message.text
    print(f"ПІБ - {message.text}")
    await FSMzap.next()
    await message.reply("Введіть адресу:")

@dp.message_handler(state=FSMzap.address)
async def get_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    print(f"Адреса - {message.text}")
    await FSMzap.next()
    await message.reply("Введіть показник:")

@dp.message_handler(state=FSMzap.pokaznik)
async def get_pokaznik(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pokaznik'] = message.text
    print(f"Показник - {message.text}")
    botBD.rec(data['os_raxunok'],data['pib'],data['address'],data['pokaznik'],date="09.07.2022")
    #print(f"Особовий рахунок -{data['os_raxunok']}\nПІБ - {data['pib']}\nАдрес - {data['address']}\nПоказник - {data['pokaznik']}")
    await message.reply(f"Показник прийнятий в обробку!\nОсобовий рахунок -{data['os_raxunok']}\nПІБ - {data['pib']}\nАдрес - {data['address']}\nПоказник - {data['pokaznik']}",reply_markup=kbcl)
    await state.finish()

@dp.message_handler()
async def echo(message : types.Message):
    #await message.reply(message.text)
    if message.text == "Стат":
        te=botBD.stat()
        print(te)
        await message.reply(te)
    else:
        await message.answer("Не розумію!")
    
print("Bot running!")
executor.start_polling(dp,skip_updates=True)