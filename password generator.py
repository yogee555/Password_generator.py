import string
import random
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
characters = string.ascii_letters + string.digits + string.punctuation
print(characters)
password = " ".join(random.choice(characters)for x in range(random.randint(8,16)))
print(password)