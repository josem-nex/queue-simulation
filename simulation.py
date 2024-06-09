import math
import random
from simpy import Environment, Resource


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
    def __init__(self, env: Environment, parameters: dict):
        self.parameters = parameters
        Resource.__init__(self, env, capacity=parameters.get('operators', 3))
        self.env = env
        self._results = []

    @property
    def results(self):
        return self._results

    # Generamos las llegadas de los clientes al sistema (llamadas)
    def client_arrivals(self):
        i = 1

        while True:
            # La llegada de los clientes sigue una distribucion exponencial de media 3 minutos
            client_arrival = generar_exponencial(self.parameters.get('arrival_mean', 3))
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
        # Guardamos los datos de la llamada, tiempo de llamada y duracion
        # En caso de que la llamada falle la duracion es -1
        call_data = [self.env.now, -1] 

        # Verificar si hay alguna operadora libre
        if call_center.count < call_center.capacity:   
            with call_center.request() as request:
                yield request
                # Las llamadas tienen una duracion con distribucion exponencial de media 6 minutos
                duration = generar_exponencial(call_center.parameters.get('duration_mean', 6))
                yield self.env.timeout(duration)

                call_center.results.append(tuple([call_data[0], duration]))
        # La llamada se pierde si no hay operadora libre
        else:
           call_center.results.append(tuple(call_data))

def simulate_call_center(parameters: dict) -> list[tuple[int, int]]:
   env = Environment()
   call_center = CallCenter(env, parameters)
   env.process(call_center.client_arrivals())
   env.run(parameters.get('time', 180)) 

   return call_center.results
