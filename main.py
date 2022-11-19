import telegram
from telegram.ext import *
from telegram import Poll
from io import BytesIO
import cv2
import numpy as np
#import tensorflow as tf
import time

TOKEN = ""

def start (update, context):
    update.message.reply_text("\U0001F44B Привет! Добро пожаловать в ММОРПГ выставки Музея Транспорта Москвы \U0001F687. Окунитесь в приключения, попутно исследуя экспонаты нашей выставки. Соревнуйтесь с друзьями и другими людьми, чтобы подняться на первые строчки рейтинга и получить крутые призы \U0001F381")
    update.message.reply_text("Используйте команду /create, чтобы создать персонажа, либо продолжите свой путь с уже существующим аватаром \U0001F916")
    update.message.reply_text("Пригласите друга с помощью кода своего персонажа и получите бонус +50 очков славы к своему рейтингу.")

def help(update, context):
    update.message.reply_text("""

\U0001F9BE /start - Начать игру 

\U0001F4DC /help - Полный список команд 

\U0001F635 /restart - Перезапустить бота 

\U0001F916 /create - Создать персонажа 

\U0001F9D1 /tutorial - Запускает туториал 

\U0001F48E /quests - Показывает список доступных квестов 

\U0001F608 /duel - Начать дуэль с другим игроком 

\U0001F4CA /stats - Статистика персонажа 

\U0001F396 /allstats - Общая статистика по выставке 
    """)


def handle_photo(update, context):
    update.message.reply_text("Обрабатываем фотографию...")
    time.sleep(5)
    update.message.reply_text("Поздравляем! Вы прошли туториал, теперь вы побороться за первое место в турнирной таблице и получит уникальные призы!")
    update.message.reply_text("""Теперь вам доступен список квестов, используйте команду /quests, чтобы прокачать своего персонажа. 
Начать дуэль можно через команду /duel. 
Посмотреть свою статистику можно через команду /stats и общую статистику через /allstats.""")

def prize(update, context):
    update.message.reply_text("Поздр-авто-вляем! Вы победили, назовите на кассе промокод: 'TEAM21WIN', чтобы получить подарок!")

def create(update, context):
        update.message.reply_text("\U0001F476 Ваш персонаж официально создан. Ваш номер 116, используйте этот номер для взаимодействия с другими игроками \U0001F46F")
        update.message.reply_text("Используйте команду /tutorial, чтобы пройти обучение и начать соревноваться \U0001F5E1")

def tutorial(update, context):
    update.message.reply_text("Пришли фотографию инсталляции 'Машина времени'. Убедись, что объект хорошо виден на фото.")

def quests(update, context):
    update.message.reply_text("""
\U0001F4F7 Пришлите фотографию инсталляции 'Машина Времени', убедитесь, что на фотографии экспонат видно ясно и четко. (+10 Сила)

\U0001F4DD Пройдите до конца квиз по выставке на скорость (сложность: Высокая) (+30 Удача). Введите команду /quiz, чтобы начать.

\U0001F9E9 Решите загадку (сложность: Средняя) (+15 Ловкость)
    
    
\U0001F52E Задания, квизы и загадки периодически обновляются.""")

def stats(update, context):
    update.message.reply_text(""" \U0001F4CA Статистика персонажа \U0001F4CA
    
\U0001F9BE Сила: 50

\U0001F977 Ловкость: 30

\U0001F340 Удача: 35

\U0001FAC5 Слава: 15""")


def allstats(update, context):
    update.message.reply_text(""" \U0001F451 Общая статистика \U0001F451 
    
\U0001F947 Иван Иванов (114): 900

\U0001F948 Екатерина Антонова (098): 867

\U0001F949 Виктория Лазарева (007): 854

\U0001F525 Исламова Диана (006): 801

\U0001F31F Вилльямс Коммандор (089): 780""")

def duel(update, context):
    update.message.reply_text("Ищем случайного противника.")
    update.message.reply_text(fight())
    send_document(update, context)

def fight():
    answer = "Борьба игрока 116 и игрока 007"
    return answer

def send_document(update, context):
    chat_id = update.message.chat_id
    document = open('frogs-fighting.gif', 'rb')
    context.bot.send_document(chat_id, document)
    time.sleep(3)
    update.message.reply_text("Противник нанес вам урон, но благодаря вашей удаче вы быстро восстановились.")
    time.sleep(3)
    update.message.reply_text("Вы ударили противника и нанесли критический урон!")
    time.sleep(3)
    update.message.reply_text("Противник упал без сознания.")
    update.message.reply_text("Вы победили! +10 очков славы.")

def get_chat_id(update, context):
  chat_id = -1

  if update.message is not None:
    chat_id = update.message.chat.id
  elif update.callback_query is not None:
    chat_id = update.callback_query.message.chat.id
  elif update.poll is not None:
    chat_id = context.bot_data[update.poll.id]

  return chat_id

def quiz(update, context):
    c_id = get_chat_id(update, context)
    q = 'Кто являются авторами инсталляции "Машина Времени"?'
    answers = ['Илья Шагалов и Сергей Неботов', 'Илья Муромец и Алеша Поповович', 'Данила Козловский и Сергей Безруков']
    message = context.bot.send_poll(chat_id=c_id, question=q, options=answers, type=Poll.QUIZ, correct_option_id=0, open_period=5)

def poll_handler(update, context):
  question = update.poll.question
  correct_answer = update.poll.correct_option_id
  option_1_text = update.poll.options[0].text
  option_1_vote = update.poll.options[0].voter_count

def get_answer(update):
  answers = update.poll.options

  ret = ""

  for answer in answers:
    if answer.voter_count == 1:
      ret = answer.text
      break
  return ret


def is_answer_correct(update):
    answers = update.poll.options

    ret = False
    counter = 0
    for answer in answers:
        if answer.voter_count == 1 and \
                update.poll.correct_option_id == counter:
            ret = True

            break

        counter = counter + 1
    return ret

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(CommandHandler("restart", start))
dp.add_handler(CommandHandler("create", create))
dp.add_handler(CommandHandler("tutorial", tutorial))
dp.add_handler(CommandHandler("quests", quests))
dp.add_handler(CommandHandler("stats", stats))
dp.add_handler(CommandHandler("allstats", allstats))
dp.add_handler(CommandHandler("duel", duel))
dp.add_handler(CommandHandler("quiz", quiz))
dp.add_handler(PollHandler(poll_handler, pass_chat_data=True, pass_user_data=True))
dp.add_handler(MessageHandler(Filters.photo, handle_photo))

updater.start_polling()
updater.idle()