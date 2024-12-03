
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Разрешаем запросы с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Лучше указать точный адрес фронтенда для безопасности
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Загружаем вопросы из файла
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

quiz_data = load_quiz("../created_quizzes/quiz-4.json")

# Эндпоинт для получения вопросов
@app.get("/quiz")
def get_quiz():
    return quiz_data