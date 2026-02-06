#Task 12
import re
txt = input('Введите строку ')
print(re.sub(r"\s+", " ", txt))