"""
Number Theory 
Write a program that solves the congruence
ax ≡ c (mod m). [If gcd(a, m) does not divide c, return an error message and the value of gcd(a, m).]
"""

"""
This function calculates greatest common divisor 
"""
def gcd(a,b):
    while b != 0:
        a,b=b,a%b


    return a
"""
This Function calculates all incongruent solutions of each linear congruence
Note: In for this program to work you must be able to out a and m into a linear
equation.
"""
def egcd(a,b):
        if b==0:
            return a,1,0
        (x,g,v,w) = (1,a,0,b)
        while w !=0 :
            (x,g,v,w) = (v,w,x-(g//w)*v,g%w)
        x=x%(b/g)
        #print(x,g,v,w)
        return g,x,(g-a*x)//b
"""
This funcion calculates allpossible solutions for X in our equation ax=m mod b for congruency
"""

def congruence(a,b,m):
    p=b//gcd(a,m)
    
   # print (p)
    #check 
    if b%gcd(a,m) != 0:
        return "error",gcd(a,m)
    (g,x,y)=egcd(a,m)
    #print(g,x,y)
    u=p*x
    v=p*y
    print("All Possible solution(s) for x are:")
    #print("x=",u)
    for i in range(0, gcd(a,m)):
        k=1
        x1=u+(m//gcd(a,m))*k
        print("x=",int(u))
        u=x1
        k=k+1 

    
    

    
    

    
