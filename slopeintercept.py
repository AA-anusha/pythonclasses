eq= raw_input ("enter the equation:")

parts=eq.split("=")[1]
first=parts.split("+")

second=first[0].replace('x','').strip()

third=first[1].strip()
print "slope of line:",second
print "intercept of line:",third



