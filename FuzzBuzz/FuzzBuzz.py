#Write your code below this row 👇

for number in range(0, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("Fuzz Buzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print ("Buzz")
  else:
    print(number)