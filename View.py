from aiogram import types
from bot import bot

async def start_game(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}\n\
       Правила: На столе лежит 117 конфет. Играют два игрока делая ход друг после друга.\
       Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
       Все конфеты оппонента достаются сделавшему последний ход.')
async def help(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}\n\
       Правила: На столе лежит 117 конфет. Играют два игрока делая ход друг после друга.\
       Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\
       Все конфеты оппонента достаются сделавшему последний ход.\n\n\
        /start - Начать игру\n \
        /help - Помощь по коммандам и правила игры')


async def table_info(message: types.Message, name: str, count: int, total_count: int, name2: str):
    await bot.send_message(message.from_user.id, f'{name} взял {count} конфет\nИ на столе осталось {total_count} конфет\nХод {name2}\n\n Чтобы начать сначала введите /start')


async def wrong_take(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вы взяли конфет больше чем нужно (или меньше)! Попробуйте еще раз')


async def player_take(message: types.Message):
    await bot.send_message(message.from_user.id,'Возьмите конфеты, но не больше 28: ')


async def win(message: types.Message, name:str, count:int, total_count):
    await bot.send_message(message.from_user.id, f'{name} взял {count} конфет\nИ на столе осталось {total_count} конфет\n{name} выиграл! \n\n Чтобы начать игру заново введите /start')