largura= float(input('Qual é a largura da parede? '))
altura= float(input('Qual é a altura da parede? '))
area= largura * altura

print(f'A dimensão da sua parede é {largura}x{altura} e sua área é {area}m²')

quant= area / 2

print(f'A quantidade necessária de tinta para pintar sua parede é {quant} litros')
