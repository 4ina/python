'''
pip install pyTelegramBotAPI
'''

import telebot
import config
import requests

params = {
    'key': config.API_TOKEN,
    'lang': 'en-ru',
    'text': '',
}

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Welcome, this is dictionary type some english word...')

@bot.message_handler(content_types=['text'])
def lalala(message):
	params['text'] = message.text
	response = requests.get('https://dictionary.yandex.net/api/v1/dicservice.json/lookup', params=params,)
	json_response = response.json()
	if json_response['def']:
		translate = json_response['def'][0]['tr'][0]['text']
		bot.send_message(message.chat.id, translate)
	else:
		bot.send_message(message.chat.id, 'Sorry, I can`t help to you.')
	

#RUN
bot.polling(none_stop=True)