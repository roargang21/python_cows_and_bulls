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
elif user_input > 0:
    rem_two()


guess_two_onwards = f[0]




##while user_input != 30:
    
    

print(len(f))
print(f)     

#print(x)

