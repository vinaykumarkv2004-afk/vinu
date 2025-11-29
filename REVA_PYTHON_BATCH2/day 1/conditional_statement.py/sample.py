n=int(input("enter the amount in INR"))
c100=n//100
n=n%100

c50=n//50
n=n%50

c20=n//20
n=n%20

c10=n//10
n=n%10

c2=n//2
n=n%2

c1=n//1
n=n%1

total=c100+c50+c20+c10+c2+c1
print("total number of notes:",total)
 