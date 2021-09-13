class Currency:
    def manage(self,n):
        if n<10:
            return "0{0}".format(n)
        return "{0}".format(n)
    def __init__(self,rupees,paisa):
        self.total=100*rupees+paisa
    def __str__(self):

        r=self.total//100
        p=self.total%100
        r=self.manage(r)
        p=self.manage(p)

        return ("₹{0}.{1}".format(r,p))
    def __add__(self, other):
        return (Currency(0,self.total+ other.total))
    def __sub__(self, other):
        return (Currency(0,self.total- other.total))
    def __gt__(self, other):
        return self.total>other.total
    def __lt__(self, other):
        return self.total<other.total
c1=Currency(100,5)
c2=Currency(150,10)
print(c1)
print(c2)
sum=c1+c2
print("sum=",sum)
sub=c2-c1
print("sub=",
      sub)

if c1>c2:
    print("grater=",c1)
else:
    print("less=",c2)
if c1<c2:
    print("grater=",c2)
else:
    print("less=",c1)