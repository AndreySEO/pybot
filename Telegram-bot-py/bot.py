# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.token)
bot.send_message(13256893, "test")

bot = telebot.Telebot(config.token)

upd = bot.get_updates()


last_upd = upd(-1)
massage_from_user = last_upd.massage
print(massage_from_user)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привіт, я Telegram бот")

    if __name__ == "__main__":
        bot.polling()

        @bot.message_handler(commands=["help"])
        def start(message):
            bot.send_message(message.chat.id, "/start - початок використання\n/help - допомога")