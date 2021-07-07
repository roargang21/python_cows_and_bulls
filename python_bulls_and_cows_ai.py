## to create a list with all the possibilities 
## let all the possibilities be called x
## 0 is also included
x = []
## to create a function which knows all 3 digits of the number is different
## let this function be called numbers()
def numbers(element):
    if element//100 != (element%100)//10 != (element%100)%10 and (element%100)%10 != element//100:
        x.append(element)

for element in range(100,1000):
    numbers(element)
## to create a list which also includes 0 at the start
c=[]
def numtwo(elementwo):
    if elementwo//10 != elementwo%10 and elementwo%10 != 0:
        c.append(elementwo)

for elementwo in range(11,100):
    numtwo(elementwo)

## extending numbers with 0 in front
## c is not neccessary anymore
x.extend(c)
c.clear()

## guess 1 is always the same 
guess_one = 123
print("My guess is {}".format(guess_one))

user_input = int(input("Please input a bull b cow : "))
#removing elements which are not a possiblity if user_input = 0

def rem(i):
    if i//100 == 1 or (i%100)//10 == 1 or (i%100)%10 == 1 or i//10 ==1 or i%10 ==1:
        x.remove(i)
    elif i//100 == 2 or (i%100)//10 == 2 or (i%100)%10 == 2 or i//10 == 2 or i%10 == 2:
        x.remove(i)
    elif i//100 == 3 or (i%100)//10 == 3 or (i%100)%10 == 3 or i//10 ==3 or i%10 ==3:
        x.remove(i)
