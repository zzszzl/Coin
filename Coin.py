print("我们总共投币五组，输入的初始值是: \n P(A_H)=0.60    P(B_H)=0.50 ")

print("第一次投币有5个H（正面朝上），5个T（反面朝上）")
print("第二次投币有9个H（正面朝上），1个T（反面朝上）")
print("第三次投币有8个H（正面朝上），2个T（反面朝上）")
print("第四次投币有4个H（正面朝上），6个T（反面朝上）")
print("第五次投币有7个H（正面朝上），3个T（反面朝上）")



P_A_H = 0.60
P_B_H = 0.50
def CoinCal(m,n):
    ret=[]
    x = pow(P_A_H, m) * pow((1 - P_A_H), n)
    y = pow(P_B_H, m) * pow((1 - P_B_H), n)
    p_a = x / (x + y)
    p_b = y / (x + y)

    coina_h = p_a * m
    coina_t = p_a * n

    coinb_h = p_b * m
    coinb_t = p_b * n
    print("%0.1f  %8.1f   %9.1f  %9.1f" % (coina_h, coina_t, coinb_h, coinb_t))
    ret.append(coina_h)
    ret.append(coina_t)
    ret.append(coinb_h)
    ret.append(coinb_t)
    return ret

def CountCoin():
    ret2=[]
    tem1 = CoinCal(5,5)
    tem2 = CoinCal(9,1)
    tem3 = CoinCal(8,2)
    tem4 = CoinCal(4,6)
    tem5 = CoinCal(7,3)
    print("*********************************************")
    print("COUNT:")
    counta_h = tem1[0] + tem2[0] + tem3[0] + tem4[0] + tem5[0]
    counta_t = tem1[1] + tem2[1] + tem3[1] + tem4[1] + tem5[1]
    countb_h = tem1[2] + tem2[2] + tem3[2] + tem4[2] + tem5[2]
    countb_t = tem1[3] + tem2[3] + tem3[3] + tem4[3] + tem5[3]
    print("%0.1f  %8.1f   %9.1f  %9.1f" % (counta_h, counta_t, countb_h, countb_t))
    P_A_H = counta_h/(counta_h+counta_t)
    P_B_H = countb_h/(countb_h+countb_t)
    ret2.append(P_A_H)
    ret2.append(P_B_H)
    print("P_A_H= %0.2f          P_B_H=%0.2f  " %(P_A_H, P_B_H))
    return ret2

count=0
while (count <=10):
    print("第 %d 次输出结果：" %count)
    print("*********************************************")
    print("   CoinA                   CoinB     ")
    print("H         T            H          T")
    print("*********************************************")
    item = CountCoin()
    P_A_H =item[0]
    P_B_H=item[1]
    print("*********************************************")
    print("\n")
    count += 1