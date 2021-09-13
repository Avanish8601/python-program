from oops import personclass as p


class Employee(p.personclass):
    def __init__(self,salary, post):
        self.salary=salary
        self.post=post
     #def __init(self,name,age,address):


    def __str__(self):
        return "salary={0},post={1}".format(self.salary,self.post)
E=Employee('36000',"manager")
print(E)
