class A:
    def f1(self):
        print("f1 in A")
    def f2(self):
        print("f2 in A")
class B:
    def f1(self):
        print("f1 in B")
class C(A,B):
    def f(self):
        A().f1()
        B().f1()
c=C()
c.f()

