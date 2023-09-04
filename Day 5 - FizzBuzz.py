#Write your code below this row 👇

score = 0
for number in range (1, 101,):
  score += 1
  if score % 5 == 0 and score % 3 == 0:
      print("FizzBuzz")
  elif score % 5 == 0:
      print("Buzz")
  elif score % 3 == 0:
      print("Fizz")
  else:
      print(score)

