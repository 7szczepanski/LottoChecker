'''

Created by Mateusz Szczepanski 21-04-2017

This is simple problem to solve I just want to program something :)

So, we are generating random 6 numbers and then we will try to find another 6 numbers that are the same as the initial one
I just want to show my friends how little chance you have to actualy win on lottery

Now let's add counter of partial hits i.e 3,4,5 hits 

1,2,3,4,5,6
1,2,3,6,8,22

There is small posibility of having same numbers in one list i.e [1,2,2,4,5,7] but it is actualy not very heavy for our computers :)

'''


import random

def randcurrent():
    current = [None] * 6
    x = 0
    while x < 6:
        current[x] = random.randint(1, 49)
        x += 1
    current.sort()
    return current

def randiter():
    iter = [None]*6
    i = 0
    while i<6:
        iter[i] = random.randint(1,49)
        i+=1
    iter.sort()
    return iter

def main():

    counter = 0
    curr = randcurrent()
    curriter = 0
    print("Our current numbers are: ",curr,"\n")
    while curr != curriter:
        hits = 0
        curriter = randiter()
        for i in range(0,len(curriter)):
            for j in range(0,len(curr)):
                if curriter[i]==curr[j]:
                    hits +=1
        counter +=1
        print("Try nr: ",counter," numbers: ",curriter,"We have: ",hits," hits. \n")


    print("We have one it is try numer: ", counter)

if __name__ == '__main__':
    main()