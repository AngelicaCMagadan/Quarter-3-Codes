scores = [
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
]

print("Student Scores Summary:\n")

student_num = 1

for row in scores:
    print(f"Student {student_num} scores:", row)
    
    total = sum(row)
    average = total / len(row)
    
    print("Total:", total)
    print("Average:", round(average, 2))
    print()
    
    student_num += 1

# Find highest score in entire dataset
max_score = max(max(row) for row in scores)

print("Highest score in the dataset:", max_score)
