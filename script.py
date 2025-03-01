print('Verificar coordenadas')

def verificador(x,y):
    x = int(input('Digite o valor no eixo X'))
    y = int(input('Digite o valor no eixo Y'))

    if x >=0 and y >0:
        print('O ponto está no primeiro quadrante')
    elif x < 0 and y > 0:
        print('O ponto está no segundo quadrante')
    elif x < 0 and y < 0:
        print('O ponto está no terceiro quadrante')
    elif x > 0 and y < 0:
        print('O ponto está no quarto quadrante')
    else:
        print('O ponto é a origem')

verificador()