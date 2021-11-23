import pytest

def somar_dois_numeros(num1,num2):
   return  num1 + num2

def subtrair_dois_numeros(num1,num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2


def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except:
        ZeroDivisionError
    return 'Não é possivel dividir por zero'


def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

def calcular_area_do_quadrado(num1, num2):
    return num1 ** num2

def calcular_area_do_retangulo(num1, num2):
    return num1 * num2

def calcular_area_do_triangulo(num1, num2):
    return num1 * num2 / 2

def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 2





if __name__ == '__main__':

    resultado = somar_dois_numeros(5,7)
    print(f'A soma é {resultado}')

    resultado = subtrair_dois_numeros(7,5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(10,5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(100,5)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(4,3)
    print(f'A exponenciação é {resultado}')

    resultado = calcular_area_do_quadrado(6,2)
    print(f' A Area do quadrado é {resultado}')

    resultado = calcular_area_do_retangulo(8,9)
    print(f' A Area do retangulo é {resultado}')

    resultado = calcular_area_do_triangulo(4,6)
    print(f' A Area do Triangulo é {resultado}')

    resultado = calcular_area_do_circulo(8)
    print(f' A Area do circulo é {resultado}')


    #Desgustador / Teste
'''
    def testar_somar_dois_numeros():
# - 1 Etapa: Configura / Prepara
#Dados / Valores
#Entrada / Input
    num1 = 5
    num2 = 7
#saida / output
    resultado_esperado = 12

# - 2 Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)
#- 3 Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado
'''




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
