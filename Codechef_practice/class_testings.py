class Employee:
    company="google"
    def __init__(self,age,salary=100000):
        self.name="JOHN"
        self.age=30
        self.salary=100000

e1=Employee(30)
print(e1.name,e1.age,e1.salary)