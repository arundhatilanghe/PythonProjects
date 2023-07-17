a=int(input("The value of a is : "))
b=int(input("The value of b is : "))
p=int(input("Enter Obtained Marks : "))
q=int(input("Enter Total Marks : "))
def Para(a,b):
    print("Value of a is : ",a)
    print("Value of b is : ",b)
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    per=((p*100)/q)
    obtain=((per*q)/100)
    avg=(a+b+p+q)/4
    print("sum of a & b is :",sum,"\n","sub of a & b is :",sub," \n","mul of a & b is :",mul,"\n",
          "div of a & b is :",div,"\n","per is :",per,"\n","Obtained Marks are :",obtain,"\n",\
          "average is :",avg,"\n")