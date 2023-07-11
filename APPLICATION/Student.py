from APPLICATION.Application import Application

class Student(Application):
    def __init__(self,_id,_name,marks):
        self._id=_id
        self._name=_name
        self.marks=marks

    def Welcome(self):
        print("Welcome", self._name)

    def getName(self):
        return self._name
    def getId(self):
        return self._id
    def StdGrades(self):
        if self.marks>50:
            return 'A'
        else:
            return 'B'
    def select(self):
        print("Do you want to Opt for internship? 1. Yes 2. No")
        n=int(input())
        return n
