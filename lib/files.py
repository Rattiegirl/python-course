import json

def load_questions_array(filename):
    """Загружает вопросы из файла JSON."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            big_element = json.load(f)
        return big_element
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {filename}.")
        return []
    

