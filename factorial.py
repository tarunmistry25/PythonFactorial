
while True:
    number1=int(input("Enter number "))
    number2=number1+1
    multipliers=list()
    for i in range(number1,0,-1):
        multipliers.append(i)
        #print(i)
    import operator
    import functools
    result = functools.reduce(operator.mul,multipliers, 1)
    print(result)
