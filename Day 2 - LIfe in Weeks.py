# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

ageint = int(age)
days_old = ageint * 365
days_left = 32850 - days_old
weeks_old = ageint * 52
weeks_left = 4680 - weeks_old
months_old = ageint * 12
months_left = 1080 - months_old

#print(int(days_left))
#print(int(weeks_left))
#print(int(months_left))

print(f"You have {days_left} days,  {weeks_left} weeks, {months_left} and months left.")