"""
module contains config
"""
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class Config:
    """
    Сonfig class
    """
    DB_CONNECTION = os.getenv('DATABASE_URL', 'sqlite:///main.db')
    SECRET_KEY = os.getenv('SECRET_KEY').encode()

