print("--------------------------------------------------------------")
print()
print("This is the program to implement rsa algorithm")
print()


p=int(input("Enter the 1st prime no:- "))
q=int(input("Enter the 2nd prime no:- "))

n=p*q
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf






phi=(p-1)*(q-1)
print("The phi is as follows",phi)

# here i is eqvivalent to e
i=2

while(i<phi):
    a=compute_hcf(phi, i)
    if(a==1):
        break
    else:
        i+=1
print("the value of e is",i)

# plaintext
m=7
c=(m**i)%n
print("The cipher text is",c)

def Find_mod_Inverse( a, m):
    for i in range(1,m):
        if (((a % m) * (i % m)) % m == 1):
        
            #  Here i is the value of d
            return i;
        
        
  
d=Find_mod_Inverse(i,phi)  

print("The value of d is",d)
# for plaintext
m=(c**d)%n
print("The plaintext is",m)
