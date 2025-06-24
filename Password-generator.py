import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pswd1 = []
pswd2 = []
pswd3 = []
# print(pswd1 + pswd2 + pswd3)
for let in range(1, nr_letters+1):
  let = random.randint(0, len(letters))
  letf = letters[let-1]
  # print(letf)
  pswd1.append(letf)

for sym in range(1, nr_symbols+1):
  sym = random.randint(0, len(symbols))
  symf = symbols[sym-1]
  # print(symf)
  pswd2.append(symf)

for num in range(1, nr_numbers+1):
  num = random.randint(0, len(numbers))
  numf = numbers[num-1]
  # print(numf)
  pswd3.append(numf)
  
passwordf = (pswd1 + pswd2 + pswd3)

YourPassword = []
for i in range(1, len(passwordf)+1):
  password = random.randint(0, len(passwordf))
  z = (passwordf[password-1])
  # print(z)
  YourPassword.append(z)

YourPass = ""
for char in YourPassword:
  YourPass += char
  

print(YourPass)