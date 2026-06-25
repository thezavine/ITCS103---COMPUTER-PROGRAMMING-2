#---------------------------- HANDS ON NUMBER 1 ----------------------------------------------
#Use of lists, functions, loops, and conditional statements.
print("----------------------------------------------------------")
print("Konnichiwa, Welcome to my first hands on for 2nd Semester.") #intro
print("--------------------- Enjoy!!! ---------------------------")

#Ask the user to enter a word
word = input("\nEnter any word: ")
#Then, identify how long the word is
word_length = len(word)

#Ask the user to provide numbers corresponding to each character of the word and record them in a list.
numbers = []
add = 0
for i in range(1, word_length + 1):
    num_input = int(input(f"Enter number {i}: "))
    numbers.append(num_input)
    add += num_input

ave = add / word_length
print(numbers)  # it shows here the full list of numbers entered
print(f"The length of the word is {word_length}")
print(f"The average of the numbers is {ave}")

if word_length < ave:
    print(f"The length of the word '{word}' is less than the average of the numbers.")
elif word_length > ave:
    print(f"The length of the word '{word}' is greater than the average of the numbers.")
else:
    print(f"The length of the word '{word}' is equal to the average of the numbers.")

#---------------------------------------- E N D -----------------------------------------------
