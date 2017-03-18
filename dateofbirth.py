bdate= raw_input("enter the birthdate in YYYY-MM-DD:")
f1=bdate.split("-")

dob=float(f1[0]) + float(f1[1])/12 + float(f1[2])/365
[py,pm,pd]=['2017','03','19']
pdate=float(py) + float(pm)/12 + float(pd)/365
years=pdate-dob
months=(years - int(years))*12
print "your age is %d years and %d months" %(years,months)

