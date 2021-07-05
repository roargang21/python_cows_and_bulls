## to create a list with all the possibilities 
## let all the possibilities be called x
## 0 is also included
x = []
## to create a function which knows all 3 digits of the number is different
## let this function be called numbers()
f =[]

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

  
## extending the list with the numbers that have 0 in front
x.extend(c)

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

if user_input == 0:
    for i in x:
        rem(i)
        for i in x:
          rem(i)
    f.extend(x)
elif user_input == 30:
    print("You have won")
    print("Number of guesses = 1")
elif user_input > 0:
    rem_two()


guess_two_onwards = f[0]
## for 3 digits number that dosent start with 0
g = guess_two_onwards//100 ##hundreds place
h = (guess_two_onwards%100)//10 ##tens place
z = (guess_two_onwards%100)%10 ## ones place
## count number of turns\
count = 1

## main loop to find out the number
def main():
    if user_input == 1 or user_input == 10:
        for i in f:
              if not ( (i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g) and \
              not (i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h) and not \
              (i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z) ):
                f.remove(i)
              elif not ( (i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 ==h or i%10 ==h) and \
              not (i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 == g or i%10 == g) and not \
              (i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z) ):
                f.remove(i)
              elif not ( (i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z) and \
              not (i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h) and not \
              (i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g) ):
                f.remove(i)
    elif user_input == 0:
        for i in f:
                if i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g:
                    f.remove(i)
                elif i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h:
                    f.remove(i)
                elif i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z:
                    f.remove(i)
                    
        for i in f:
                if i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g:
                    f.remove(i)
                elif i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h:
                    f.remove(i)
                elif i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z:
                    f.remove(i)
        for i in f:
                if i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g:
                    f.remove(i)
                elif i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h:
                    f.remove(i)
                elif i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z:
                    f.remove(i)
        for i in f:
                if i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g:
                    f.remove(i)
                elif i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h:
                    f.remove(i)
                elif i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z:
                    f.remove(i)
                    
        for i in f:
                if i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g:
                    f.remove(i)
                elif i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h:
                    f.remove(i)
                elif i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z:
                    f.remove(i)
        for i in f:
                if i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g:
                    f.remove(i)
                elif i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h:
                    f.remove(i)
                elif i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z:
                    f.remove(i)
        for i in f:
                if i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g:
                    f.remove(i)
                elif i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h:
                    f.remove(i)
                elif i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z:
                    f.remove(i)
                    
        for i in f:
                if i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g:
                    f.remove(i)
                elif i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h:
                    f.remove(i)
                elif i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z:
                    f.remove(i)
       
        
                    
    elif user_input == 2 or user_input == 20 or user_input == 11:
        for i in f:
              if not ( (i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g) and \
               (i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h) and not \
              (i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z) ):
                f.remove(i)
              elif not ( (i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z) and \
               (i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 == g or i%10 == g) and not \
              (i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 ==h or i%10 ==h) ):
                f.remove(i)
              elif not ( (i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z) and \
               (i//100 ==h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h) and not \
              (i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g) ):
                f.remove(i)
    else:
        for i in f:
              if not ( (i//100 == g or (i%100)//10 == g or (i%100)%10 == g or i//10 ==g or i%10 ==g) and \
               (i//100 == h or (i%100)//10 == h or (i%100)%10 == h or i//10 == h or i%10 == h) and  \
              (i//100 == z or (i%100)//10 == z or (i%100)%10 == z or i//10 ==z or i%10 ==z) ):
                f.remove(i)


while user_input != 30:
    print("My guess is {}".format(guess_two_onwards))
    user_input = int(input("Please input a bull b cow : "))
    guess_two_onwards = f[0]
    main()
    count = count + 1
    print(f)
    
print("You have won. Count = {}".format(count))
    
    
    
    

print(len(f))
print(f)     

#print(x)



