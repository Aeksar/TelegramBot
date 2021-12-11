#Ботяра
import pyowm
import telebot

bot = telebot.TeleBot("1931456593:AAGyS3zc7hMggUBoXwk2LAJyHY5mZtNcvRM")
owm = pyowm.OWM('fe8c4010528c038db1f1b697a2ee4b75')
mgr = owm.weather_manager()

print('robit')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Здарова")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	t = w.temperature('celsius')['temp']

	bot.send_message(message.chat.id, message.text)

	tp = ('Температура: ' + str(t))
	bot.send_message(message.chat.id, tp)

bot.infinity_polling()
