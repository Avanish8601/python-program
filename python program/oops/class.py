class person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def __str__(self):
        return "name={0},age={1},address={2}".format(self.name,self.age,self.address)
p=person("ram",36,"varanasi")
print(p)
