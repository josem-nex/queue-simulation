import random
import simpy
import math
# variables
semilla = 10
num_peluqueros = 1
tiempo_corte_min = 15
tiempo_corte_max = 30
t_llegadas =20
tot_clientes = 5
clientes_atendidos = 0
te = 0.0 # tiempo de espera total
dt = 0.0 # duracion de servicio
fin = 0.0 # minuto en el que finaliza
# procedimientos

def cortar (cliente):
    global dt #Para poder acceder a la variable dt declarada anteriormente
    R = random.random() # Obtiene un numero aleatorio y lo guarda en R
    tiempo = tiempo_corte_max - tiempo_corte_min  
    tiempo_corte = tiempo_corte_min + (tiempo*R) # Distribucion uniforme
    yield env.timeout(tiempo_corte) # deja correr el tiempo n minutos
    print("Corte listo a %s en %.2f minutos" % (cliente,tiempo_corte))
    dt = tiempo_corte # Acumula los tiempos de uso de la i
    
def cliente (env, name, personal):
    global te #Para poder acceder a la variable te declarada anteriormente
    global fin #Para poder acceder a la variable fin declarada anteriormente
    global clientes_atendidos #Para poder acceder a la variable clientes_atendidos declarada anteriormente
    llega = env.now # Guarda el minuto de llegada del cliente
    print ("%s llego a la barberia en %.2f." % (name, llega))
    if personal.count < personal.capacity:
        with personal.request() as request: # Espera su turno
            yield request # Obtiene turno
            pasa = env.now # Guarda el minuto cuado comienza a ser atendido
            espera = pasa - llega # Calcula el tiempo que espero
            te = te + espera # Acumula los tiempos de espera
            print ("%s pasa con el peluquero en %.2f minutos" % (name, espera))
            yield env.process(cortar(name)) # Invoca al procedimiento cortar
            deja = env.now #Guarda el minuto en que termina el proceso cortar
            print ("%s deja la barberia en %.2f" % (name, deja))
            clientes_atendidos += 1
            fin = deja # Conserva globalmente el ultimo minuto de la simulacion
    else:
        print ("%s se va porque la barberia esta ocupada." % name)
        
def principal (env, personal):
    llegada = 0
    i = 0
    for i in range(tot_clientes): # Para n clientes
        R = random.random()
        llegada = -t_llegadas * math.log(R) # Distribucion exponencial
        yield env.timeout(llegada)  # Deja transcurrir un tiempo entre uno y otro
        i += 1
        env.process(cliente(env, 'Cliente %d' % i, personal))
        
# Programa principal
print ("Barberia XYZ")
random.seed (semilla)  # Cualquier valor
env = simpy.Environment() # Crea el objeto entorno de simulacion
personal = simpy.Resource(env, num_peluqueros) #Crea los recursos (peluqueros)
env.process(principal(env, personal)) #Invoca el proceso princial
env.run() #Inicia la simulacion

print ("\nSimulacion terminada en %.2f minutos" % fin)
print ("Tiempo medio de espera %.2f" % (te/tot_clientes))
print ("Clientes atendidos", clientes_atendidos)
print ("Minutos de uso de la barberia: %.2f" % dt)




class Cars:
    def __init__(self, env, gas_station, name):
        self.env = env
        self.gas_station = gas_station
        self.name = name
    def refuel(self):
        yield self.env.timeout(5)
    def action(self):
        with self.gas_station.request() as req:
            print(f"{self.name} solicita gasolina en el momento: {self.env.now}")
            yield req
            print(f"{self.name} entra a la gasolinera en {self.env.now} y en la gasolinera numero: {self.gas_station.count}")
            yield self.env.process(self.refuel())
            print(f"{self.name} sale de la gasolinera en {self.env.now}")

def car_generator(env, gas_station):
    i=0
    while True:
        t = random.randrange(1,10)
        yield env.timeout(t)
        c = Cars(env, gas_station,  name=f"Car {i}")
        env.process(c.action())
        i += 1

env = simpy.Environment()
gas_station = simpy.Resource(env, capacity=2)
env.process(car_generator(env, gas_station))

env.run(until=100)