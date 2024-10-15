def convert_to_test(file_name, quiz_name, passing_score):
# take big element of file_name (like loadquiz)
# take 5 random indexes of the big element
#for each index
  #randomly assign "open" or "single" type
  #if open
    #index[0] -> "question", index[1] -> "answer", append to questions
  #if single
    #index[0] -> "question", index[1] -> "answer", take 3 other random index[1] and create shuffled "oprions" []
    #append to questions
#create new file