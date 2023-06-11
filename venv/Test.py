import telebot
from telebot import types
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

bot = telebot.TeleBot('5838447318:AAGlaNIsRiM2jHWU8XDNjepn45ZY-3mqQso')

@bot.message_handler(content_types=["text"])
def save_log_msg(message):
    bot.send_message(message.chat.id, "Input login: ")
    log_msg = message.text
    print(log_msg)

@bot.message_handler(content_types=["text"])
def save_pas_msg(message):
    log_msg = bot.send_message(message.chat.id, "Input password: ")
    print(log_msg.text)

bot.infinity_polling()
