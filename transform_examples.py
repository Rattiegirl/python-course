import random

list1 = [3,64,2,1]
random_nums = random.sample(list1, 3) #find random answers
random.shuffle(list1) #shuffle random answers

print(random_nums)
print(list1)

for element in list1:
  if element == 2:
    continue #skip and don't use
  print(element)

list2 = [element for element in list1 if element != 2]
print(list2)

print(random.sample(range(10), 3))

print(random.choice(["open", "single"]))