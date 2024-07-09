print("Time to do some math")
print("First enter two numbers and then the sign you want to merge them with")
current_number = float(input())
while (True):
  sign = input()
  if (sign == "="):
    print(current_number)
    break
  value2 = float(input())
  if (sign == "+"):
    current_number += value2 
  elif (sign == "-"):
    current_number -= value2
  elif (sign == "x") or (sign == "*"):
    current_number *= value2
  elif (sign == "/"):
    current_number /= value2
  else:
    print("Not in my powers to answer")
    break
  print(current_number)
