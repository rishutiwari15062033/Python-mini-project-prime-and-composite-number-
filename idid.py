#taking a string and converting into digit to find prime and composite number between the range A and B
Z=input('Enter the value of A:')
X=input('Enter the value of B:')
def prime_and_composite(Z,X):# using def function to call a function
    c=0
    p=0

    if (Z.isdigit() and X.isdigit()) or (Z.lstrip('+').isdigit() and X.isdigit()) or (X.lstrip('+').isdigit() and Z.isdigit() )or (Z.lstrip('+').isdigit() and X.lstrip('+').isdigit()) or (X.lstrip('+').isdigit() and Z.lstrip('+').isdigit() ) :
    #The isdigit() method returns True if all the characters are digits, otherwise False.
    #The lstrip() method returns a copy of the string with specified characters removed
        a=int(Z)
        b=int(X)
        if a<b:
            for a in range(a,b+1):
            #we are using b+1 beacause range function didn't include till b 
                x=1
                count=0
                while(x<=a):
                    if a%x==0:
                        count=count+1# we used this because we want to include zero also in range
                    x=x+1
                if count==2:
                    p=p+1
                    print("{} is prime number".format(a))
                elif count>2:
                    c=c+1
                    print("{} is composite number".format(a))
                else:
                    print()
            print("{} prime and {} composite number in range.".format(p,c))# The format() method formats the specified value(s) and insert them inside the string's placeholder. The placeholder is defined using curly brackets: {}.

        else:
            d=0
            d=a
            a=b
            b=d
            for a in range(a,b+1):
                x=1
                count=0
                while(x<=a):
                    if a%x==0:
                        count=count+1
                    x=x+1
                if count==2:
                    p=p+1
                    print("{} is prime number".format(a))
                elif count>2:
                    c=c+1
                    print("{} is composite number".format(a))
                else:
                    print()
    
            print("{} prime and {} composite number in range.".format(p,c))
    elif (Z.lstrip('-').isdigit() and X.isdigit()) or (X.lstrip('-').isdigit() and Z.isdigit()) or (X.lstrip('+').isdigit() and X.isdigit()) or (X.lstrip('+').isdigit() and Z.isdigit() ) :
        a=int(Z)
        b=int(X)
        if a<b:
            for a in range(a,b+1):
                x=1
                count=0
                while(x<=a):
                    if a%x==0:
                        count=count+1
                    x=x+1
                if count==2:
                    p=p+1
                    print("{} is prime number".format(a))
                elif count>2:
                    c=c+1
                    print("{} is composite number".format(a))
                else:
                    print()
            print("{} prime and {} composite number in range.".format(p,c))
        else:#for conditions like a>b
            print("A>B so we will swap A and B to find composite and prime in give range")
            d=0
            d=a
            a=b
            b=d
            for a in range(a,b+1):
                x=1
                count=0
                while(x<=a):
                    if a%x==0:
                        count=count+1
                    x=x+1
                if count==2:
                    p=p+1
                    print("{} is prime number".format(a))
                elif count>2:
                    c=c+1
                    print("{} is composite number".format(a))
                else:
                    print()
    
            print("{} prime and {} composite number in range.".format(p,c))
    
    elif  type(Z)==str or type(X)==str or Z.isdecimal() or X.isdecimal():#.isdecimal function is used to check string is in decimal or not
    
        print(" can not find prime and composite number between this range.")
    
    else:
        print(" can not find prime and composite number between this range.")
prime_and_composite(A,B)
