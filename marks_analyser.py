import numpy as np
#Generate random marks for 10 students in 5 subjects
array=np.random.randint(1,100,(10,5))
print(array)
#Create a list of student names and Subjects
student=["Sowmya","Ravi","Anjali","Rahul","Priya","Amit","Sneha","Karan","Neha","Vikram"]
subjects=["Maths","Science","English","History","Geography"]
print(np.array(student).shape)
print(np.array(subjects).shape)
#Total of Each student
TOTAL=np.array(array.sum(axis=1))
print(TOTAL)
#average of Each student
AVERAGE=np.array(array.mean(axis=1))
print(AVERAGE)
#TOTAL of Each subject
TOTAL_SUBJECTS=np.array(array.sum(axis=0))
print(TOTAL_SUBJECTS)
#average of Each subject
AVERAGE_SUBJECTS=np.array(array.mean(axis=0))
print(AVERAGE_SUBJECTS)
#Topper and lowest scorer in the list
topper_index = np.argmax(TOTAL)
lowest_index = np.argmin(TOTAL)
print("Topper:", student[topper_index], "with total marks", TOTAL[topper_index])
print("Lowest scorer:", student[lowest_index], "with total marks", TOTAL[lowest_index])
#Grade of students based on average marks
Grade=[]
for avg in AVERAGE:
    if avg>= 90:
        Grade.append("A")
    elif avg>= 75: 
        Grade.append("B")
    elif avg>= 60:
        Grade.append("C")
    elif avg>= 50:
        Grade.append("D")
    else:
        Grade.append("F")   
Grade=np.array(Grade)
print("Grades of students:", Grade) 
#  Subject-wise pass percentage
PASS_MARK = 40
pass_count = (array >= PASS_MARK).sum(axis=0)     # count of students passing, per subject
PASS_PERCENTAGE = (pass_count / array.shape[0]) * 100
print(PASS_PERCENTAGE)                   
#  Rank students by total marks (highest to lowest)
RANK = np.argsort(TOTAL)[::-1]
print(RANK)
# Print ranked list with names
for position, index in enumerate(RANK, start=1):
    print(position, student[index], TOTAL[index])