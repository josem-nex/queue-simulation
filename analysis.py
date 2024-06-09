import numpy as np

class Analizer:
    """ PARAMETERS_ANALIZE = {
    'time': 180, 
    'operators': PARAMETERS['operators'],
    'operator_costxhour': 24,
    'profitxcall': 210,
    'porcentage_lost_calls': 0.6,
    }    """
    def __init__(self, results: list[tuple[int, int]], parameters: dict) -> None:
        self.results = results
        self.calls = len(results)
        self.lost_calls = len([call for call in results if call[1] == -1])
        self.successful_calls = len([call for call in results if call[1] != -1])
        self.average_call_duration = np.mean([call[1] for call in results if call[1] != -1])
        self.max_call_duration = np.max([call[1] for call in results if call[1] != -1])
        self.min_call_duration = np.min([call[1] for call in results if call[1] != -1])
        self.total_time = results[-1][0]
        self.lost_money = self.lost_calls * parameters['profitxcall'] * parameters['porcentage_lost_calls']
        self.employees = parameters['operators']
        self.employees_cost =  parameters['operators'] * parameters['operator_costxhour'] *8
    
    def __str__(self) -> str:
        return f'''
        Calls: {self.calls}
        Successful calls: {self.successful_calls}
        Lost calls: {self.lost_calls}
        Average call duration: {self.average_call_duration}
        Max call duration: {self.max_call_duration}
        Min call duration: {self.min_call_duration}
        Total time: {self.total_time}
        Lost money: {self.lost_money}
        Employees: {self.employees}
        Employees cost: {self.employees_cost}
        '''

