# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_score = 0
love_score = 0

for letter in (name1.casefold()+name2.casefold()):
  if letter in ["t", "r", "u", "e"]:
    true_score += 1
  if letter in ["l", "o", "v", "e"]:
    love_score += 1

final_score = (str(true_score)+str(love_score))

if int(final_score) < 10 or int(final_score) > 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif int(final_score) >= 40 and int(final_score) <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")

