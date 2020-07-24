import numpy as np
import pyqtgraph as pg
import sys
from PyQt5 import QtWidgets, QtCore

UPDATE_RATE_MS = 10


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        pg.setConfigOption("antialias", True)  # Smooths line edges but reduces performance
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")

        widget = pg.PlotWidget()
        widget.setTitle("Stream Visualiser", size="18pt")
        widget.setLabel("left", "Amplitude")
        widget.setLabel("bottom", "Time", units="s")

        widget.setLimits(xMin=0)
        widget.setYRange(-1, 1)
        widget.showGrid(y=True)
        self.setCentralWidget(widget)

        self.x = [0]
        self.time = 0
        pen = pg.mkPen(color=(255, 0, 0))
        self.plot = widget.plot(self.x, np.sin(self.x), pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(UPDATE_RATE_MS)
        self.timer.timeout.connect(self.update)
        self.timer.start()

    def update(self):
        self.time += UPDATE_RATE_MS / 1000
        self.x.append(self.time)
        y = np.sin(self.x)
        self.plot.setData(self.x, y)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.resize(1280, 720)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
