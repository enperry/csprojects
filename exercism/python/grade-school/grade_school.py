class School:
    def __init__(self):
        self.all = []

    def add_student(self, name, grade):
        self.all.append([name, grade])
        self.all = sorted(self.all, key = lambda x: (x[1], x[0]))

    def roster(self):
        students = []
        for student in self.all:
            students.append(student[0])

        return students

    def grade(self, grade_number):
        grades = []
        for student in self.all:
            if student[1] == grade_number:
                grades.append(student[0])
        grades.sort()
        return grades