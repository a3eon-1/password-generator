import string, random
type_of_password = str(input("1. Only Letters\n2. Only Numbers\n3. Letters and Numbers\n4. Letters and Special Characters\n5. Numbers and Special Characters\n6. Letters and Numbers and Special Characters\n7. Custom\n"))
length_of_password = int(input("Enter the length of password: "))

letters = list(string.ascii_letters)
numbers = list(string.digits)
special_characters = list(string.punctuation)
charachters = list(string.ascii_letters + string.digits + string.punctuation)

password = []

if type_of_password == "1":
    for i in range(length_of_password):
        password.append(random.choice(letters))
elif type_of_password == "2":
    for i in range(length_of_password):
        password.append(random.choice(numbers))
elif type_of_password == "3":
    for i in range(length_of_password):
        password.append(random.choice(letters + numbers))
elif type_of_password == "4":
    for i in range(length_of_password):
        password.append(random.choice(letters + special_characters))
elif type_of_password == "5":
    for i in range(length_of_password):
        password.append(random.choice(numbers + special_characters))
elif type_of_password == "6":
    for i in range(length_of_password):
        password.append(random.choice(charachters))
elif type_of_password == "7":
    letter_count = int(input("Enter letter count in password: "))
    number_count = int(input("Enter number count in password: "))
    special_characters_count = int(input("Enter special characters count in password: "))
    total_count = letter_count + number_count + special_characters_count

    for i in range(letter_count):
        password.append(random.choice(letters))
    for i in range(number_count):
        password.append(random.choice(numbers))
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))
    
    

random.shuffle(password)
print("".join(password))