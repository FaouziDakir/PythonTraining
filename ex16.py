class Grade:
    def __init__(self, grade, students):
        self.grade = grade
        self.students = students

    def toString(self):
        print("Students list of grade " + str(self.grade) + " :")
        for each in sorted(self.students):
            print(each)

    def addStudent(self, student):
        self.students.append(student)


gradeOne = Grade(1, ['Benjamin', 'Zoe', 'Alex'])
gradeTwo = Grade(2, ['Pascal', 'Faouzi', 'Jean'])
gradeThree = Grade(3, ['Thomas', 'Zakaria', 'Georges'])

grades = [gradeOne, gradeTwo, gradeThree]

for grade in grades:
    grade.toString()