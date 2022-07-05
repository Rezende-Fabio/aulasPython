#Teste 01
"""import random as rm

x = rm.randint(1, 20)
print(x)"""""

#Teste 02
"""import time as ti
from datetime import date

data_de_hoje = date.today()
print(data_de_hoje)

data_de_hoje02 = date.today().strftimecc
print(data_de_hoje02)

data_hoje_c = data_de_hoje.strftime("%d/%m/%y")
print(data_hoje_c)"""

#Teste 03
"""from datetime import date

data_de_hoje = date.today()
data_hoje_c = data_de_hoje.strftime("%d/%m/%y")

dia = int(input("DIA: "))
mes = int(input("MÊS: "))
meuNiver = date(date.today().year, mes, dia)

if meuNiver < data_de_hoje:
    meuNiver = meuNiver .replace(year= date.today().year + 1)

print(meuNiver)

datahoje = date.today()
datahojec = datahoje.strftime("%d/%m/%Y")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
meuniver = date(date.today().year, mes, dia)

if meuniver < datahoje:
    meuniver = meuniver.replace(year = date.today().year + 1)
dias = abs(meuniver - datahoje)

if dias.days == 0:
    print("Parabéns")
print(f'Faltam {dias.days} dias para seu aniversário.')"""

#Teste 04
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

# example data
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)

num_bins = 50

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(x, num_bins, density=True)

# add a 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()
