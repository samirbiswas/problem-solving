A, C, B, D = list(map(int, input().split()))
dif=((B*60)+D)-((A*60)+C)

if(dif <= 0):
    dif += 24*60

time = dif//60
minute = dif % 60
print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")
