class Application:
    n=0
    def select(self):
        print("Welcome to our Application. Please select any one option:- ")
        print("1. Ineuron 2. Student 3. Class Type 4. Number Of Course :- ")
        n=int(input())
        return n
    def private(self):
        __var=self.select()
        if __var==1:
            return 1
        if __var==2:
            return 2
        if __var==3:
            return 3
        if __var==4:
            return 4
        else:
            return 0
    def Welcome(self):
        print("Welcome to Application")

