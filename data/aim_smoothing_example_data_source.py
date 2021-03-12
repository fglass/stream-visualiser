import numpy as np
from pyqtgraph.graphicsItems import PlotDataItem
from .data_source import DataSource

UPDATE_RATE_MS = 10


class AimSmoothingExampleDataSource(DataSource):

    MAX_VELOCITY_DURATION = 450
    NO_SMOOTHING_DATA = [0] * 75 + [1] * MAX_VELOCITY_DURATION + [0] * 10000
    SMOOTHING_DATA = [0] * 75 + np.arange(0, 1, 0.01).tolist() + [1] * (MAX_VELOCITY_DURATION - 100) + [0] * 10000

    def __init__(self, smoothing: bool = True):
        super().__init__()
        self.label = "Rotation Velocity"
        self.update_rate_ms = UPDATE_RATE_MS
        self.data = self.SMOOTHING_DATA if smoothing else self.NO_SMOOTHING_DATA

    def update(self, plot: PlotDataItem):
        self.time.append(self.current_time)
        y = self.data[:len(self.time)]
        plot.setData(self.time, y)
        self.current_time += UPDATE_RATE_MS / 1000
