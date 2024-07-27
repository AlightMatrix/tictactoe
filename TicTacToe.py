import random

inv = {'a1' : ' ' , 'a2' : ' ' , 'a3' : ' ' ,
       'b1' : ' ' , 'b2' : ' ' , 'b3' : ' ' ,
       'c1' : ' ' , 'c2' : ' ' , 'c3' : ' '}

disp = {'a1' : '1' , 'a2' : '2' , 'a3' : '3' ,
       'b1' : '4' , 'b2' : '5' , 'b3' : '6' ,
       'c1' : '7' , 'c2' : '8' , 'c3' : '9'}

checks = [
    ['a1' , 'a2' , 'a3'],
    ['b1' , 'b2' , 'b3'],
    ['c1' , 'c2' , 'c3'],
    ['a1' , 'b1' , 'c1'],
    ['a2' , 'b2' , 'c2'],
    ['a3' , 'b3' , 'c3'],
    ['a1' , 'b2' , 'c3'],
    ['a3' , 'b2' , 'c1']
]

def menu():
    print("MENU:")
    print("A - Start")
    print("B - Help")
    start = str(input("Enter Option: "))
    print()
    start = start.upper()
    return start

def display():
    print(disp['a1'] , '|' , disp['a2'] , '|' , disp['a3'])
    print('----------')
    print(disp['b1'] , '|' , disp['b2'] , '|' , disp['b3'])
    print('----------')
    print(disp['c1'] , '|' , disp['c2'] , '|' , disp['c3'])

def diff():
    print('1 - Easy')
    print('2 - Hard')
    print()
    dif = int(input("Choose Difficulty: "))
    return dif

def help():
    print()
    display()
    print()
    print("Input the number corresponding to the place you want to put your cross.")


def boxplay():
    print(inv['a1'] , '|' , inv['a2'] , '|' , inv['a3'])
    print('----------')
    print(inv['b1'] , '|' , inv['b2'] , '|' , inv['b3'])
    print('----------')
    print(inv['c1'] , '|' , inv['c2'] , '|' , inv['c3'])

def wincheck():
    for i in checks:
        if i[0] in x and i[1] in x and i[2] in x:
            return "You Win!"
        else:
            continue

def losecheck():
    for i in checks:
        if i[0] in o and i[1] in o and i[2] in o:
            return "You Lose."
        else:
            continue
    

def userturn():
    global x
    x = []
    while True:
        print()
        ask = str(input("Enter Place Number: "))
        for i in disp.keys():
            if disp[i] == ask:
                inv[i] = 'X'
                x.append(i)
            else:
                continue
        if wincheck() == "You Win!":
            boxplay()
            print("You Win!")
            break
        else:
            botturn()
            boxplay()
        if losecheck() == 'You Lose.':
            print('You Lose.')
            print()
            break

o = []

def turnlist():
    global turnl
    turnl = []
    for i in inv.keys():
        turnl.append(i)
    for i in x:
        if i in turnl:
            turnl.remove(i)
    for i in o:
        if i in turnl:
            turnl.remove(i)
    return turnl

def botturn():
    a = turnlist()
    botpos = random.choice(a)
    inv[botpos] = 'O'
    o.append(botpos)

def userturn_hard():
    global x
    x = []
    while True:
        print()
        ask = str(input("Enter Place Number: "))
        for i in disp.keys():
            if disp[i] == ask:
                inv[i] = 'X'
                x.append(i)
            else:
                continue
        if smartbot() == 1:
            boxplay()
            print("It's a Draw!")
            break
        elif wincheck() == "You Win!":
            boxplay()
            print("You Win!")
            break
        else:
            boxplay()
        if losecheck() == 'You Lose.':
            print('You Lose.')
            print()
            break

def smartbot():
    global lis
    lis = turnlist()

    if len(x) == 1 and 'b2' not in x and 'b2' in lis:
        inv['b2'] = 'O'
        o.append('b2')
    
    elif 'a1' in x and 'a2' in x and 'a3' in lis:
        inv['a3'] = 'O'
        o.append('a3')
    elif 'a2' in x and 'a3' in x and 'a1' in lis:
        inv['a1'] = 'O'
        o.append('a1')
    elif 'a1' in x and 'a3' in x and 'a2' in lis:
        inv['a2'] = 'O'
        o.append('a2')

    elif 'b1' in x and 'b2' in x and 'b3' in lis:
        inv['b3'] = 'O'
        o.append('b3')
    elif 'b2' in x and 'b3' in x and 'b1' in lis:
        inv['b1'] = 'O'
        o.append('b1')
    elif 'b1' in x and 'b3' in x and 'b2' in lis:
        inv['b2'] = 'O'
        o.append('b2')  

    elif 'c1' in x and 'c2' in x and 'c3' in lis:
        inv['c3'] = 'O'
        o.append('c3')
    elif 'c2' in x and 'c3' in x and 'c1' in lis:
        inv['c1'] = 'O'
        o.append('c1')
    elif 'c1' in x and 'c3' in x and 'c2' in lis:
        inv['c2'] = 'O'
        o.append('c2') 

    elif 'a1' in x and 'b2' in x and 'c3' in lis:
        inv['c3'] = 'O'
        o.append('c3')  
    elif 'c3' in x and 'a1' in x and 'b2' in lis:
        inv['b2'] = 'O'
        o.append('b2')
    elif 'b2' in x and 'c3' in x and 'a1' in lis:
        inv['a1'] = 'O'
        o.append('a1')
    
    elif 'a3' in x and 'b2' in x and 'c1' in lis:
        inv['c1'] = 'O'
        o.append('c1')
    elif 'c1' in x and 'a3' in x and 'b2' in lis:
        inv['b2'] = 'O'
        o.append('b2')
    elif 'b2' in x and 'c1' in x and 'a3' in lis:
        inv['a3'] = 'O'
        o.append('a3')

    elif 'a1' in x and 'b1' in x and 'c1' in lis:
        inv['c1'] = 'O'
        o.append('c1')
    elif 'c1' in x and 'a1' in x and 'b1' in lis:
        inv['b1'] = 'O'
        o.append('b1')
    elif 'b1' in x and 'c1' in x and 'a1' in lis:
        inv['a1'] = 'O'
        o.append('a1')

    elif 'a2' in x and 'b2' in x and 'c2' in lis:
        inv['c2'] = 'O'
        o.append('c2')
    elif 'c2' in x and 'a2' in x and 'b2' in lis:
        inv['b2'] = 'O'
        o.append('b2')
    elif 'b2' in x and 'c2' in x and 'a2' in lis:
        inv['a2'] = 'O'
        o.append('a2')

    elif 'a3' in x and 'b3' in x and 'c3' in lis:
        inv['c3'] = 'O'
        o.append('c3')
    elif 'c3' in x and 'a3' in x and 'b3' in lis:
        inv['b3'] = 'O'
        o.append('b3')
    elif 'b3' in x and 'c3' in x and 'a3' in lis:
        inv['a3'] = 'O'
        o.append('a3')

    else:
        a = turnlist()
        if len(a) == 0:
            return 1
        else:
            botpos = random.choice(a)
            inv[botpos] = 'O'
            o.append(botpos)
    print(o)




#-----------------------------------------------EXECUTION---------------------------------------------------------

initiate = menu()

if initiate == 'B':
    help()
elif initiate == 'A':
    di = diff()
    if di == 1:
        print()
        print("EASY MODE")
        print()
        boxplay()
        userturn()
    elif di == 2:
        print()
        print("MEDIUM MODE")
        print()
        boxplay()
        userturn_hard()




