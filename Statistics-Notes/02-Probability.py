# --- Permutation ---- 

import math 
# We need to create a password which length is 5 character and has letter and number between 0 and 9 
# You can't use typed letter or number again.
letter = 29 
number = 10
total = letter + number
numerator = math.factorial(total)
passwordLength = 5
denominator = math.factorial(total - passwordLength)
fraction = numerator / denominator
print("Permutation (without repated): ", fraction)

# If you can use the typed number again  P = n^r
fraction = total**passwordLength
print("Permutation repeated: ",fraction)

#--------------------------------------------------------

# ----- Combination ------ 

# Question:  Picking a team of 3 people from a group of 10.

people = 10 
pick = 3
numerator = math.factorial(people)
denominator = math.factorial(people-pick) * math.factorial(pick)

print("\nCombination: ",numerator/denominator)

#--------------------------------------------------------
