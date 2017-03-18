a=raw_input("enter the marks of science")
b=raw_input("enter the marks of math")
c=raw_input("enter the marks of social")
d=raw_input("enyer the marks of nepali")
e=raw_input("enter the marks of optionalmath")

total = float(a) + float(b) +float(c) +float(d)  +float(e) 
percentage = total / 5
print ("the total is = {} ".format(total))
print ("the percentage is = {:.2f}% ".format(percentage))