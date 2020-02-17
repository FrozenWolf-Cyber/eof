input_num = int(input("enter num"))

prime_numbers = []


def check(value):
    factor = []
    for i in range(1,value+1):
        if(value%i==0):
            factor.append(i)

    if(len(factor)==2):
        prime_numbers.append(value)
        print(len(prime_numbers))
    
n = 1
while len(prime_numbers)<100:

    check(n)
    n = n+1


print(prime_numbers[:-1])



n = int(input("Number of values to be entered"))
sorted_list=[]
for i in range(n):
    sorted_list.append(int(input("enter number "+str(i+1)+" ",)))

output = []

for a in range(input_num):
    for b in range(input_num):
        for c in range(input_num):
            if ((a**2)+(b**2) == (c**2) and a+b+c == input_num):
                
                output.append([a,b,c])


print(output)


sum = 0
factor = []
for i in range(1,input_num+1):
    if input_num%i==0:
        factor.append(i)


for i in factor:
    if i%2==0:
        print(i)
        sum = sum+i

print(sum)

