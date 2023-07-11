# This is my application interface
from APPLICATION.Affiliates import Affiliates
from APPLICATION.Application import Application
from APPLICATION.Blog import Blog
from APPLICATION.ClassType import ClassType
from APPLICATION.Course import Course
from APPLICATION.Ineuron import Ineuron
from APPLICATION.Intership import Intership
from APPLICATION.Jobs import Jobs
from APPLICATION.NumberOfCourses import NumberOfCourses
from APPLICATION.Student import Student
from APPLICATION.Training import Training

obj = Application()
#obj.select()
choice = obj.private()

if choice == 1:
    ineuron = Ineuron()
    ineuron.Welcome()
    ineuron.getInfo()
    i = ineuron.select()
    if i==1:
        affiliates=Affiliates()
        affiliates.Welcome()
        affiliates.Procedure()
    elif i==2:
        blog=Blog(1,'Priya',89)
        blog.iNeuronBlog()
    else:
        print("Invalid Choice")
elif choice == 2:
        print("Please enter your id, name, marks and choice for internship (yes or no):-")
        id = int(input())
        name = input()
        marks = int(input())
        #c = input()
        student = Student(id,name,marks)
        print(f"Welcome {student.getName()}. Your login id is {student.getId()} and grades are {student.StdGrades()}")

        inter = Intership(id, name, marks)
        inter.getStudentIntern()


elif choice == 3:
    type = ClassType()
    #c = type.select()
    type.getInternship()
    inter = Intership(7,"abc",38)
    inter.intern()
    type.getJob()
    jobs = Jobs()
    print("Do you have an offer? yes-1 no-0:- ")
    res = int(input())
    jobs.eligile(res)

elif choice == 4:
    course = Course()
    courses = NumberOfCourses()
    print("Which course you want? 1. Programming 2. Design:- ")
    c = int(input())
    if c ==1:
        courses._NumberOfCourses__CourseCountProg()

    elif c == 2:
        courses._NumberOfCourses__CourseCountDesign()
    course.Welcome()

    courses.Welcome()
    training = Training()
    training.Progress()

else:
    print("Invalid Choice")


