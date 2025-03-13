inp = int(input(""))
interest = int(inp * 0.0375)
fee = int(interest * 0.15)
pandi = inp + interest - fee
print('{:10s} {:15,d}'.format('principal',inp))
print('{:10s} {:15,d}'.format('interest',interest))
print('{:10s} {:15,d}'.format('fee',fee))
print('{:10s} {:15,d}'.format('P and I',pandi))