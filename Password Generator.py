import random
import array

Maximum_Length= 12


Digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Symbols = ['@', '#', '$', '%', ':', '?','*']

Combined_List = Digits + Uppercase + Lowercase + Symbols

digit = random.choice(Digits)
upper = random.choice(Uppercase)
lower = random.choice(Lowercase)
symbol = random.choice(Symbols)

passw = digit + upper + lower + symbol

for x in range(Maximum_Length - 4):
	passw += random.choice(Combined_List)
	temp_pass_list = array.array('u', passw)
	random.shuffle(temp_pass_list)

password = ""
for x in temp_pass_list:
		password = password + x
		
print(password)
