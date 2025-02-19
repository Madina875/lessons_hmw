data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

data_str = str(data)

with open("data.json", "w") as file:
    file.write(data_str)

answer = {'ism': 'Ali', 'yosh': 25, 'kasb': 'dasturchi'}
answer_str = str(answer)

print(answer_str)

# 2-misol
import json

data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)

# 3-misol
import json

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

people_over_20 = [person for person in data["people"] if person["age"] > 20]

print("yigirma yoshdan katta odamlar:")
print(json.dumps(people_over_20, indent=4, ensure_ascii=False))

# 1-misol
import json
from fileinput import close

answer = [4, 5, 4, 2, 5, 7, 2, 8]

answers = list(dict.fromkeys(answer))
print(answers)

# 2-misol
import json

with open("number.txt", "w") as file:
    file.write("5\n10\n3\n7\n2")

with open("number.txt", "r") as file:
    answers = file.read()
print(answers)


def sum_numbers(obj):
    if isinstance(obj, list):
        return sum(sum_numbers(item) for item in obj)


total_sum = sum_numbers(answers)
print(total_sum)


# 3-misol

class BankAccaunt:
    def __init__(self, hisob_raqami: str, egasi: str, balans: float = 0):
        self.hisob_raqami = hisob_raqami
        self.egasi = egasi
        self.balans = balans

    def deposit(self, miqdor):
        return self.balans + miqdor

    def withdraw(self, miqdor):
        if self.balans < 0:
            return self.balans - miqdor
        else:
            print('Insufficient funds')


class SavingAccaunt(BankAccaunt):
    def __init__(self, hisob_raqam, egasi, balans, interest_rate):
        super().__init__(hisob_raqam, egasi, balans)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balans += self.balans * (self.interest_rate / 100)
        return self.balans


class CurrentAccaunt(BankAccaunt):
    def __init__(self, hisob_raqami, egasi, balans, overdraft_limit):
        super().__init__(hisob_raqami, egasi, balans)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, miqdor):
        if miqdor > self.balans + self.overdraft_limit:
            return "Insufficient funds"
        else:
            return self.balans - self.overdraft_limit

