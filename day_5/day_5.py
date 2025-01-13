import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_seq = ""
for rand_l in range(0,nr_letters):
    letter_seq += random.choice(letters)

num_seq = ""
for rand_n in range(0,nr_numbers):
    num_seq += random.choice(numbers)

sy_seq = ""
for rand_s in range(0,nr_symbols):
    sy_seq += random.choice(symbols)
"""
final_pass = sy_seq+num_seq+letter_seq
final_list = []

for i in final_pass:
    final_list.append(i)
"""
final_list = list(letter_seq+num_seq+sy_seq)
print(final_list)

random.shuffle(final_list)

rand_fi_pass = "".join(final_list)
print(f"Your final randomized password is{rand_fi_pass}")
print(f"The length of your final password is {len(final_list)}")

#print(f"your password is {sy_seq+num_seq+letter_seq}")

