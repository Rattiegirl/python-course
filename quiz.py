
class Question:
  def __init__(self, type, text, answer, options = None):
    self.type = type
    self.text = text 
    self.answer = answer
    self.options = options

test1 = []
# questions = []
test1.append(Question("open", "What is the capital of Brazil?", "Brasilia"))  
test1.append(Question("open", "How many legs does a chicken have?", "Two"))  
test1.append(Question("single", "What animal can survive being thrown into space?", "Water bear", ["Penguin", "Microbe", "Water bear", "Bear"]))  

test2 = []
test2.append(Question("open", "What bug can walk on water?", "Water strider"))  
test2.append(Question("single", "Which food is not a vegetable?", "Pomegranate", ["Asparagus", "Broccoli", "Pomegranate", "Bell peppers"]))  

tests = []
tests.append(test1)
tests.append(test2)

current_test = test1

def print_question(question):
  print(question.text)

def see_answers():
  for i, question in enumerate(test1):
    print(question.text, question.answer, sep=" ")

score = 0

def correct_text():
   global score
   score += 1
   print("You are absolutely right!")

def incorrect_text():
   print("Unfotunately that is not correct.")
  

def check_answer(question):
  global score
  answer = input()

  if question.type == "open":
    if question.answer == answer:
      correct_text()
    else:
      incorrect_text()
  elif question.type == "single":
    if question.options[int(answer) - 1] == question.answer:
      correct_text()
    else:
      incorrect_text()


print("Hello! I see you came to take a quiz")
def test():
  index = 0
  while (len(current_test) > index):
    question = current_test[index]
    print_question(question)
    if (question.type == "single"):
      show_options(question.options)
    check_answer(question)
    index += 1
  print("You scored", score, "point(s) out of", len(current_test), sep=" ")
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
      current_test = tests[index]
      test()
      index += 1
    print("Very good job! Unfortunately we don't have anymore for you yet, so goodbye")
    break
  elif (action == 2):
    print("Ok")
    break
  else:
    print("huh?")