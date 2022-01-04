n=int(input("Enter an integer:"))
print("The divisors of the number are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)

"""
~/Desktop/sem3_a/python ❯ python3 Q10.py                               15:36:48
Enter an integer:26
The divisors of the number are:
1
2
13
26

"""