from APPLICATION.Application import Application

class ClassType(Application):
    def select(self):
        print("Please select class type 1. Internship 2. Job Assistance:- ")
        n=int(input())
        return n
    def getInternship(self):
        print("You are eligible for the internship")
    def getJob(self):
        print("You are eligible for the job")