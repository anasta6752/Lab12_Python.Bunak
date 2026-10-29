
import random
import string


def generate_number():
    digits = "".join(random.choices(string.digits, k=4))
    letters = "".join(random.choices(string.ascii_uppercase, k=3))
    return digits + " " + letters


N = int(input("Введіть кількість автомобільних номерів: "))

for i in range(N):
    print(generate_number())
