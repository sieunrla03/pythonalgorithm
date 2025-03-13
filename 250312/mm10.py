inp_line = input('Input 3 integer values>> ')
line = inp_line.split()
a = int(line[0])
b = int(line[1])
c = int(line[2])

if ( c < a + b and b < a + c and a < b + c ):
	print('Yes, this is a triangle.')
else:
    print('No, this is NOT a triangle.')