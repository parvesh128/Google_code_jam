import sys
from math import  *

converter_memoize_map = {}
prime_memoize_map = {}
prime_memoize_map[2] = [True,1]
sieve = {}
sieve_max = 1
sieve_prime = []
def base_conversion(num,base):
    global converter_memoize_map
    if base < 2 or base > 10:
        return
    if not num:
        return
    if (num,base) in converter_memoize_map.keys():
        return converter_memoize_map[(num,base)]
    current_num = num
    converted_num = 0

    ctr = 0
    while current_num:
        mod=current_num % 2
        current_num = current_num // 2
        if mod == 1:
            converted_num = converted_num + int(pow(base,ctr))
        ctr = ctr + 1
    converter_memoize_map[(num,base)]=converted_num
    return converted_num


def buildsieve(num):
    global sieve
    global sieve_prime
    global  sieve_max


    for i in xrange(2,num+1):

        multiplier = 1
        if i in sieve.keys():
            continue
        while True:
            if (i*multiplier > num):
                break
            if multiplier == 1 :
                    sieve[i] = [True,1]
                    sieve_prime.append(i)
            else:
                sieve[i*multiplier] = [False,i]
            multiplier = multiplier + 1
    print sieve_prime
    sieve_max = num


def buildsieveincremental(start,end):
    global  sieve
    global  sieve_prime
    global  sieve_max
    if(len(sieve_prime) == 0):
        return buildsieve(end)

    sieve_prime_temp = sieve_prime
    for x in sieve_prime_temp:
        multiplier = (start+1)//x
        curr_num = multiplier*x
        while(curr_num <= end):
            if curr_num not in sieve.keys():
                sieve[curr_num] = [False,x]
            multiplier =  multiplier + 1
            curr_num = multiplier *x

    sieve_prime_temp = sieve

    for x in xrange(start,end+1):
        if x not in sieve_prime_temp.keys():
            sieve[x] = [True,1]
            sieve_prime.append(x)
    print sieve_prime
    sieve_max = end


def testwithdivisorsinsieve(num,end):
    for x in sieve_prime:
        if x > end:
            break
        if num % x == 0 :
            return [False,x]

    return [True,1]



def is_prime(num):
    global prime_memoize_map
    global  sieve
    global  sieve_max
    ret = [True,1]

    print ("Stage1")
    if(num < sieve_max):
        print ("Stage2a")
        return sieve[num]
    else:
        print ("Stage2b")
        sqrt_num = int(sqrt(num))
        print("sqrt: " + str(sqrt_num))
        if sqrt_num <= sieve_max:
            print ("Stage2ba")
            return testwithdivisorsinsieve(num,sqrt_num)
        else :
            print ("Stage2bb")
            buildsieveincremental(sieve_max+1,sqrt_num)
            return testwithdivisorsinsieve(num,sqrt_num)
        #check for the prime numbers as divisors in sieve
        #If not found there as well , then try to build sieve between
        #sieve_max and sqrt(num) and check for divisors then.


    # if num in prime_memoize_map.keys():
    #     return prime_memoize_map[num]

    # for i in prime_memoize_map.keys():
    #     if num % i == 0:
    #         ret = [False,i]
    #         prime_memoize_map[num] = ret
    #         return ret
    #
    # num_sqrt = int(sqrt(num))
    # print ("Num: " + str(num) + "Range to be checked for prime: " + str(num_sqrt))
    #
    # if num % 2 == 0:
    #     ret = [False,2]
    #     prime_memoize_map[num] = ret
    #     return ret
    #
    # for i in xrange(3,num_sqrt+1,2):
    #
    #     if num%i == 0:
    #         ret = [False,i]
    #         prime_memoize_map[i] = [True,1]
    #         break
    #     else:
    #         ret = [True,1]
    # prime_memoize_map[num]=ret
    # return  ret

def generate_jamcoin(numbits,numjamcoins,f):
    jamcoin = [None]*numbits
    jamcoin[0] = 1
    jamcoin[numbits-1]= 1
    prime_map = {}
    current_num_jamcoins = 0
    for i in xrange(2,11):
        prime_map[i] = [0,True]
    #print prime_map #DEBUG
    jamcoin_map = {}
    clamp_inner_bits_max = int(pow(2,numbits))
    clamp_inner_bits_min = int(pow(2,numbits-1)) + 1

    print (str(clamp_inner_bits_max) + " " + str(clamp_inner_bits_min))

    for x in xrange(clamp_inner_bits_min,clamp_inner_bits_max,2):
        if current_num_jamcoins >= numjamcoins:
            break
        print ("Stage 0")

        is_all_bases_not_prime = True
        for y in prime_map.keys():
            print ("Stage 1")
            temp = base_conversion(x,y)
            print ("Stage 2")
            is_base_prime = is_prime(temp)
            print ("Stage 3")
            if(is_all_bases_not_prime):
                prime_map[y] = [temp, is_base_prime[0],is_base_prime[1]]
                is_all_bases_not_prime = is_all_bases_not_prime and not is_base_prime[0]
            else:
                break

        if is_all_bases_not_prime :
            print(str(current_num_jamcoins)+ " jamcoin found\n")
            div_list = []
            for k in prime_map.keys():
                div_list.append(prime_map[k][2])
            jamcoin_map[str(bin(x)[2:])] = div_list
            current_num_jamcoins += 1


    for x in jamcoin_map.keys():
         fo.write(x+" "+str(" ".join(str(y) for y in jamcoin_map[x]))+"\n")





f = open("C-large-practice.in","r")
fo = open("C-large-practice.out","w")
num_cases = int(f.readline())

for i in xrange(1,num_cases+1):
    fo.write("Case #"+str(i)+":\n")
    numbits,numjamcoins = f.readline().split(" ")
    numbits = int(numbits)
    numjamcoins = int(numjamcoins)
    generate_jamcoin(numbits,numjamcoins,fo)

f.close()
fo.close()

# buildsieveincremental(15,20)
# buildsieveincremental(21,35)
# buildsieveincremental(35,1000)
# buildsieveincremental(1000,10000)
# buildsieveincremental(10001,100000)
# print is_prime(9997)
# print("**************************")
#
# print is_prime(19001)
#
#
# print("**************************")
#
# print is_prime(18997)




