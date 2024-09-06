import logging
import telebot

from django.conf import settings

bot = telebot.TeleBot(
    settings.TOKEN_BOT,
    parse_mode='HTML'
)

telebot.logger.setLevel(settings.LOG_LEVEL)
logger = logging.getLogger(__name__)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

