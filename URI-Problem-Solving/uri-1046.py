A, B = map(int, input().split())

if A > B:
    time = (B+24) - A
    print(f'O JOGO DUROU {time} HORA(S)')
elif B > A:
    time = (B - A)
    print(f'O JOGO DUROU {time} HORA(S)')
elif A == B:
    time = 24
    print(f'O JOGO DUROU {time} HORA(S)')
