# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
totalnames = len(names)
randomnumber = random.randint(0, totalnames - 1)
pay = names[randomnumber]
print(f"{pay} is going to buy the meal today!")

#Alternatively, you can use: pay = random.choice(names)