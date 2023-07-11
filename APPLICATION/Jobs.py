from APPLICATION.ClassType import ClassType


class Jobs(ClassType):
    def eligile(self, offer):
        if offer==1:
            print("Congratulations! You got the job!")
        else:
            print("Try harder")