import sys


r = open(sys.argv[1],'r')


store = []
for lines in r.readlines():

    s = lines.split()
    store.append(s)

r.close()

cout = 0
for i in range(len(store)):

    if i < 2:
        continue

    if 'NCR' in store[i][0]:

        if 'NCR' in store[i][1]:
            cout += 1
            print()
            print(cout, '. Column 1 with NCR and with Pea Ortholog')
            print('   Medicago NCR -> ',store[i][0],store[i][1])
            print()
        else:
            continue
        
        if 'Med' in store[i-1][0]:
            if not store[i-1][1] == '.':
                print('   Others at -1 -> ',store[i-1][0],store[i-1][1])
        elif 'NCR' in store[i-1][0]:
            print('   *** Found NCR at -1')
            
        if 'Med' in store[i-2][0]:
            if not store[i-2][1] == '.':
                print('   Others at -2 -> ',store[i-2][0],store[i-2][1])                
        elif 'NCR' in store[i-2][0]:
            print('   *** Found NCR at -2')

        if 'Med' in store[i+1][0]:
            if not store[i+1][1] == '.':
                print('   Others at +1 -> ',store[i+1][0],store[i+1][1])
        elif 'NCR' in store[i+1][0]:
            print('   *** Found NCR at +1')

        if 'Med' in store[i+2][0]:
            if not store[i+2][1] == '.':
                print('   Others at +2 -> ',store[i+2][0],store[i+2][1])
        elif 'NCR' in store[i+2][0]:
            print('   *** Found NCR at +2')
            
        print()

