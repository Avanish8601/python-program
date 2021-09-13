class MsgError(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)
class AgeError (Exception):
    def __init__(self,message):
        Exception.__init__(self,message)
class MobileError(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)
try:
    name=input("enter name:")
    if len(name)<=3:
        raise NameError("name is to short")
    for i in (name):
        if (ord(i) not in range (65,91) and ord(i) not in range(97,123) and ord(i)!=32):



            raise NameError("name should not allow numerical or special charecter")

    age=int(input("enter age:"))
    if age<18 or age >=60:
        raise AgeError(" age is less than 18 or grater than 60")

    mobile=int(input("enter mobile no:"))
    if mobile>=10:
        raise MobileError("Error, please enter 10 digits numbers")
except Exception as e:1
else:
    print("correct details")
"""finally:
    print("exit")"""