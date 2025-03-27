from random import randint

class train:

    def __init__(self,trainno):
        self.trainno= trainno

    def book(self,fro,to):
        print(f"the train no: {self.trainno} is traveling from {fro} to {to}")

    def status(self,fro,to,city):
        print(f"the train no:{self.trainno} is traveling from {fro} to {to} is running on time which will at the city {city} at the time mentioned earlier.")

    def getfare(self,fro,to):
        print(f"the fare in train no:{self.trainno} is traveling from {fro} to {to} is {randint(2222,6666)}.")

t = train(15551)
t.book ("solapur","walha")
t.status("solapur","walha","bhoom")
t.getfare("solapur","walha")