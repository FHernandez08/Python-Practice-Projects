student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(sum(student_scores))
print(max(student_scores))

exam_scores = [8, 65, 89, 86, 55, 91, 64, 89]

current_score = 0
for score in exam_scores:
    if score > current_score:
        current_score = score

print(current_score)