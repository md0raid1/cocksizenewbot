import os, hashlib
import random
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


load_dotenv()
token = os.getenv("TOKEN")
bot = Bot(token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
print(token)

emoji1 = '\U0001F923'
emoji2 = '\U0001F602'
emoji3 = '\U0001F609'
emoji4 = '\U0001F60E'
emoji5 = '\U0001F973'
emoji6 = '\U0001F631'
emoji7 = '\U0001F608'


@dp.inline_handler()
async def   inline_handler(query: types.InlineQuery):
    cocksize = random.randint(0, 51)
    text = query.query or 'echo'
    result_id = str = hashlib.md5(text.encode()).hexdigest()
    
    if 1 <= cocksize <= 9:
        articles = [types.InlineQueryResultArticle(
            id = result_id,
            title = 'Share Your Cock Size',
            input_message_content=types.InputTextMessageContent(
                message_text=f'my cock size is <b>{cocksize}cm</b>{emoji1}'
            )
        )]
    elif 10 <= cocksize <= 14:
        articles = [types.InlineQueryResultArticle(
            id = result_id,
            title = 'Share Your Cock Size',
            input_message_content=types.InputTextMessageContent(
                message_text=f'my cock size is <b>{cocksize}cm</b>{emoji2}'
            )
        )]

    elif 15 <= cocksize <= 19:
        articles = [types.InlineQueryResultArticle(
            id = result_id,
            title = 'Share Your Cock Size',
            input_message_content=types.InputTextMessageContent(
                message_text=f'my cock size is <b>{cocksize}cm</b>{emoji3}'
            )
        )]
    elif 20 <= cocksize <= 24:
        articles = [types.InlineQueryResultArticle(
            id = result_id,
            title = 'Share Your Cock Size',
            input_message_content=types.InputTextMessageContent(
                message_text=f'my cock size is <b>{cocksize}cm</b>{emoji4}'
            )
        )]
    elif 25 <= cocksize <= 34:
        articles = [types.InlineQueryResultArticle(
            id = result_id,
            title = 'Share Your Cock Size',
            input_message_content=types.InputTextMessageContent(
                message_text=f'my cock size is <b>{cocksize}cm</b>{emoji5}'
            )
        )]
    elif 35 <= cocksize <= 39:
        articles = [types.InlineQueryResultArticle(
            id = result_id,
            title = 'Share Your Cock Size',
            input_message_content=types.InputTextMessageContent(
                message_text=f'my cock size is <b>{cocksize}cm</b>{emoji6}'
            )
        )]
    elif cocksize >= 40:
        articles = [types.InlineQueryResultArticle(
            id = result_id,
            title = 'Share Your Cock Size',
            input_message_content=types.InputTextMessageContent(
                message_text=f'my cock size is <b>{cocksize}cm</b>{emoji7}'
            )
        )]
    await query.answer(articles, cache_time=60, is_personal=True)


executor.start_polling(dp, skip_updates=True)