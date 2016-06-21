
import sys
numbers_seen = {}

def breaknumber(N):
    global numbers_seen
    temp = N
    while 1:
        rem = temp % 10
        temp = temp/ 10
        if rem not in numbers_seen.keys():
            numbers_seen[rem] = 1
            #print("Digits seen till now:  " + str(numbers_seen.keys()))
            if len(numbers_seen) == 10:
                return True

        if temp == 0 :
            break
    return False

def count(N):
    global  numbers_seen
    buf = {}
    ctr = 1
    while 1:
        temp = ctr*N
        ctr = ctr + 1
        if temp in buf.keys():
            numbers_seen = {}
            return "INSOMNIA"

        else:
            buf[temp] = 1
            #print("Numbers seen till now:  " + str(buf.keys()))
            if(breaknumber(temp)):
                numbers_seen = {}
                return str(temp)

    return True


#
# print(count(1692))
# print("********************************************")
# print(count(11))
# print("********************************************")
# print(count(2))

f = open("A-large-practice.in","r")

num_cases = int(f.readline())
output = []
for i in range(0,num_cases):
    inp_num = int(f.readline())
    output.append(count(inp_num))

f.close()

f = open("A-large-practice.out","w")
ctr = 1
for x in output:
    f.write("Case #"+str(ctr)+": " + x+ "\n")
    ctr += 1


f.close()






