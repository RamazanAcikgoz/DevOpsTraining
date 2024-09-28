student_score = [150, 142, 195, 120, 171, 184, 149, 24, 59, 68, 89, 86]
sum_ = 0
total_sum = sum(student_score)
for point in student_score:
    sum_ += point

print(sum_)
# Easy way :
print(total_sum)

# Highest score:
highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score

print(highest_score)