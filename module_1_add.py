grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
names=list(students)
names.sort()
print(names)
aver_grade=list(sum(x)/len(x) for x in grades)
Named_aver_grade=dict(zip(names,aver_grade))
print(Named_aver_grade)

