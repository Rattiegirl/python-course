
class Question:
  def __init__(self, type, text, answer, options = None):
    self.type = type
    self.text = text 
    self.answer = answer
    self.options = options


questions = []
questions.append(Question("open", "What is the capital of Brazil?", "Brasilia"))  
questions.append(Question("open", "How many legs does a chicken have?", "Two"))  
questions.append(Question("single", "What animal can survive being thrown into space?", "Water bear", ["Penguin", "Microbe", "Water bear", "Bear"]))  


def print_question(question):
  print(question.text)

def see_answers():
  for i, question in enumerate(questions):
    print(question.text, question.answer, sep=" ")
  
score = 0

def check_answer(question):
  global score
  answer = input()
  if question.answer == answer:
    score += 1
    print("You are absolutely right!")
  else:
    print("Unfotunately that is not correct.")

print("Hello! I see you came to take a quiz")
def test():
  index = 0
  while (len(questions) > index):
    question = questions[index]
    print_question(question)
    if (question.type == "single"):
      show_options(question.options)
    check_answer(question)
    index += 1
  print("You scored", score, "point(s) out of", len(questions), sep=" ")

def show_options(options):
 for i, option in enumerate(options):
    print(option, " [", i+1, "]", sep="")

while (True):
  print("\n")
  print("Ready to start? Yup! [1] Noo [2]") 
  action = int(input())
  if (action == 1):
    test()
  elif (action == 2):
    print("Ok")
    break
  else:
    print("huh?")