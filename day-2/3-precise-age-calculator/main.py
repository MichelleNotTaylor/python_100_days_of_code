# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days_in_a_year = 365
weeks_in_a_year = 52
months_in_a_year = 12
max_years = 90

years_left = max_years - int(age)
days = days_in_a_year * years_left
weeks = weeks_in_a_year * years_left
months = months_in_a_year * years_left

print(f"You have {days} days, {weeks} weeks, and {months} months.")








