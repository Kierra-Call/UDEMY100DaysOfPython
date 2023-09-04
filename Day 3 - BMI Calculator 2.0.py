# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height * height)

if BMI < 18.5:
    BMIstat = str("you are underweight.")
elif BMI < 25:
    BMIstat = str("you have a normal weight.")
elif BMI < 30:
    BMIstat = str("you are slightly overweight.")
elif BMI < 35:
    BMIstat = str("you are obese.")
else:
    BMIstat = str("Your BMI is 40, you are clinically obese.")
finalBMI = round(BMI)
print(f"Your BMI is {finalBMI}, {BMIstat}")