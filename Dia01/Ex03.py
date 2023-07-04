# Faça um programa que receba o raio de uma circunferência em centímetros. 
# Retorne para o usuário qual é a área e perímetro desta circunferência no seguinte formato.

#%% 

# Importamos a biblioteca math
# 'raio' recebe  o input recebido do usuário e convertido para float
# 'area' recebe o valor de raio elevado ao quadrado e multiplicado pela constante pi 
# 'perimetro' recebe o valor de 2 multiplicado por pi e pelo raio
# Imprimimos o resultado 

import math 

raio = float(input('digite o raio da circunferência:'))
area = (raio ** 2) * math.pi
perimetro = 2 * math.pi * raio
print(f'Área:{area}')    
print(f'Perímeto:15{perimetro}')

# %%
