import json
import sys

def load_quiz(filename):
    """Загружает вопросы из файла JSON."""
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
    
test1 = load_quiz(sys.argv[1])
tests = []
tests.append(test1)

# def print_question(question):
#   print(question["question"])

# def see_answers():
#   for i, question in enumerate(test1):
#     print(question["question"], question["answer"], sep=" ")

def correct_text():
   print("You are absolutely right!")

def incorrect_text():
   print("Unfotunately that is not correct.")
  
def process_question(question):
  if (question["type"] == "single"):
    print(question["question"])
    show_options(question["options"])
    answer = input()

    return question["options"][int(answer) - 1] == question["answer"]

  elif (question["type"] == "open"):
    print(question["question"])
    answer = input()

    return question["answer"] == answer

  else:
    print("unknown type,", question["type"])
    return False

# def check_answer(question):
#   answer = input()

#   if question["type"] == "open":
#     if question["answer"] == answer:
#       correct_text()
#       return True
#     else:
#       incorrect_text()
#       return False
#   elif question["type"] == "single":
#     if question["options"][int(answer) - 1] == question["answer"]:
#       correct_text()
#       return True
#     else:
#       incorrect_text()
#       return False



print("Hello! I see you came to take a quiz")
def test(current_test):
  print("You are doing the", current_test["name"], "!")
  index = 0
  score = 0
  questions = current_test["questions"]
  while (len(questions) > index):
    question = questions[index]
    if process_question(question):
      correct_text()
      score += 1
    else:
      incorrect_text()
    # print_question(question)
    # if (question["type"] == "single"):
    #   show_options(question["options"])
    # if check_answer(question):
    #   score += 1
    index += 1
  print("You scored", score, "point(s) out of", len(questions), sep=" ")
  if (score >= current_test["passing_score"]):
    print("You passed the test!")
  else:
    print("You failed the test!")
  score = 0

def show_options(options):
 for i, option in enumerate(options):
    print(option, " [", i+1, "]", sep="")

while (True):
  print("\n")
  print("Ready to start? Yup! [1] Noo [2]") 
  action = int(input())
  if (action == 1):
    index = 0 
    while (len(tests) > index):
      test(tests[index])
      index += 1
    print("Very good job! Unfortunately we don't have anymore for you yet, so goodbye")
    break
  elif (action == 2):
    print("Ok")
    break
  else:
    print("huh?")