##removing element if input is more than 0
def rem_two():
    if user_input == 1 or user_input == 10:
        for i in x:
              if (i//100 == 1 or (i%100)//10 == 1 or (i%100)%10 == 1 or i//10 ==1 or i%10 ==1) and \
              not (i//100 == 2 or (i%100)//10 == 2 or (i%100)%10 == 2 or i//10 == 2 or i%10 == 2) and not \
              (i//100 == 3 or (i%100)//10 == 3 or (i%100)%10 == 3 or i//10 ==3 or i%10 ==3):
                f.append(i)
              elif (i//100 == 2 or (i%100)//10 == 2 or (i%100)%10 == 2 or i//10 ==2 or i%10 ==2) and \
              not (i//100 == 1 or (i%100)//10 == 1 or (i%100)%10 == 1 or i//10 == 1 or i%10 == 1) and not \
              (i//100 == 3 or (i%100)//10 == 3 or (i%100)%10 == 3 or i//10 ==3 or i%10 ==3):
                f.append(i)
              elif (i//100 == 3 or (i%100)//10 == 3 or (i%100)%10 == 3 or i//10 ==3 or i%10 ==3) and \
              not (i//100 == 2 or (i%100)//10 == 2 or (i%100)%10 == 2 or i//10 == 2 or i%10 == 2) and not \
              (i//100 == 1 or (i%100)//10 == 1 or (i%100)%10 == 1 or i//10 ==1 or i%10 ==1):
                f.append(i)
    elif user_input == 2 or user_input == 20 or user_input == 11:
        for i in x:
              if (i//100 == 1 or (i%100)//10 == 1 or (i%100)%10 == 1 or i//10 ==1 or i%10 ==1) and \
               (i//100 == 2 or (i%100)//10 == 2 or (i%100)%10 == 2 or i//10 == 2 or i%10 == 2) and not \
              (i//100 == 3 or (i%100)//10 == 3 or (i%100)%10 == 3 or i//10 ==3 or i%10 ==3):
                f.append(i)
              elif (i//100 == 3 or (i%100)//10 == 3 or (i%100)%10 == 3 or i//10 ==3 or i%10 ==3) and \
               (i//100 == 1 or (i%100)//10 == 1 or (i%100)%10 == 1 or i//10 == 1 or i%10 == 1) and not \
              (i//100 == 2 or (i%100)//10 == 2 or (i%100)%10 == 2 or i//10 ==2 or i%10 ==2):
                f.append(i)
              elif (i//100 == 3 or (i%100)//10 == 3 or (i%100)%10 == 3 or i//10 ==3 or i%10 ==3) and \
               (i//100 == 2 or (i%100)//10 == 2 or (i%100)%10 == 2 or i//10 == 2 or i%10 == 2) and not \
              (i//100 == 1 or (i%100)//10 == 1 or (i%100)%10 == 1 or i//10 ==1 or i%10 ==1):
                f.append(i)
    else:
        for i in x:
              if (i//100 == 1 or (i%100)//10 == 1 or (i%100)%10 == 1 or i//10 ==1 or i%10 ==1) and \
               (i//100 == 2 or (i%100)//10 == 2 or (i%100)%10 == 2 or i//10 == 2 or i%10 == 2) and  \
              (i//100 == 3 or (i%100)//10 == 3 or (i%100)%10 == 3 or i//10 ==3 or i%10 ==3):
                f.append(i)

## f is the main list for the main() loop
f = []
                
## to append all the numbers into f
if user_input == 0:
    for i in x:
        rem(i)
        for i in x:
          rem(i)
    f.extend(x)
elif user_input == 30:
    print("You have won")
    print("Count = 1")
elif user_input > 0:
    rem_two()


## to keep track of number of tries    
if user_input != 30:
    print("count = 1")

## defining count
count = 1
## creating a copy og loop to cycle through
f_copy = f.copy()
## main loop to find out the number
while user_input != 30:

    if f[0] > 99:
        print("My guess is {}".format(f[0]))
    else:
        print("My guess is 0{}".format(f[0]))
    user_input = int(input("Please input a bull b cow : "))

    g = f[0]//100 ##hundreds place
    h = (f[0]%100)//10 ##tens place
    z = f[0]%10 ## ones place
    if len(f) == 1 :
        print("My guess is {}".format(f[0]))
        user_input = int(input("Please input a bull b cow : "))
        if user_input == 30:
            break
    if user_input == 1 or user_input == 10:
        for i in f:
              if not ( (i//100 == g or (i%100)//10 == g or i%10 == g or i//10 ==g or i%10 ==g) and \
              not (i//100 == h or (i%100)//10 == h or i%10 == h or i//10 == h or i%10 == h) and not \
              (i//100 == z or (i%100)//10 == z or i%10 == z or i//10 ==z or i%10 ==z) ):
                f_copy.remove(i)
              elif not ( (i//100 == h or (i%100)//10 == h or i%10 == h or i//10 ==h or i%10 ==h) and \
              not (i//100 == g or (i%100)//10 == g or i%10 == g or i//10 == g or i%10 == g) and not \
              (i//100 == z or (i%100)//10 == z or i%10 == z or i//10 ==z or i%10 ==z) ):
                f_copy.remove(i)
              elif not ( (i//100 == z or (i%100)//10 == z or i%10 == z or i//10 ==z or i%10 ==z) and \
              not (i//100 == h or (i%100)//10 == h or i%10 == h or i//10 == h or i%10 == h) and not \
              (i//100 == g or (i%100)//10 == g or i%10 == g or i//10 ==g or i%10 ==g) ):
                f_copy.remove(i)
                
    elif user_input == 0:
        for i in f:
                if i//100 == g or (i%100)//10 == g or i%10 == g or i//10 ==g or i%10 ==g:
                    f_copy.remove(i)
                elif i//100 == h or (i%100)//10 == h or i%10 == h or i//10 == h or i%10 == h:
                    f_copy.remove(i)
                elif i//100 == z or (i%100)//10 == z or i%10 == z or i//10 ==z or i%10 ==z:
                    f_copy.remove(i)

    
    elif user_input == 2 or user_input == 20 or user_input == 11:
        for i in f:
              if not ( (i//100 == g or (i%100)//10 == g or i%10 == g or i//10 ==g or i%10 ==g) and \
               (i//100 == h or (i%100)//10 == h or i%10 == h or i//10 == h or i%10 == h) and not \
              (i//100 == z or (i%100)//10 == z or i%10 == z or i//10 ==z or i%10 ==z) ):
                f_copy.remove(i)
              elif not ( (i//100 == z or (i%100)//10 == z or i%10 == z or i//10 ==z or i%10 ==z) and \
               (i//100 == g or (i%100)//10 == g or i%10 == g or i//10 == g or i%10 == g) and not \
              (i//100 == h or (i%100)//10 == h or i%10 == h or i//10 ==h or i%10 ==h) ):
                f_copy.remove(i)
              elif not ( (i//100 == z or (i%100)//10 == z or i%10 == z or i//10 ==z or i%10 ==z) and \
               (i//100 ==h or (i%100)//10 == h or i%10 == h or i//10 == h or i%10 == h) and not \
              (i//100 == g or (i%100)//10 == g or i%10 == g or i//10 ==g or i%10 ==g) ):
                f_copy.remove(i)
            
    else:
        for i in f:
              if not ( (i//100 == g or (i%100)//10 == g or i%10 == g or i//10 ==g or i%10 ==g) and \
               (i//100 == h or (i%100)//10 == h or i%10 == h or i//10 == h or i%10 == h) and  \
              (i//100 == z or (i%100)//10 == z or i%10 == z or i//10 ==z or i%10 ==z) ):
                f_copy.remove(i)
    f = f_copy
    f.remove(f[0])
    count = count + 1
    print("Count = {}".format(count))
    
    



print("You have won. Count = {}".format(count))
