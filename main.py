import pyqtgraph as pg
import sys
from component.sine_plot import SinePlot
from component.toolbar import Toolbar
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QMainWindow

BACKGROUND_COLOUR = "#323232"
DARK_STYLESHEET = "QMainWindow { background-color: %s } QToolBar { background-color: #232323 }" % BACKGROUND_COLOUR
LIGHT_STYLESHEET = "QMainWindow { background-color: white } QToolBar { background-color: #d7d7d7 } "


class Window(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setWindowTitle("Stream Visualiser")
        self.setStyleSheet(DARK_STYLESHEET)
        self._dark_mode = True
        self.resize(1280, 720)

        self._frame = QWidget()
        self.setCentralWidget(self._frame)
        self._layout = QGridLayout()
        self._frame.setLayout(self._layout)

        toolbar = Toolbar()
        self._layout.addWidget(toolbar)

        pg.setConfigOption("antialias", True)  # Smooths line edges but reduces performance
        pg.setConfigOption("background", BACKGROUND_COLOUR)

        self._canvas = pg.GraphicsLayoutWidget()
        self._layout.addWidget(self._canvas)

        self._plots = []
        self._add_plot()

        toolbar.home_button.clicked.connect(self._auto_range)
        toolbar.add_button.clicked.connect(self._add_plot)
        toolbar.theme_toggle.clicked.connect(self._change_theme)

    def _add_plot(self):
        new_plot = SinePlot()
        self._canvas.addItem(new_plot, row=len(self._plots), col=0)
        self._plots.append(new_plot)

    def _auto_range(self):
        [plot.auto_range() for plot in self._plots]

    def _change_theme(self):
        self._dark_mode = not self._dark_mode

        if self._dark_mode:
            self.setStyleSheet(DARK_STYLESHEET)
            self._canvas.setBackground(BACKGROUND_COLOUR)
        else:
            self.setStyleSheet(LIGHT_STYLESHEET)
            self._canvas.setBackground("w")


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
