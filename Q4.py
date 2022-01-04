a=str(input("Enter the name of the file with .txt extension:"))
file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()

"""
for this program you all need test.txt file in same folder where Q4.py is

~/Desktop/sem3_a/python ❯ python3 Q4.py                                15:21:05
Enter the name of the file with .txt extension:test.txt
Hello from txt file....

"""