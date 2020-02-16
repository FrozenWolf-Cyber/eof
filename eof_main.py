#INPUT_USER
years_of_data = int(input("ENTER NUMBER OF YEARS"))
print()
number_of_crops = int(input("NUMBER OF CROPS"))
print()

Ps_i = []
Pf_i = []
S_r = []
c = []

for j in range(number_of_crops):
    temp1 = []
    temp2 = []
    for i in range(years_of_data):

        temp1.append(float(input("ENTER "+str(i+1)+"st YEAR'S SUCESS PRICE OF CROP "+str(j+1))))
        print(" ")

    for i in range(years_of_data):
        temp2.append(float(input("ENTER "+str(i+1)+"st YEAR'S FAILURE PRICE OF CROP "+str(j+1))))
        print(" ")

    Ps_i.append(temp1)
    Pf_i.append(temp2)



for i in range(number_of_crops):
    for j in range(years_of_data):
        temp = []
        temp_ = []
        temp.append(float(input("ENTER "+str(j+1)+"st YEAR'S " +str(i+1) +"st SUCCESS RATE OF CROP "+str(i+1))))
        print(" ")
        temp_.append(float(input("ENTER "+str(j+1)+"st YEAR'S " +str(i+1) +"st  MINIMUM PRICE CONSTANT OF CROP "+str(i+1))))
    S_r.append(temp)
    c.append(temp_)


S_r_avg = []
for i in S_r:
    temp = 0
    for j in i:
        temp = temp + (j/len(i))
    S_r_avg.append(temp)

c_avg = []
for i in c:
    temp = 0
    for j in i:
        temp = temp + (j/len(i))
    c_avg.append(temp)

E_d = float(input("ENTER ELASTICITY OF DEMAND"))

E_s = float(input("ENTER ELASTICITY OF SUPPLY"))

a = float(input("ENTER MAXIMUM QUANTITY SOLD AT NEGLIGIBLE PRICE"))

P_min = float(input("ENTER PRICE BELOW WHICH QUANTITY SUPPLIED IS 0 "))

n_sw = int(input("ENTER NUMBER OF SKILLED WORKERS REQUIRED"))

n_uw = int(input("ENTER NUMBER OF UNSKILLED WORKERS REQUIRED"))

c_sw = int(input("ENTER CHARGE OF EACH SKILLED WORKER"))

c_uw = int(input("ENTER CHARGE OF EACH UNSKILLED WORKER"))

c_rm = float(input("ENTER COST OF RAW MATERIALS INCLUDING SEEDS AND FERTILIZERS BUT NOT MACHINERY"))

#CALCULATION
c_p = c_rm + (n_sw*c_sw) + (n_uw*c_uw)




p_s = []

for i in Ps_i:
    avg = 0.0
    for j in i:
        avg = avg + (j/len(i))
    p_s.append(avg)

p_f = []

for i in Pf_i:
    avg = 0.0
    for j in i:
        avg = avg + (j/len(i))
    p_f.append(avg)

p_star = []

for i in range(number_of_crops):

    temp_result = (p_s[i]*S_r_avg[i]) + (p_f[i]*(100.00 - S_r_avg[i]))
    p_star.append(temp_result)

Q_star = []
for i in range(number_of_crops):
    temp_result = 0.0
    temp_result = c_avg[i]/(1-E_s)
    Q_star.append(temp_result)

production_info = []

for i in range(number_of_crops):
    if (Q_star[i]<0):
        print("Recheck Crop " +str(i+1)+" value or please do not grow this crop")
        print("------------------------")
        continue
    temp_result = float((Q_star[i])**((1+abs(E_d/E_s))**2))
    production_info.append(temp_result)

for i in production_info:
    print(production_info)
    print("--------RATIO-------")
    print(production_info[i]/min(production_info)+":")
    # print(Q_star)
