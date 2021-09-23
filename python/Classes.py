class Student:
    name = ""
    rollno = 0
    # subject = "Python"
    marks = 0

    def __init__(self, n, r, m, s="Python"):
        self.name = n
        self.rollno = r
        self.marks = m
        self.subject = s

s1 = Student("Kriti", 20, 30, "C++")
# s1.name = "Kriti"
# s1.rollno = 20
# s1.marks = 30

print(s1.name, s1.rollno, s1.subject, s1.marks)

s2 = Student("Ritvik", 15, 0)
# s2.name = "Ritvik"
# s2.rollno = 15
# s2.marks = 0

print(s2.name, s2.rollno, s2.subject, s2.marks)