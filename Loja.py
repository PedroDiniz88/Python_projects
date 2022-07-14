# Elabore um algoritmo que leia os valores de entrada de um caixa
# O algoritmo deverá informar:
# 1. O caixa total da loja.
# 2. O valor da compra média efetuada.
# 3. Quantidade de compras acima de 100 reais.

ncad = 0
vcompra = 0
mediac = 0
x = 0
Qcad = 0
cmc = 0
mediac1 = 0

Qcad = int(input('Digite o número de  clientes que compraram na loja hoje: '))


for x in range(Qcad):
    vcompra = int(input("Digite o valor da compra: "))
    mediac1 = mediac1 + vcompra
    if (vcompra > 100):
        cmc = cmc + 1
mediac2 = mediac1/Qcad
print('Caixa total: ',mediac1)
print('Media de compras: ',mediac2)
print('Quantidade de compras acima de 100 reais: ',cmc)