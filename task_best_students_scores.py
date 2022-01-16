students_score = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Maria': 5.50,
    'Georgy': 5.00
}

best_students_score = {}

best_students_score = dict((k, v) for k, v in students_score.items() if v >= 4.00)
for k,v in best_students_score.items():
    print(f'{k} - {v}')

########################################################################################

students_score = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Maria': 5.50,
    'Georgy': 5.00
}

best_students_score = {}

for k,v in students_score.items():
    if v>4.00:
        best_students_score[k]=v

for k, v in best_students_score.items():
    print (f'{k} - {v}')








