def load_questions_array(file_name):
  #return big_element
  return []

def take_some_indexes(big_element, amount):
  #take 5 random indexes of the big element
  return [1,2,5,6,3]

def create_open_question(question, answer):
  return {
    "type": "open", 
    "question": question,
    "answer": answer
  }

def create_single_question(question, answer, random_answers):
  return {
    "type": "single", 
    "question": question,
    "answer": answer,
    "options": []
    #shuffle random answers + actual answer
  }

def find_random_answers(big_element, amount, index_to_skip):
  return []

def create_file(file_name, quiz_name, created_questions, passing_score):
  # with open(output_file, 'w', encoding='utf-8') as f:
  #   json.dump(my_quiz_obj, f, ensure_ascii=False, indent=4)
  return True

def convert_to_test(file_name, quiz_name, passing_score):
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

