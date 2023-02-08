import os
import dotenv

dotenv.load_dotenv('.env')

openai_api_key = os.environ['openai_api_key']
telebot_TeleBot_api_key = os.environ['telebot_TeleBot_api_key']