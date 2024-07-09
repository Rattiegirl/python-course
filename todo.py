print("Write stuff you need to achieve here")
cycle_times = 0
tasks = []
while (True):
  print("Would you like to add a task (1), remove a task (2) or recieve a gift (3)?")
  action = int(input())
  if (action == 1):
    while (True):
      print("Say your task, or type 'exit'!")
      stuff = input()
      if (stuff == "exit"):
        break
      cycle_times += 1
      print("Your task of", stuff, "has been added to the list")
      print(str(cycle_times) + ". " + stuff)
      tasks.append(stuff)
  elif (action == 2):
    for i, task in enumerate(tasks):
      print(task)
      
    print("Which one of your tasks have you completed?")
  elif (action == 3):
    print("Here you go!🍬")
  else:
    print("what in the world is that")