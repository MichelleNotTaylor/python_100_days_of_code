# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height**2)
return_message = ""
if bmi < 18.5:
  return_message = "underweight"
elif bmi < 25:
  return_message = "normal weight"
elif bmi < 30:
  return_message = "slightly overweight"
elif bmi < 35:
  return_message = "obese"
else:
  return_message = "clinically obese"

print(f"Your BMI is {bmi}, you are {return_message}.")



