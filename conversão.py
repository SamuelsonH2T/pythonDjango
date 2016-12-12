
'''
Conversão de 	para 	Fórmula
Grau Celsius Grau Fahrenheit      --> 	°F = °C × 1,8 + 32
Grau Fahrenheit Grau Celsius      -->	°C = (°F − 32) / 1,8
Grau Celsius 	kelvin 	          -->    K = °C + 273,15
Kelvin 	Grau Celsius 	          -->   °C = K − 273,15
Grau Celsius 	Rankine 	      -->   °R = (°C + 273,15) × 1,8
Rankine 	Grau celsius 	      -->   °C = (°R ÷ 1,8) – 273,15
'''


def Choice():
    print('1- Grau Celsius para Grau Fahrenheit')
    print('2- Grau Fahrenheit para Grau Celsius')
    print('3- Grau Celsius para kelvin')
    print('4- kelvin para Grau Celsius ')
    print('5- Grau Celsius para Rankine ')
    print('6- Rankine para Grau Celsius ')

    print()

    choice = int(input('Escolha uma opção de conversão: '))
    while choice == 0:
        print('Escolha um numero diferente de', choice)
        choice = int(input('Escolha uma opção de conversão: '))

    if choice == 1:
        C = int(input('Digite o valor para ser convertido :'))
        F = C * 1.8 + 32
        print('O valor convertido é', F)

    elif choice == 2:

        F = int(input('Digite o valor para ser convertido :'))
        C = (F - 32)/1.8
        print('O valor convertido é', C)
    elif choice == 3:
        C = int(input('Digite o valor para ser convertido :'))
        K = C + 273.15
        print('O valor convertido é', K)

    elif choice == 4:
        K = int(input('Digite o valor para ser convertido :'))
        C = K - 273.15
        print('O valor convertido é', C)

    elif choice == 5:
        C = int(input('Digite o valor para ser convertido :'))
        R = (C + 273.15) * 1.8
        print('O valor convertido é', R)

    elif choice == 6:
        R = int(input('Digite o valor para ser convertido :'))
        C = (R / 1.8) - 273.15
        print('O valor convertido é', C)


    else:
        print()
        print('Escolha inválida, tente outra vez.')
        print()
        Choice()


Choice()

