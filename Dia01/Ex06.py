# Faça um programa que receba um número em segundos, converta esse número para horas, minuto e segundos. 
# Exemplos Entrada: 556 Saída: 0:9:16 Entrada: 140153 Saída: 38:55:53

#%%
segundos = int(input('Digite o valor:'))
minutos = int(segundos / 60)
horas = int(minutos / 60)
segundos = (segundos % 60)

print(f'{horas}:{minutos}:{segundos}')



# %%
