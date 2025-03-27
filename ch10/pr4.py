class calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self,):
        print(f"square of a number is {self.n*self.n}")

    def qube(self):
        print(f"cube of the number is :{self.n*self.n*self.n}")

    def squareroot(self):
        print(f"squareroot of the number is :{self.n**0.5}")

    @staticmethod
    def greet():
        print("hello their!!!")

a= calculator(25)
a.greet()
a.square()
a.qube()
a.squareroot()