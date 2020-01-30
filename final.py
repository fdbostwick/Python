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
    #print(cond,field)
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
    vals = []
    names = []
    xlist = []
    for x in cond:
        #print(x)
        if '<=' in x:
            xlist = x.split('<=')
            names.append(xlist[0])
            vals.append(xlist[1])
            op.append('<=')
        elif '>=' in x:
            xlist = x.split('>=')
            names.append(xlist[0])
            vals.append(xlist[1])
            op.append('>=')
        elif '<>' in x:
            xlist = x.split('<>')
            names.append(xlist[0])
            vals.append(xlist[1])
            op.append('<>')
        elif '>' in x:
            xlist = x.split('>')
            names.append(xlist[0])
            vals.append(xlist[1])
            op.append('>')
        elif '<' in x:
            xlist = x.split('<')
            names.append(xlist[0])
            vals.append(xlist[1])
            op.append('<')
        elif '=' in x:
            xlist = x.split('=')
            names.append(xlist[0])
            vals.append(xlist[1])
            op.append('=')
        elif x == '':
            names.append('')
            vals.append('')
            op.append('')
        else:
            print("Invalid operator")
            return 
    #print(names,vals,op)       
    content = read_func()
    #print(content)
    results = []
    
    for a in content:
        if field == []:
            print(a)
            results.append(a)
        else:    
            for b,c,d in zip(names,op,vals):
                #print(a,b,c,d)
                start = a.find(b)
                #print(start)
                if start > -1:
                    end = None
                    value = a[start:end].split(' ')
                    #print(value)
                    val = value[0][0:len(b)]
                    num = value[0][len(b)+1:end]
                    #print(val,num)
                    #print(c)
                    if c == '<=':
                        if num <= d:
                            results.append(a)
                    elif c == '>=':
                        if num >= d:
                            results.append(a)
                    elif c == '<>':
                        if num != d:
                            results.append(a)
                    elif c == '<':
                        if num < d:
                            results.append(a)
                    elif c == '>':
                        if num > d:
                            results.append(a)
                    elif c == '=':
                        if num == d:
                            results.append(a)
                    elif c == '':
                        results.append(a)
    #print(results)
    finResults = []
    seen = set()
    for x in results:
        if x not in seen:
           finResults.append(x)
           seen.add(x)

    if len(cond) > 1:
        doubles = []
        #TRY TO FIGURE OUT AND names,ops,vals -- b,c,d
        for x in finResults:
            start1 = x.find(names[0])
            start2 = x.find(names[1])
            #print(start1,start2)
            if start1 > -1 and start2 > -1:
                end = None
                value1 = x[start1:end].split(' ')
                value2 = x[start2:end].split(' ')
                #print(value)
                val1 = value1[0][0:len(names[0])]
                num1 = value1[0][len(names[0])+1:end]
                val2 = value2[0][0:len(names[1])]
                num2 = value2[0][len(names[1])+1:end]
                #print(val,num)
                #print(c)
                #print(op[0],op[1],num1,num2)
                #print(vals)
                if op[0] == '<=':
                    if op[1] == '<=':
                        if num1 <= vals[0] and num2 <= vals[1]:
                            doubles.append(x)
                    elif op[1] == '>=':
                        if num1 <= vals[0] and num2 >= vals[1]:
                            doubles.append(x)
                    elif op[1] == '<>':
                        if num1 <= vals[0] and num2 != vals[1]:
                            doubles.append(x)
                    elif op[1] == '<':
                        if num1 <= vals[0] and num2 < vals[1]:
                            doubles.append(x)
                    elif op[1] == '>':
                        if num1 <= vals[0] and num2 > vals[1]:
                            doubles.append(x)
                    elif op[1] == '=':
                        if num1 <= vals[0] and num2 == vals[1]:
                            doubles.append(x)
                    elif op[1] == '':
                        if num1 <= vals[0]:
                            doubles.append(x)
                elif op[0] == '>=':
                    if op[1] == '<=':
                        if num1 >= vals[0] and num2 <= vals[1]:
                            doubles.append(x)
                    elif op[1] == '>=':
                        if num1 >= vals[0] and num2 >= vals[1]:
                            doubles.append(x)
                    elif op[1] == '<>':
                        if num1 >= vals[0] and num2 != vals[1]:
                            doubles.append(x)
                    elif op[1] == '<':
                        if num1 >= vals[0] and num2 < vals[1]:
                            doubles.append(x)
                    elif op[1] == '>':
                        if num1 >= vals[0] and num2 > vals[1]:
                            doubles.append(x)
                    elif op[1] == '=':
                        if num1 >= vals[0] and num2 == vals[1]:
                            doubles.append(x)
                    elif op[1] == '':
                        if num1 >= vals[0]:
                            doubles.append(x)
                elif op[0] == '<>':
                    if op[1] == '<=':
                        if num1 != vals[0] and num2 <= vals[1]:
                            doubles.append(x)
                    elif op[1] == '>=':
                        if num1 != vals[0] and num2 >= vals[1]:
                            doubles.append(x)
                    elif op[1] == '<>':
                        if num1 != vals[0] and num2 != vals[1]:
                            doubles.append(x)
                    elif op[1] == '<':
                        if num1 != vals[0] and num2 < vals[1]:
                            doubles.append(x)
                    elif op[1] == '>':
                        if num1 != vals[0] and num2 > vals[1]:
                            doubles.append(x)
                    elif op[1] == '=':
                        if num1 != vals[0] and num2 == vals[1]:
                            doubles.append(x)
                    elif op[1] == '':
                        if num1 != vals[0]:
                            doubles.append(x)
                elif op[0] == '<':
                    if op[1] == '<=':
                        if num1 < vals[0] and num2 <= vals[1]:
                            doubles.append(x)
                    elif op[1] == '>=':
                        if num1 < vals[0] and num2 >= vals[1]:
                            doubles.append(x)
                    elif op[1] == '<>':
                        if num1 < vals[0] and num2 != vals[1]:
                            doubles.append(x)
                    elif op[1] == '<':
                        if num1 < vals[0] and num2 < vals[1]:
                            doubles.append(x)
                    elif op[1] == '>':
                        if num1 < vals[0] and num2 > vals[1]:
                            doubles.append(x)
                    elif op[1] == '=':
                        if num1 < vals[0] and num2 == vals[1]:
                            doubles.append(x)
                    elif op[1] == '':
                        if num1 < vals[0]:
                            doubles.append(x)
                elif op[0] == '>':
                    if op[1] == '<=':
                        if num1 > vals[0] and num2 <= vals[1]:
                            doubles.append(x)
                    elif op[1] == '>=':
                        if num1 > vals[0] and num2 >= vals[1]:
                            doubles.append(x)
                    elif op[1] == '<>':
                        if num1 > vals[0] and num2 != vals[1]:
                            doubles.append(x)
                    elif op[1] == '<':
                        if num1 > vals[0] and num2 < vals[1]:
                            doubles.append(x)
                    elif op[1] == '>':
                        if num1 > vals[0] and num2 > vals[1]:
                            doubles.append(x)
                    elif op[1] == '=':
                        if num1 > vals[0] and num2 == vals[1]:
                            doubles.append(x)
                    elif op[1] == '':
                        if num1 > vals[0]:
                            doubles.append(x)
                elif op[0] == '=':
                    #print("got here")
                    if op[1] == '<=':
                        if num1 == vals[0] and num2 <= vals[1]:
                            doubles.append(x)
                    elif op[1] == '>=':
                        if num1 == vals[0] and num2 >= vals[1]:
                            doubles.append(x)
                    elif op[1] == '<>':
                        if num1 == vals[0] and num2 != vals[1]:
                            doubles.append(x)
                    elif op[1] == '<':
                        #print("hello")
                        if num1 == vals[0] and num2 < vals[1]:
                            doubles.append(x)
                    elif op[1] == '>':
                        #print("hello")
                        #print(num1,num2,vals)
                        if num1 == vals[0] and num2 > vals[1]:
                            doubles.append(x)
                    elif op[1] == '=':
                        if num1 == vals[0] and num2 == vals[1]:
                            doubles.append(x)
                    elif op[1] == '':
                        if num1 == vals[0]:
                            doubles.append(x)
                elif op[0] == '':
                    if op[1] == '<=':
                        if num2 <= vals[1]:
                            doubles.append(x)
                    elif op[1] == '>=':
                        if num2 >= vals[1]:
                            doubles.append(x)
                    elif op[1] == '<>':
                        if num2 != vals[1]:
                            doubles.append(x)
                    elif op[1] == '<':
                        if num2 < vals[1]:
                            doubles.append(x)
                    elif op[1] == '>':
                        if num2 > vals[1]:
                            doubles.append(x)
                    elif op[1] == '=':
                        if num2 == vals[1]:
                            doubles.append(x)
                    elif op[1] == '':
                            doubles.append(x)
        #print(doubles)                    
        finResults.clear()
        finResults = doubles
    if finResults != '':
        for x in finResults:
            #sys.stdout.write(correct)      
            for y in field:
                start = x.find(y)
                if start == -1:
                    sys.stdout.write(y + ":NA" + " ")
                else:    
                    step = x[start:end].split(' ')
                    sys.stdout.write(step[0] + " ")
            print()
    return        
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
    return
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
        f.write(" ".join(map(str,items)))
            
    return        
def my_function(x):
    if len(x) > 1 and "final" in x:
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
            print("Query semantic error!")
    else:
        print("Query semantic error!")
    return

def main():
    x = input("Enter a query or q to quit: ")
    while x != "q":
        x = x.split('.')
        my_function(x)
        x = input("Enter a query or q to quit: ")
main()        
