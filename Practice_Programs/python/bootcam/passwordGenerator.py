import random
import string

password_len = int(input("How many letters you want in your password?"))
password_symbols = int(input("How many symbols you want in your password?"))
password_numbers = int(input("How many numbers you want in your password?"))

password = ""
j_symbol = 0
k_num = 0
for i in range(int(password_len)):
    password += random.choice(string.ascii_letters)
for j in range(int(password_symbols)):
    password += random.choice(string.punctuation)
for k in range(int(password_numbers)):
    password += random.choice(string.digits)


print(f"Your Password is: {password}")
print(f"Your password length is : {len(password)}")


