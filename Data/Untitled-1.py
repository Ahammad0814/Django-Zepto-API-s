# num=int(input("enter number "))
#b=int(input("enter secounnd value "))
#if n%2==0:
#    if (n<=5 and n>=2) or n>=20:
#     print(n," Not wired")
#      elif n>=6 and n<=20:
 #    print(n,"wired")
#else:
 #   print(n,"wired")
#print(a+b)
#print(a-b)
#print(a*b)
#print(a//b)
#print(a/b)
#i=0
#while i < n:
# print(i)
#i +=1
#for i in range (n):
#print(i**2)
#def is_leap(year):
#    if (year%400==0) or (year%4==0 or year%100!=0):
#        print(year," is leap year")
#    else:
#       print(year," is not a leap year") 
#is_leap(year)
# i=1
# for i in range(i, num+1):
#     if i==3:
#         print()
#     print(i,end=" ")
    
x = [0,3,4,6,3,5,6,7,6,6,6]

first = x[0]  #4
second = x[1]  #3

for i in x:
    if i > first: #  > 4
        second = first
        first = i

    if i > second and i!= first: #0 > 3
        second = i

print(first,second)