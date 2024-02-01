from pathlib import Path
from colorama import Fore
import sys

# Открывает и читает содержимое файла.
def open_read_file(path):

    """
    Параметры:
    - path: Путь к файлу

    Возвращает:
    - Строка содержимого файла, если файл найден и может быть прочитан
    - Пустая строка, если файл не найден или произошла ошибка чтения
    """

    file_content = ''  # Инициализация переменной для содержимого файла

    try:
        with open(path, "r") as file:  # Открытие файла на чтение
            file_content = file.read()  # Чтение содержимого файла
    except FileNotFoundError:  # Обработка исключения "Файл не найден"
        print("File not found!")
    except IOError:  # Обработка исключения "Ошибка ввода-вывода"
        print("Error read or write to the file")
    except Exception as e:  # Обработка других исключений
        print("Error:", e)
    finally:
        return file_content  # Возвращение содержимого файла или пустой строки в случае ошибки

# Задание - 1
# Pозробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників
def total_salary(path):

    """
    Параметры:
    - path: Путь к файлу.

    Возвращает:
    - Строка содержимого файла, если файл найден и прочитан.
    - Пустая строка, если файл не найден или произошла ошибка чтения.
    """

    # Чтение содержимого файла
    text_str = open_read_file(path)
    
    # Проверка на пустой файл или ошибку чтения
    if text_str == '':
        return {'Error': 'Function "open_read_file" or file is empty'}
    
    # Инициализация переменных для общей суммы и среднего значения
    total = 0
    average = 0
    
    # Создание словаря для хранения имен и зарплат
    text_dict = {}
    
    # Разделение текста на строки и парсинг имен и зарплат
    text_split_list = text_str.split('\n')
    for line in text_split_list:
        name, salary = line.split(',')
        text_dict[name.strip()] = int(salary.strip())
    
    # Вычисление общей суммы и средней зарплаты
    total = sum(text_dict.values())
    average = total / len(text_dict)
    
    return {'total': total, 'average': average}

# Тест к заданию - 1
# print(total_salary('task_1_2_3\workers.txt'))

# Задание - 2
# Pозробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

def get_cats_info(path):

    """
    Параметры:
    - path: Путь к файлу

    Возвращает:
    - Список словарей с информацией о каждом коте в файле.
      Каждый словарь содержит ключи 'id', 'name', 'age'.
    - Если произошла ошибка при чтении файла или файл пустой,
      возвращается список с одним словарем, содержащим информацию об ошибке
    """

    # Чтение содержимого файла
    text_str = open_read_file(path)
    
    # Проверка на пустой файл или ошибку чтения
    if not text_str:
        return [{'Error': 'Function "open_read_file" or file is empty'}]
    
    # Создание списка для хранения информации о котах
    cat_info_list = []
    
    # Разделение текста на строки
    text_split_list = text_str.split('\n')

    # Парсим информацию о котах
    for line in text_split_list:
        cat_id, name, age = line.split(',')
        cat_info_list.append({'id': cat_id, 'name': name, 'age': int(age)})
    
    return cat_info_list

# Тест к заданию - 2
# for cat in get_cats_info('task_1_2_3\cats.txt'):
#     print(cat)

# Task 3
# Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, 
# виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.

def color_print(text, level=0):

    """
    Параметры:
    - text: Текст для вывода
    - level: Уровень вложенности. Используется для определения отступа и цвета

    Возвращает:
    Ничего
    """

    colors = [Fore.YELLOW, Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    color = colors[level if level < len(colors) else 6]  # Выбор цвета в зависимости от уровня
    ident = '     ' * level  # Определение отступа в зависимости от уровня
    print(f'{color}{ident}|---{text}{Fore.RESET}')  # Вывод текста с цветом

def read_folder(folder  = 'task_1_2_3', level = 0):

    """
    Параметры:
    - folder: Путь к папке
    - level: Уровень вложенности текущей папки

    Возвращает:
    Ничего
    """

    path = Path(folder)  # Преобразует путь к объекту Path
    
    if path.exists():  # Проверяет существование пути
        print(path.name) if level == 0 else None  # Выводит имя папки, если это корневая папка
        if path.is_dir():  # Проверяет, является ли объект папкой
            items = path.iterdir()  # Получает список элементов в папке
            for item in items:
                color_print(item.name, level)  # Выводит имя элемента с учетом уровня вложенности
                if item.is_dir():
                    level += 1  # Увеличивает уровень вложенности для следующей итерации
                    read_folder(item, level)  # Рекурсивно вызывает функцию для каждой подпапки
                    level -= 1  # Возвращается на один уровень вложенности для корректного вывода
        else:
            print(f'{path} is a file', level)  # Выводит информацию о файле
    else:
        print(f'{path.absolute()} is not exist')  # Выводит сообщение об ошибке, если путь не существует

# Тест к заданию - 3
# read_folder(r'D:\basic\python-course-go-it')
# read_folder()