import random
import string



def generate_password(length=8):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("suggested password: /n")


for i in range(4):
    print(f"{i+1}. {generate_password()}")
