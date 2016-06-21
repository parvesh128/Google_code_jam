original_stack = []
flipped_stack = []
num_flips = 0
output = []

first_bad_found = False

def rev_srch_list(lst,item):
    return len(lst) - lst[::-1].index(item) -1


def push_in_flipped_stack(stack,item):
    if (item == '-'):
        stack.insert(0,'+')
    else:
        stack.insert(0,'-')

    return stack

def flip_bring_back(last_idx):
    global original_stack
    global flipped_stack

    flipped_stack = []
    print ("Before flipping " + str(original_stack))

    for itr in range(0,last_idx+1):
        push_in_flipped_stack(flipped_stack,original_stack.pop(0))
        print ("During flipping Flipped stack:" + str(flipped_stack) + "Original stack: " + str(original_stack)) #debug

    copy_flipped_stack = flipped_stack
    for i in range(0,len(copy_flipped_stack)):
        original_stack.insert(0,flipped_stack.pop(0))

    print ("After flipping " + str(original_stack))



def take_revenge():
    global  original_stack
    global num_flips
    num_flips = 0
    copy_stack = original_stack

    for i in range(0,len(copy_stack)-1):
        if('-' not in original_stack):
            break # done
        #Greedy logic
        if(original_stack[i] == original_stack[i+1]):
            continue
        else:
            print ("Flip upto: "+str(i))
            flip_bring_back(i) #FLip 0 to i
            num_flips = num_flips + 1
            continue

    if '-' in original_stack:
        flip_bring_back(len(copy_stack)-1)
        num_flips = num_flips + 1

    print(original_stack)
    print (num_flips)



f = open("B-large-practice.in","r")
num_cases = int(f.readline())

for i in range(0,num_cases):
    original_stack = list(f.readline())
    if original_stack[-1] == "\n":
        original_stack = original_stack[:-1]
    print (original_stack)
    take_revenge()
    output.append(num_flips)

f.close()

f = open("B-large-practice.out","w")
ctr=1
for x in output:
    f.write("Case #"+str(ctr)+": "+str(x) + "\n")
    ctr = ctr + 1

f.close()







