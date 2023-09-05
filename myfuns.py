def rad_deg(a):
    degree= 57.296*a
    print("the degree value is..",degree)

def deg_rad(a):
    radians=0.0174*a
    print("Radians",radians)


def binary(a):
    b=[]
    while(a>0):
        b.append(a%2)
        a=a//2
    n=len(b)
    c=b[::-1]
    for i in range(0,n):
        print(c[i],end="")

def bin_dec(n):
    sum=0
    i=0
    while(n>0):
        sum += (n%10)*(2**i)
        n=n//10
        i+=1
    return sum

def octal(value):
    print("Octal={:o}".format(value))

def hexa(value):
    print("hexa={:h}".format(value))

def toggle(x,n):
    toggel=x^(1<<n)
    return toggel

def swap(a,b):
    c=a^b
    a=c^a
    b=c^b
    return (a,b)
    
#leap year are not.....    
def leap(year):
   # year=int(input("enter the year :"))
    rem=year%4
    if (rem==0):
        #......
        print("this year ({}) is a leap year".format(year))
    else:
        print("this year ({}) is a not leap year".format(year))



#sum of the given number, example input=143 then out=8

def num_sum(n):
    sum=0
    while(n>0):
        sum += n%10
        n=n//10
    return sum


def reverse(n):    # example in=1234 out=4321
    #n=int(input("enter the number:"))
    rev=0
    while(n>0):
        rev =rev*10 + n%10
        n=n//10
    return rev

def fact(n):
    #n=int(input("enter the number"))
    factorial=1
    while(n>0):
        factorial *= n
        n=n-1
    return factorial

#strong number
def strong_num():
    def fact(n):
        fact=1
        while(n>0):
            fact *= n
            n=n-1
        return fact
    r=int(input("enter the range:"))
    count=0
    for n in range(r):
        temp=n
        sum=0
        while(n>0):
            s=n%10
            sum += fact(s)
            n=n//10
        if (temp==sum):
            print("strong number =",sum)
            count+=1
    print("tne number of strong number is ",count)


def power_num():
    base=int(input("enter the base number :"))
    n=power=int(input("enter the power number :"))
    sum=1
    while(n>0):
        sum *=base
        n=n-1
    print(sum)



def fibonacci(r):
    a=0
    b=1
    print("*****fibonacci series*****")
    print(a,b,end=" ")
    for i in range(r-2):
        c=a+b
        a=b
        b=c
        print(c,end=" ")

def lcm(a,b):
    if (a==0)^(b==0):
        print("ZeroDivisionError try again....")
    else:
        if a<b:
            max=b
        else:
            max=a
        while(1):
            if (max%a==0)&(max%b==0):
                break
            else:
                max=max+1
        return max
        
def armstrong(a):
    temp=a
    b=[]
    cout=0
    sum=0
    while(a>0):
        b.append(a%10)
        a=a//10
        cout +=1
    for i in range(cout):
        sum +=b[i]**cout
    if temp==sum:
        print("this is armstrong number..")
    else:
        print("this is not armstrong number")







