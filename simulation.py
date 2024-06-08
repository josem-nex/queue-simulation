import math
import random
from simpy import Environment, Resource


def generar_poisson(media):
    """
    Función para generar un número aleatorio a partir de una distribución de Poisson
    Formula: P(k) = (e^-λ * λ^k) / k!
    """
    k = 0
    p = math.exp(-media)
    acumulado = p
    r = random.random()
    while acumulado < r:
      k += 1
      p = p * media / k
      acumulado += p
    return k

def generar_dist_acumulado(dist, media, n):
    """
    Función para generar n números aleatorios a partir de una distribución de Poisson
    """
    return [dist(media) for _ in range(n)]


def generar_exponencial(media):
  """
  Función para generar un número aleatorio a partir de una distribución exponencial
  """
  u = random.random()
  return -media * math.log(1 - u)


'''
    Clase que representa el centro de llamadas, que posee una capacidad de atencion simultanea
    Representada como child de la clase Resource de simpy
'''
class CallCenter(Resource):
    def __init__(self, env: Environment, capacity: int):
        Resource.__init__(self, env, capacity=capacity)
        self.env = env

    # Generamos las llegadas de los clientes al sistema (llamadas)
    def client_arrivals(self):
        i = 1

        while True:
            # La llegada de los clientes sigue una distribucion exponencial de media 3 minutos
            client_arrival = generar_exponencial(3)
            yield self.env.timeout(client_arrival)
            
            client = Client(f"Cliente {i}", self.env)
            self.env.process(client.call(self))
            i += 1

'''
    Clase que representa nuestro agente, el cliente, que es el encargado de realizar las llamadas
'''
class Client:
    def __init__(self, name: str,  env: Environment) -> None:
        self.env = env
        self.name = name

    def call(self, call_center: CallCenter):
        print(f"{self.name} solicita una llamada en {self.env.now}")
        # Verificar si hay alguna operadora libre
        if call_center.count < call_center.capacity:   
            with call_center.request() as request:
                yield request
                print(f"{self.name} se comunica con el operador {call_center.count} en {self.env.now}")
                # Las llamadas tienen una duracion con distribucion exponencial de media 6 minutos
                duration = generar_exponencial(6)
                yield self.env.timeout(duration)
                print(f"{self.name} finaliza la llamada en {self.env.now}")
        # La llamada se pierde si no hay operadora libre
        else:
           print(f"Se pierde la llamada de {self.name}")

def simulate_call_center(time: int, operators: int):
   env = Environment()
   call_center = CallCenter(env, operators)
   env.process(call_center.client_arrivals())
   env.run(time) 
