import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, \
    elevar_um_numero_pelo_outro, calcular_area_do_quadrado, calcular_area_do_retangulo, calcular_area_do_triangulo, \
    calcular_area_do_circulo


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

def testar_subtrair_dois_numeros():
    num1 = 7
    num2 = 5
    resultado_esperado = 2
    resultado_atual = subtrair_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_multiplicar_dois_numero():
    num1 = 10
    num2 = 5
    resultado_esperado = 50
    resultado_atual = multiplicar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_dividir_dois_numeros():
    num1 = 100
    num2 = 5
    resultado_esperado = 20
    resultado_atual = dividir_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_elevar_um_numero_pelo_outro():
    num1 = 4
    num2 = 3
    resultado_esperado = 64
    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_quadrado():
    num1 = 6
    num2 = 2
    resultado_esperado = 36
    resutado_atual = calcular_area_do_quadrado(num1, num2)
    assert resutado_atual == resultado_esperado

def testar_calcular_area_do_retangulo():
    num1 = 8
    num2 = 9
    resultado_esperado = 72
    resultado_atual = calcular_area_do_retangulo(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_triangulo():
    num1 = 4
    num2 = 6
    resultado_esperado = 12
    resultado_atual = calcular_area_do_triangulo(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_triangulo():
    num1 = 8
    resultado_esperado = 200.96
    resultado_atual = calcular_area_do_circulo(num1)
    assert resultado_atual == resultado_esperado




