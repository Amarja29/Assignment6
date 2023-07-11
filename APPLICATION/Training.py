from APPLICATION.NumberOfCourses import NumberOfCourses
import math

class Training(NumberOfCourses):


    def Progress(self):
        print("Please enter the number of lectures and assignments you have done :- ")
        num1 = int(input())
        num2 = int(input())
        per1 = (num1/450) * 100
        per2 = (num2/150) * 100
        print(f"You have completed {math.ceil(per1)}% lectures and {math.ceil(per2)}% assignments!")