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
    
def load_quiz(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            questions = json.load(f)
        return questions
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {filename}.")
        return []
    
def load_results():
    try:
        with open("results.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Файл results.txt не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле results.txt.")
        return []
    
async def save_results(quiz_name, score):
  print(quiz_name, score)
  with open("results.txt", 'a', encoding='utf-8') as f:
    f.write(f"{quiz_name}: {score}\n")

