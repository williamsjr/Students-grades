print("Type -999 to exit any prompts")
test_scores = {}
student = input("Enter student name: ")
grade_sum = 0
while student != '-999':
    grade = eval(input("Test grade: "))
    test_scores[student] = grade
    grade_sum += grade
    print()

    student = input("Enter student name: ")

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

search = input("Enter student name: ")

while search != '-999':
    if search in test_scores:
        print(search, '\t', test_scores[search])
    else:
        print(search, "Name not found")
    print()
    print()
    search = input("Enter student name: ")


total_scores = list(test_scores.values())
total_score_count = len(total_scores)
class_avg = (grade_sum / total_score_count)
print("Class average: ", class_avg, "%")
    
