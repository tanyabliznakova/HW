students_score = {
    'Ivan': 5.00,
    'Alex': 3.50,
    'Maria': 5.50,
    'Georgy': 5.00
}
values = students_score.values()
max_score = max(values)
min_score = min (values)

for k, v in students_score.items():
    if v== min_score:
        print (f'{k} - {v}')

for k, v in students_score.items():
    if v == max_score:
        print (f'{k} - {v}')