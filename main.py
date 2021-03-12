import pyqtgraph as pg
import sys
from component.plot import Plot
from component.toolbar import Toolbar
from data.aim_smoothing_example_data_source import AimSmoothingExampleDataSource
from data.sine_data_source import SineDataSource
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QMainWindow, QAction

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

        self._container = QWidget()
        self._layout = QGridLayout()
        self._container.setLayout(self._layout)
        self.setCentralWidget(self._container)

        toolbar = Toolbar()
        self._layout.addWidget(toolbar)

        pg.setConfigOption("antialias", True)  # Smooths line edges but reduces performance
        self._canvas = pg.GraphicsLayoutWidget()
        self._canvas.setBackground(BACKGROUND_COLOUR)
        self._layout.addWidget(self._canvas)

        self._plots = []

        toolbar.home_button.clicked.connect(self._auto_range)
        toolbar.add_button.menu().triggered.connect(self._add_plot)
        toolbar.theme_toggle.clicked.connect(self._change_theme)

    def _add_plot(self, action: QAction):
        data_source = SineDataSource() if action.text() == "Sine Wave" else AimSmoothingExampleDataSource()
        new_plot = Plot(data_source)
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
