# ------------------------------------------------------------
# Eli Cohen
# Z:23490083
# Class: Intro To Python
# Professor: Oge Marques
# Assignment: A1
# ------------------------------------------------------------

name = "Eli Cohen"
academic_status = {"Major": "Computer Science", "GPA": 4.7}  # Dict
hobbies = ['Gaming', 'Programming', 'Anime', 'Learning']  # list

preferences = "My hobbies are: \n"  # str
for hobby in hobbies:
    preferences += hobby + "\n"
if academic_status["GPA"] == 4.0:
    rating = "perfect"
elif academic_status["GPA"] >= 3.5:
    rating = "Excellent"
else:
    rating = "Subpar"

print("My name is: ", name, "\n")
print("My Major is:", academic_status['Major'], "and my GPA is:",
      academic_status['GPA'], ", which is considered: ", rating)
print(preferences)
