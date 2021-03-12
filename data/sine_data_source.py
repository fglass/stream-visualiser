import numpy as np
from pyqtgraph.graphicsItems import PlotDataItem
from .data_source import DataSource

UPDATE_RATE_MS = 10


class SineDataSource(DataSource):

    def __init__(self):
        super().__init__()
        self.label = "Amplitude"
        self.update_rate_ms = UPDATE_RATE_MS

    def update(self, plot: PlotDataItem):
        self.time.append(self.current_time)
        y = np.sin(self.time)
        plot.setData(self.time, y)
        self.current_time += UPDATE_RATE_MS / 1000
