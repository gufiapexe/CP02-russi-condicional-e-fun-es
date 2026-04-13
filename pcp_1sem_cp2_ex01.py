codigo_do_estado = int(input("Digite o código do estado de origem da carga: "))
peso_da_carga = int(input("Digite o peso da carga em toneladas: "))
codigo_da_carga = int(input("Digite o codigo da carga: "))
conversao = peso_da_carga * 1000


if codigo_da_carga >= 10 and codigo_da_carga <= 20:
   calculo = 100 * conversao
elif codigo_da_carga >= 21 and codigo_da_carga <= 30:
   calculo = 250 * conversao
else:
   calculo = 400 * conversao

if codigo_do_estado == 1:
   valor_imposto = 1.35 * calculo
elif codigo_do_estado == 2:
   valor_imposto = 1.25 * calculo
elif codigo_do_estado == 3:
   valor_imposto = 1.15 * calculo
elif codigo_do_estado == 4:
   valor_imposto = 1.05 * calculo
else:
   valor_imposto = calculo

print(f"Valor total transportado pelo caminhão é: {valor_imposto}")

