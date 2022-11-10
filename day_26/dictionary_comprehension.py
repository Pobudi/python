'''import random
names = ["Bartek", "Ida", "Klaudia", "Alina", "Adam", "Jolanta", "Łukasz"]

random_grades = {name: random.randint(1, 100) for name in names}
passed_students = {name: grade for (name, grade) in random_grades.items() if grade >= 50}
print(passed_students)'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)
