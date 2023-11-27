#1 Доработиване задачи
# Добавлен возможность запуска из командной строки


import logging
from datetime import datetime
from collections import namedtuple
import argparse

logging.basicConfig(filename='task_5.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='{asctime} {levelname} - {msg}',
                    style='{')
logger = logging.getLogger()

DAYS = {
    'пон': 0, 'вто': 1, 'сре': 2, 'чет': 3, 'пят': 4, 'суб': 5, 'вос': 6,
    0: 'пон', 1: 'вто', 2: 'сре', 3: 'чет', 4: 'пят', 5: 'суб', 6: 'вос',
}
MONTHS = {
    'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4,
    'май': 5, 'мая': 5, 'июн': 6,
    'июл': 7, 'авг': 8, 'сен': 9,
    'окт': 10, 'ноя': 11, 'дек': 12,
    1: 'янв', 2: 'фев', 3: 'мар',
    4: 'апр', 5: 'май', 6: 'июн',
    7: 'июл', 8: 'авг', 9: 'сен',
    10: 'окт', 11: 'ноя', 12: 'дек',
}
Dates = namedtuple('Dates', ['Year', 'Month', 'Day', 'user_text'])


def text_to_date(text):
    try:
        dn, d, m = text.split()
    except ValueError as e:
        logger.exception(e)
    else:
        week_day = DAYS[d[:3]]
        month = MONTHS[m[:3]]
        year = datetime.now().year
        dn = int(dn[:-2])
        counter = 1

        for day in range(1, 32):
            date = datetime(year=year, month=month, day=day)
            if date.weekday() == week_day:
                if counter == dn:
                    date_log = Dates(date.year, date.month, date.day, text)
                    logger.info(f'{date_log = }')
                    return date
                counter += 1
        logger.error(f'Такой даты нет - {text}')

parser = argparse.ArgumentParser()
parser.add_argument('-dn', metavar='dn', default='1-й')
parser.add_argument('-d', metavar='d', default=DAYS[datetime.now().weekday()])
parser.add_argument('-m', metavar='m', default=MONTHS[datetime.now().month])
args = parser.parse_args()
print(args)
print(text_to_date(f'{args.dn} {args.d} {args.m}'))


#2 код, который запускается из командной строки и получает на вход путь до директории на ПК.
#собрано информация о содержимом в виде объектов namedtuple.
#В процессе сбора сохранены данные в текстовый файл с  использованем логирование.

import argparse
import logging
import os
from collections import namedtuple
from pathlib import Path

logging.basicConfig(filename='hw.log',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='{asctime} {levelname} - {msg}',
                    style='{')
logger = logging.getLogger()

PathElements = namedtuple("PathElements", ['name', 'extension', 'directory', 'parent_dir'])

parser = argparse.ArgumentParser()
parser.add_argument('-p', type=str)
args = parser.parse_args()
path = Path(args.p)

path_elements_list = []
file_list = os.listdir(path)
for elem in file_list:
    temp_path = path / elem
    name = temp_path.stem
    suffix = temp_path.suffix or 'directory does not have extension'
    directory = temp_path.is_dir()
    parent_dir = temp_path.parent.stem
    logger.info(f"file/dir name: {name}, suffix: {suffix}, directory: {directory}, parent_dir: {parent_dir}")
    path_elements_list.append(PathElements(name, suffix, directory, parent_dir))

print(*path_elements_list, sep='\n')

# end
