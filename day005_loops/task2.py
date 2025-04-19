student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0
for score in student_scores:
    sum += score
print(sum)

max_score = max(student_scores)
print(max_score)

max_number = student_scores[0]
for score in student_scores:
    if score > max_number:
        max_number = score
print(max_number)
