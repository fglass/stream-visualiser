from abc import ABC, abstractmethod


class DataSource(ABC):

    def __init__(self):
        self.label = "Value"
        self.update_rate_ms = 50
        self.current_time = 0
        self.time = []  # Plotted on x axis

    @abstractmethod
    def update(self, plot):
        raise NotImplementedError
