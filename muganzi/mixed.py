import random
ret = random.randint(1,99)
# random number generator
start = 0
end = 99
# please input your guessing number
while True:
    boom = int(input("Please input a number from {} to {}:".format(start,end))) # transfer your string number into int
    if boom > ret :
        print ("Too large")
        end = boom
    elif boom < ret:
        print("Too small")
        start = boom
    else:
        print ("Boom!!")
        break


    import keyword
keyword.kwlist
if True:
    print ("True")
else:
    print ("False")
    

counter = 100  # integer
miles = 1000.0 # float
name = "Hello" # string

print (counter)
print (miles)
print (name)

a = b = c = 1
print(a,b,c)

a = 512
b = 24
print(a + b)    #536
print(a - b)    # 488
print(a * b)    # 12288
print(a / b)    # 21.33333333332

a = 50
b = 18
a += b    # a = a + b
a *= a+2  # a = a * (a+2)
print (a)