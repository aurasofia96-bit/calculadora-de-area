#calculadora de area
salir=0
print('='*50)
print('Calculadora de área📐.')
print('='*50)
while salir!=2:
    print()
    print('Figuras:')
    print('1. Cuadrado')
    print('2. Rectángulo')
    print('3. Triángulo')
    print('4. Círculo')
    print()
    figura=int(input('Número de la figura: '))
    print()
    while figura<1 or figura>4:
        print('Error: Valor no valido, escriba un valor entre 1 y 4.')
        print()
        figura=int(input('Número de la figura: '))
    print()
    #solicitud de datos segun la forma
    if figura==1:
        lado=float(input('Medida de uno de los lados: '))
        print()
        print(f'El área es del cuadrado es: {lado**2}')
    elif figura==2:
        longitud=float(input('Longitud: '))
        ancho=float(input('Ancho: '))
        print()
        print(f'El área de el rectángulo es: {longitud*ancho}')
    elif figura==3:
        altura=float(input('Altura: '))
        base=float(input('Base: '))
        print()
        print(f'El área de el triángulo es: {(base*altura)/2}')
    else:
        import math
        pi=math.pi
        radio=float(input('Radio: '))
        print()
        print(f'El área del circulo es: {pi*(radio**2)}')
        print()
    print('-'*50)
    print()
    print('¿Quieres calcular otra área?')
    print('1. Si')
    print('2. No')
    print('')
    salir=int(input('Digita el número:'))
    while salir!=1 and salir!=2:
        print('Error: Valor no valido, escriba un valor entre 1 y 2.')
        print()
        salir=int(input('¿Quieres calcular otra área?'))
    print()
    print('+'*50)
    print()