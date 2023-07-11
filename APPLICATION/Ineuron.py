from APPLICATION.Application import Application
class Ineuron(Application):
    def Welcome(self):
         print("Welcome to iNeuron !!!")
    def select(self):
        print("Please select any one option 1. Affiliates 2. iNeuron Blog")
        n=int(input())
        return n
    def getInfo(self):
        l=["Krish Nair", "Sudhanshu Kumar"]
        print("Names of the Mentors :-",l)
        a='''iNeuron is a Data Science learning platform with various job assistance courses. 
        It has various training and internship opportunities as well. You can opt for multiple 
        different types of other programming languages courses as well.'''
        print(a)



