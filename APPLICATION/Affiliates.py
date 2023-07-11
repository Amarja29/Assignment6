from APPLICATION.Ineuron import Ineuron

class Affiliates(Ineuron):
    def Welcome(self):
        print("Attain financial freedom by under-line joining our affiliate program")
    def Procedure(self):
        print("Do you want to be an Affilate?")
        answer = input()
        if answer == "yes":
            print("You can refer and start earning now")