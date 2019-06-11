 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
 Once 'done' is entered, print out the largest and smallest of the numbers. 
 If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
 Enter 7, 2, bob, 10, and 4 and match the output below.
 
 a=None
b=None
while True:
    c=input('Enter a Value:')
    if c=='done':
        break
                
    try:
        c=int(c)
    except:
        print("Invalid input")
        continue
    if a is None:
        a=c
    elif a<c:
        a=c
    if b is None:
        b=c
    elif b>c:
        b=c
            
print('Maximum is',a)
print('Minimum is',b)
