'''
n = int(input('digite a tabuada: '))

for x in range(1, 11):
#for y in range(1,11):
    print('%d x %d = %d '% (x, n, x*n))

print()

n = 0
'''



ano = 1970
arquivo = open('senhas.txt', 'w')
while ano <= 2016:

    mes = 1
    while mes <= 12:
        dia = 1
        while dia <= 31:
            if dia < 10 and mes < 10:

                arquivo.write("0%d0%d%d\n" % (dia, mes, ano))
            elif dia > 10 and mes < 10:
                arquivo.write("%d0%d%d\n" % (dia, mes, ano))
            elif dia > 10 and mes > 10:
                arquivo.write("%d%d%d\n" % (dia, mes, ano))
            dia += 1
        mes += 1
    ano += 1
arquivo.close()
