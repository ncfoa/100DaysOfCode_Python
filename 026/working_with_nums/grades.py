
grades = {'Alex': 64, 'Beth': 67, 'Caroline': 98, 'Donald': 44, 'Pita': 19, 'Yolanda': 74}
passing = {k: v for (k, v) in grades.items() if v > 60}
print(passing)
