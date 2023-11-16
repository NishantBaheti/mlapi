"""
Config Module
---------------
"""
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath("."), "config", "config.ini"))