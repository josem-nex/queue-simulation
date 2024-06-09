import numpy as np
import matplotlib.pyplot as plt
from analysis import Analizer


def s_data(analizers: list[Analizer]):
    calls = np.array([analizer.calls for analizer in analizers])
    successful_calls = np.array([analizer.successful_calls for analizer in analizers])
    lost_calls = np.array([analizer.lost_calls for analizer in analizers])
    lost_money = np.array([analizer.lost_money for analizer in analizers])
    average_call_duration = np.array([analizer.average_call_duration for analizer in analizers])
    max_call_duration = np.array([analizer.max_call_duration for analizer in analizers])
    min_call_duration = np.array([analizer.min_call_duration for analizer in analizers])
    total_time = np.array([analizer.total_time for analizer in analizers])
    profit = np.array([analizer.profit for analizer in analizers])
    return calls, successful_calls, lost_calls, average_call_duration, max_call_duration, min_call_duration, lost_money, total_time, profit

def print_means(calls, successful_calls, lost_calls, average_call_duration, max_call_duration, min_call_duration, lost_money, total_time, profit):
    print(f'''
    Calls: {np.mean(calls)}
    Successful calls: {np.mean(successful_calls)}
    Lost calls: {np.mean(lost_calls)}
    Average call duration: {np.mean(average_call_duration)}
    Max call duration: {np.mean(max_call_duration)}
    Min call duration: {np.mean(min_call_duration)}
    Lost money: {np.mean(lost_money)}
    Total time: {np.mean(total_time)}
    Profit: {np.mean(profit)}
    ''')

def analysis(data, name: str, do_print):
    media = np.mean(data)
    
    mediana = np.median(data)
    
    varianza = np.var(data)
    
    desviacion = np.std(data)
    
    minimo = np.min(data)
    
    maximo = np.max(data)
    
    stats = ['Media', 'Mediana', 'Varianza', 'Desviación estándar', 'Mínimo', 'Máximo']
    values = [media, mediana, varianza, desviacion, minimo, maximo]
    
    if do_print:
        print(f'''
        {name}
        Media: {media}
        Mediana: {mediana}
        Varianza: {varianza}
        Desviacion: {desviacion}
        Minimo: {minimo}
        Maximo: {maximo}
        ''')
         # Crea un gráfico de barras
        plt.bar(stats, values)

        # Añade un título y etiquetas a los ejes
        plt.title(name)
        plt.xlabel('Estadísticas')
        plt.ylabel('Valores')

        # Muestra el gráfico
        plt.show()

        # Crea un histograma
        plt.hist(data, bins=10, edgecolor='black')

        # Añade un título y etiquetas a los ejes
        plt.title('Distribución de los datos')
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')

        # Muestra el gráfico
        plt.show()
    
