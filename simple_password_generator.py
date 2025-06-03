import random
import string
print("welcome to password generator!!")
#ask user how many characters of each type do they want
n_letters=int(input("Enter how many letters do you want:"))
n_numbers=int(input("Enter how many numbers do you want:"))
n_symbols=int(input("Enter how many symbols do you want:"))
#defining character set
letters=string.ascii_letters
numbers = string.digits
symbols = string.punctuation
# Create empty lists to store characters
password_letters = []
password_symbols = []
password_numbers = []

# Fill each list using a for loop
for i in range(n_letters):
    password_letters.append(random.choice(letters))

for i in range(n_symbols):
    password_symbols.append(random.choice(symbols))

for i in range(n_numbers):
    password_numbers.append(random.choice(numbers))
#Combine all parts into one list
password_list = password_letters + password_symbols + password_numbers
# Shuffle the list to make the password random
random.shuffle(password_list)
# Join into a string
password = ''.join(password_list)
print("Your generated password is:", password)
# Ask user if they want to generate again
generate_again = input("Do you want to generate another password? (yes/no): ").lower()
if generate_again == "yes":
    print("Please run the program again.")
else:
    print("Thank you for using the Password Generator!")