# Ввод-Вывод информации
from DataManager import DataManager
from datetime import datetime
import json


def read_statement(file_name:str):
    with open(file_name,'r', encoding="utf-8") as file:
        result = json.load(file)
    return result