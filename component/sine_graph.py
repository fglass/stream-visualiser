import random

import numpy as np
import pyqtgraph as pg

UPDATE_RATE_MS = 10
COLOURS = ["#8be9fd", "#50fa7b", "#ffb86c", "#ff79c6", "#bd93f9", "#ff5555", "#f1fa8c"]


class SineGraph(pg.PlotWidget):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.hideButtons()
        self.setLabel("left", "Amplitude")
        self.setLabel("bottom", "Time", units="s")

        self.setLimits(xMin=0)
        self.setYRange(-1, 1)
        self.showGrid(y=True)

        self.x = []
        self.time = 0
        pen = pg.mkPen(color=random.choice(COLOURS))
        self.plot = self.plot(pen=pen)

        self.timer = pg.QtCore.QTimer()
        self.timer.setInterval(UPDATE_RATE_MS)
        self.timer.timeout.connect(self._update)
        self.timer.start()

    def _update(self):
        self.x.append(self.time)
        y = np.sin(self.x)
        self.plot.setData(self.x, y)
        self.time += UPDATE_RATE_MS / 1000

    def auto_range(self):
        self.enableAutoRange()
