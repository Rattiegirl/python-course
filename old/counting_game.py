import random
num = random.randint(1, 100)
attempts = 0
print("You have to guess the number!")
while True:
  guess = int(input())
  attempts += 1
  if (num == guess):
    print("You won!")
    print("It only took you",attempts,"tries!")
    break
  else:
    if (num < guess):
      print("Try again, it's lower")
    else:
      print("Try again, it's higher")