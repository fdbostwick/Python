import re
import sys
def read_func():
    datafile = open("data.txt","r")
    content = datafile.readlines()
    content = [x.strip() for x in content]
    records = []
    for x in content:
        records.extend(x.split('\n'))
    datafile.close()
    return records
def query_func(cond,field):
    print(cond,field)
    if cond == [''] and field == ['']:
        content = read_func()
        for x in content:
            start = x.find('DocID')
            end = None
            z = x[start:end].split(' ')
            z = z[0]
            x = x.replace(z,'')
            print(x.strip())
        return
    op = []
    conds = []
    for x in cond:
        if '<=' in x:
            conds.append(x.split('<='))
            op.append('<=')
        elif '>=' in x:
            cond.append(x.split('>='))
            op.append('>=')
        elif '<>' in x:
            conds.append(x.split('<>'))
            op.append('<>')
        elif '>' in x:
            conds.append(x.split('>'))
            op.append('>')
        elif '<' in x:
            conds.append(x.split('<'))
            op.append('<')
        elif '=' in x:
            conds.append(x.split('='))
            op.append('=')
        else:
            print("Invalid operator")
            return
    print(conds,op,field)    
    content = read_func()
    results = []
    for x in content:
        for y,z in zip(conds,op):
            #print(y[0],y[1])
            #print(x)
            start = x.find(y[0])
            #print(start)
        if start > -1:
            print("Got here")
            end = None
            value = x[start:end].split(' ')
            #print(value[0])
            #print(value[:len(y[0])])
            #print(len(y[0]))
            val = value[0][0:len(y[0])]
            #print(val)
            num = value[0][len(y[0])+1:end]
            #print(num)
            correct = ''
            #print(num,val)
            print(z)
            if z == '<=':
                if num <= y[1]:
                    correct = val
            elif z == '>=':
                if num >= y[1]:
                    correct = val
            elif z == '<>':
                if num != y[1]:
                    correct = val
            elif z == '<':
                if num < y[1]:
                    correct = val
            elif z == '>':
                if num > y[1]:
                    correct = val
            elif z == '=':
                if num == y[1]:
                    correct = val
            elif z == '':
                correct = 1
            print(correct)
            if correct != '':        
                #sys.stdout.write(correct)      
                for y in field:
                    start = x.find(y)
                    if start == -1:
                        sys.stdout.write(y + ":NA" + " ")
                    else:    
                        step = x[start:end].split(' ')
                        sys.stdout.write(step[0] + " ")
                print()        
def count_func(field,cond):
    content = read_func()
    count = 0
    if cond[0] == '0':
        for x in content:
            start = x.find(field[0])
            if start > -1:
                count = count +1
    else:
        nums = []
        for x in content:
            start = x.find(field[0])
            if start > -1:
                end = None
                snip = x[start:end]
                start = snip.find(" ")
                if start > -1:
                    snip = snip[0:start]
                nums.append(snip[len(field[0])+1:end])
            count = len(list(set(nums)))
    print(count)            
def insert_func(items):
    flag = 0
    val = -1
    oldV = 0
    for x in items:
        if 'DocID' in x:
            vals = x.split(':')
            val = vals[1]
    content = read_func()
    maxim = -1
    for x in content:
        stuff = x.split(' ')
        for y in stuff:
            if 'DocID' in y:
                oldVs = y.split(':')
                oldV = oldVs[1]     
        if oldV == val:
            print("Duplicate DocID Error!")
            return
        elif int(oldV) > int(maxim):
            maxim = oldV        
    if items[0][0:5] != 'DocID':
        for x in items:
            if 'DocID' in x:
                flag = 1
                temp = items.pop(items.index(x))
                items.insert(0,temp)
        if flag == 0:
            maxim = int(maxim) + 1
            doci = 'DocID:{}'.format(maxim)
            items.insert(0,doci)
    for x in items:
        sys.stdout.write(x)
        sys.stdout.write(' ')
    print()
    with open('data.txt','a+') as f:
        f.write("\n")
        for x in items:
            f.write("%s " % x)
            
def my_function(x):
    if len(x) > 1:
        if "query" in x[1]:
            x = x[1].split('query')
            y = x[1].split('],[')
            conditions = y[0][2:].split(',')
            y = x[1].split('],[')
            fieldNames = y[1].split(',')
            fieldNames[-1] = fieldNames[-1][:-2]
            query_func(conditions,fieldNames)
        elif "count" in x[1]:
            x = x[1].split('count')
            y = x[1].split('],[')
            conditions = y[0][2:].split(',')
            y = x[1].split('],[')
            fieldNames = y[1].split(',')
            fieldNames[-1] = fieldNames[-1][:-2]
            count_func(conditions,fieldNames)
        elif "insert" in x[1]:
            values = x[1][7:-1]
            values = values.split(' ')
            insert_func(values)
        else:
            print("Invalid Command! Try again")
    else:
        print("Invalid Command! Try again")
x = input("Enter a query or q to quit: ")
while x != "q":
    x = x.split('.')
    my_function(x)
    x = input("Enter a query or q to quit: ")
