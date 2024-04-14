import csv

with open('students.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    scores = {}

    for row in reader:
        full_name = row['FullName']
        score = int(row['Score'])

        if full_name in scores:
            scores[full_name].append(score)
        else:
            scores[full_name] = [score]

average_scores = {}
for student, score_list in scores.items():
    average_scores[student] = sum(score_list) / len(score_list)

print("სტუდენტის ქულა:", scores)
print("საშუალო ქულა:", average_scores)
