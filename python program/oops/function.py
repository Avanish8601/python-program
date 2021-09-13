def f(n):
    result=""
    if n%2==0:
        result= 'FIZZ'
    if n%3==0:
        result=result+ 'BUZZ'
    if n%5==0:
        result=result+'FAA'
    if result.__len__()==0:
        return 'BAR'
    else:
        return result
x=f(2)
print(x)
x=f(3)
print(x)
x=f(5)
print(x)
x=f(30)
print(x)
