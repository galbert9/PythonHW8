# Управление данными
from datetime import date
import IO_System

class DataManager:
    """Класс для работы с базой данных"""

def init_system(self):
    """Метод для старта работы с программой"""
    self.positions = [] # пустой список должностей
    """Добавляем в список людей в формате: зарплата, должность, уровень"""
    self.positions.append(Position(600.0,TypeOfPositions.boss,TypeOfLevels.senior))

    self.persons = [] # пустой список людей
    """Добавляем людей в формате: имя, фамилия, отчество, дата рождения"""
    self.persons.append(Person('Илья','Васильев', 'Андреевич', date(1988,1,15)))
