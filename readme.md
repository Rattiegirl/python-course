7/9/2024 step 2.3
7/23/2024 step 2.4

Getting a random number from 1 to 100

```python
import random
num = random.randint(1, 100)
```
Transform answers to quiz
```bash
python transform.py input/answers-2.json created_quizzes/quiz-5.json Prog_Mog_5
```
Open quiz in terminal
```bash
python quiz.py created_quizzes/quiz-2.json
```
Activates venv
```bash
.\venv\Scripts\activate
```
Start server with hot reload 
```bash
uvicorn main:app --reload
```
 