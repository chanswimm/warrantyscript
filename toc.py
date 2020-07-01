print('Warranty Check:')

print(' 1. Dell\n 2. Lenovo\n 3. HP')
num = float(input("Enter Manufactuer Number: "))

if num == 1:
    import dell_inc
elif num == 2:
    import lenovo
elif num == 3:
    import hp
else:
    print('Does not exist')
