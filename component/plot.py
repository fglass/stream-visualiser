import random
import pyqtgraph as pg
from data.data_source import DataSource

COLOURS = ["#8be9fd", "#50fa7b", "#ffb86c", "#ff79c6", "#bd93f9", "#ff5555", "#f1fa8c"]


class Plot(pg.PlotItem):

    def __init__(self, data_source: DataSource):
        super().__init__()
        self.hideButtons()
        self.setLabel("left", data_source.label)
        self.setLabel("bottom", "Time", units="s")

        self.setLimits(xMin=0)
        self.showGrid(y=True)
        self.setYRange(-1, 1)

        pen = pg.mkPen(color=random.choice(COLOURS))
        self._plot = self.plot(pen=pen)

        self.timer = pg.QtCore.QTimer()
        self.timer.setInterval(data_source.update_rate_ms)
        self.timer.timeout.connect(lambda: data_source.update(self._plot))
        self.timer.start()

    def auto_range(self):
        self.enableAutoRange()
