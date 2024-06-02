import math
llamadas_hora = 20
llamadas_resp_hora = 10

def tasa_llegada(t, lambd):
    return lambd*math.exp(-lambd*t)
def tasa_salida(t, mu):
    return mu*math.exp(-mu*t)

print(tasa_llegada(1, llamadas_hora))

