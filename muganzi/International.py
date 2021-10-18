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
