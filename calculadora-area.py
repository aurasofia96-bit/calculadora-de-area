#calculadora de area
print('='*23)
print('Calculadora de área📐.')
print('='*23)
print()
print('1. Cuadrado')
print('2. Rectángulo')
print('3. Triángulo')
print('4. Círculo')
print()
figura=int(input('Figura: '))
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
elif figura==4:
    import math
    pi=math.pi
    radio=float(input('Radio: '))
    print()
    print(f'El área del circulo es: {pi*(radio**2)}')
else:
    print('Error: Valor no valido')
enter=input('Presiona enter para salir.')