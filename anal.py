import numpy as np


class Analizer:
    def __init__(self, results: list[tuple[int, int]], employees) -> None:
        self.results = results
        self.calls = len(results)
        self.lost_calls = len([call for call in results if call[1] == -1])
        self.successful_calls = len([call for call in results if call[1] != -1])
        self.average_call_duration = np.mean([call[1] for call in results if call[1] != -1])
        self.max_call_duration = np.max([call[1] for call in results if call[1] != -1])
        self.min_call_duration = np.min([call[1] for call in results if call[1] != -1])
        self.total_time = results[-1][0]
        self.lost_money = self.lost_calls * 210 * 0.6
        self.employees = employees
        self.employees_cost =  employees * 8 * 24
    
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
        Employees cost: {self.employees_cost}
        '''

