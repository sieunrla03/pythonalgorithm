height = float(input("Input your height(cm):"))
Standard = (height - 100) * 0.9
Over = Standard * 1.2
Low = Standard * 0.8
print('your height:', height)
print('Standard weight:',Standard)
print('Over-weight standards:', Over)
print('Low-weight standards:', Low)