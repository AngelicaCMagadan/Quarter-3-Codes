students = []

for i in range(3):
    print(f"\nStudent {i+1}")
    student = {
        "name": input("Enter name: "),
        "age": int(input("Enter age: ")),
        "subject": input("Enter favorite subject: "),
        "score": int(input("Enter test score: "))
    }
    students.append(student)

print("\nStudent Records:")
for s in students:
    print(f"{s['name']} | Score: {s['score']}")

scores = [s["score"] for s in students]

print("\nClass Summary:")
print("Total:", sum(scores))
print("Average:", round(sum(scores)/len(scores), 2))
print("Highest:", max(scores))
print("Lowest:", min(scores))
