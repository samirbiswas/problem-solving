N1, N2, N3, N4 = map(float, input().split())

average = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print(f'Media: {average:.1f}')

if average >= 7.0:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado.")
elif average >= 5.0 and average <7:
    print("Aluno em exame.")
    N = float(input())
    print(f'Nota do exame: {N:.1f}')
    N = (N+average)/2
    if N >= 5.0:
        print("Aluno aprovado.")
        print(f'Media final: {N:.1f}')
    else:
        print(f'Media final: {N:.1f}')

