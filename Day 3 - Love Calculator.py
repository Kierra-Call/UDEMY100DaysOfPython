# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
new_name = name1.lower() + name2.lower()
t = new_name.count("t")
r = new_name.count("r")
u = new_name.count("u")
e = new_name.count("e")
l = new_name.count("l")
o = new_name.count("o")
v = new_name.count("v")
e = new_name.count("e")
truevalue = t+r+u+e
lovevalue = l+o+v+e

strtotal = str(truevalue) + str(lovevalue)
#Alternatively you can do total = int(str(truevalue)+str(lovevalue))
total = int(strtotal)

if total <= 10 or total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

