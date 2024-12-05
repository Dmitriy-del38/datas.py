grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
#print(grades)
#print(grades)
students={'Jonny','Bilbo','Steve','Khendrik','Aaron'}
print(students)
sorted_students = sorted(students)
#journal={'Aaron':[5,3,3,5,4],'Bilbo':[2,2,2,3],'Jonny':[4,5,5,2],'Khendrik':[4,4,3],'Steve':[5,5,5,4,5]}
#print(journal)
print(sorted_students)
journal = {sorted_students[0]:sum(grades[0])/len(grades[0]),sorted_students[1]:sum(grades[1])/len(grades[1]),sorted_students[2]:sum(grades[2])/len(grades[2]),sorted_students[3]:sum(grades[3])/len(grades[3]),sorted_students[4]:sum(grades[4])/len(grades[4])}
print(journal)