
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from lib.files import load_quiz, save_results

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

quiz_data = load_quiz("../created_quizzes/quiz-2.json")

# Эндпоинт для получения вопросов
@app.get("/quiz/{quiz_id}")
def get_quiz(quiz_id:str):
    quiz_data = load_quiz("../created_quizzes/quiz-%s.json" %(quiz_id))
    return quiz_data


@app.post("/submit/{quiz_id}")
async def recieve_submission(quiz_id: str, user_answers: dict):
    quiz_data = load_quiz("../created_quizzes/quiz-%s.json" %(quiz_id))
    questions = quiz_data["questions"]
    score = 0
    for i, question in enumerate(questions):
        k = str(i)
        if user_answers.get(k) == question["answer"]: 
            score += 1 
    # await save_results(quiz_data["name"], score)
    # print (user_answers)
    return {
        "score": score,
        "passed": quiz_data["passing_score"] <= score
    }