class Student:
    # name = ''
    # rollno = 0

    def __init__(self, n, r):
        self.name = n
        self.rollno = r

    # def getPercentage(self):
    #     return (self.marks * 100) / 50

    # def __str__(self):
    #     return self.name + " got " + str(self.getPercentage()) + f"% in " + self.subject


class Exam(Student):
    def __init__(self, n, r, s, m):
        Student.__init__(self, n, r)
        self.subject = s
        self.marks = m


s1 = Student("ABC", 4, 25)
# s1.name = 'Student1'
# s1.rollno = 20
# s1.marks = 35
# print(s1.getPercentage())
print(s1)

s2 = Student("XYZ", 5, 40, "JAVA")
# print(s2.getPercentage())
print(s2)

# s3 = Student()
# print(s3.getPercentage())
# print(s3)
