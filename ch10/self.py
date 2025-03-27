class Emp:
    name = "vishal"   
    salary= 10000000000000000000000000000000000
    id = 107
    def getinfo(self):
        print(f"the name of employee is {self.name} and salary is {self.salary}. ")
    
    @staticmethod
    def greet():
        print("hello user as we dont't need any attributes from the emp class so we can use it as static method")

vishal = Emp()
vishal.greet()
vishal.getinfo()
        #or
Emp.getinfo(vishal)
