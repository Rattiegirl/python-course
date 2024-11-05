import random
from lib.files import load_questions_array

def take_some_indexes(big_element, amount):
  random_nums = random.sample(range(len(big_element)), amount)
  return random_nums

def create_open_question(question, answer):
  return {
    "type": "open", 
    "question": question,
    "answer": answer
  }

def create_single_question(question, answer, random_answers):
  random.shuffle(random_answers + answer)
  return {
    "type": "single", 
    "question": question,
    "answer": answer,
    "options": [random.shuffle(random_answers + answer)]
    #shuffle random answers + actual answer
  }

def find_random_answers(big_element, amount, index_to_skip):
  return []

def create_file(file_name, quiz_name, created_questions, passing_score):
  # with open(output_file, 'w', encoding='utf-8') as f:
  #   json.dump(my_quiz_obj, f, ensure_ascii=False, indent=4)
  return True

def convert_to_test(file_name, quiz_name, passing_score):
  big_element = load_questions_array(file_name)
  indexes = take_some_indexes(big_element, 5)
  for index in indexes:
    type = "open"
    question = create_open_question(big_element[index][0], big_element[index][1])
    print(question)
# take big element of file_name (like loadquiz)
# take 5 random indexes of the big element
#for each index
  #randomly assign "open" or "single" type
  #if open
    #index[0] -> "question", index[1] -> "answer", append (add) to questions
  #if single
    #index[0] -> "question", index[1] -> "answer", take 3 other random index[1] and create shuffled "options" []
    #append to questions
#create new file

# big_element = load_questions_array("answers.json")

# print(take_some_indexes(big_element, 5))

# print(random.choice(["open", "single"]))

convert_to_test("answers.json", "Prog Mog", 4)