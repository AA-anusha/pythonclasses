first_name = raw_input('Your first name: ')
last_name = raw_input('Your last name: ')

# Old style formatting.
print('Hello %s %s!' % (first_name, last_name))

# New Style formatting
print('Hello {} {}!'.format(first_name, last_name))
print('Hello {0} {1}!'.format(first_name, last_name))

# This is where, you will feel the difference.
print('Hello {1} {0}!'.format(first_name, last_name))
print('Hello {0} {0} {1}!'.format(first_name, last_name))