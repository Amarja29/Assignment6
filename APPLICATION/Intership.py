from APPLICATION.Student import Student
from APPLICATION.ClassType import ClassType

class Intership(Student,ClassType):
    def intern(self):
        if ClassType.select(ClassType)==1:
            print("Congrulations!! You got the internship.")

    def getCerified(self):
        print("Project successfully submitted. You are certified")

    def getStudentIntern(self):
        n=Student.select(Student)
        if n==1:
            if Student.StdGrades(self)=='A':
                self.getCerified()
            else:
                print("Please enhance your grade by taking the course once again.")