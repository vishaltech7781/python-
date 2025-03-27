class programer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name 
        self.salary = salary
        self.pin = pin

p = programer("vishal",1000000,413001)
print(p.name,p.salary,p.company,p.pin)       
p = programer("yash",2000000,413002)
print(p.name,p.salary,p.company,p.pin)  