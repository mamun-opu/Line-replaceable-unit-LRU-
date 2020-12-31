
n = int(input('n : '))
m = int(input('m : '))

column = int(n)
row = int(m/n)

cache = [[-1 for x in range(column)] for x in range(row)]

LRU = []
list_input = []

#taking input of list..........................................
while True:
    input_value = int(input())
    if input_value == -1:
        break
    list_input.append(input_value)

#taking input of list..........................................

status = ''
con = ''
x = -2

#print function .........................................
def print_func(s):
    print(s)
    for r in range(row):
        for c in range(column):
            if cache[r][c] == -1:
                print('B   ', end="")
            else:
                print(cache[r][c] , end="")
                print('   ',end="")
        print()

#print function .........................................


for j in range (len(list_input)):
    set_num = list_input[j] % row


    for i in range (column):
        if cache[set_num][i] == -1:
            cache[set_num][i] = list_input[j]
            LRU.append(list_input[j])
            con = 'yes'
            break
    if con == 'yes':
        con = 'no'
        status = 'Miss'
        print_func(status)
        continue
    for i in range (column):
        if cache[set_num][i] != -1:
            if cache[set_num][i] == list_input[j]:
                LRU.remove(list_input[j])
                LRU.append(list_input[j])
                con = 'yes'
    if con == 'yes':
        con = 'no'
        status = 'Hit'
        print_func(status)
        continue
    it = 0
    for i in range(column):
        if cache[set_num][i] != -1:
            it += 1
    if it == column:
        for k in range(len(LRU)):

            if LRU[k] % row == set_num:
                x = LRU[k]
                break
        for i in range(column):
            if cache[set_num][i] == x:
                cache[set_num][i] = list_input[j]
                LRU.remove(x)
                LRU.append(list_input[j])
                con = 'yes'
                break
    if con == 'yes':
        con = 'no'
        status = 'Miss'
        print_func(status)
        continue
