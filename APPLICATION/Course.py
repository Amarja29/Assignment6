# from NumberOfCourses import NumberOfCourses

class Course():

    def ProgrammingCourse(self):
        print('''Please select any of the courses:- 
        1. Python Course
        2. Java Course
        3. Both''')
        c = int(input())
        return c
    def DesignCourse(self):
        print('''Please select any of the following design courses:- 
        1. Web Design
        2. Graphics Design
        3. Both''')
        c = int(input())
        return c
    def Welcome(self):
        print("Welcome to the course.")
