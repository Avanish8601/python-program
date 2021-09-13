try:
    d={1:"one"}
    print(d[1])
    age = int(input("enter age:"))
    if (age < 0):
        raise ValueError("age is negative")
    f=100/2

except KeyError as e:
    print('error' + str(e))
except ValueError as v:
    print("Value error" +str(v))
except ZeroDivisionError as z:
    print("zeroerror" + str(z))
except Exception as k:
    print("Unknown error" +str(k))
else:
    print("no error occured")
finally:
    print("bye bye")


