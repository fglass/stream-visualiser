import pyqtgraph as pg
import sys
from component.sine_graph import SineGraph
from component.toolbar import Toolbar
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QGridLayout, QWidget, QFrame

BACKGROUND_COLOUR = "#323232"


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setWindowTitle("Stream Visualiser")
        self.resize(1280, 720)
        self._dark_mode = True

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        toolbar = Toolbar()
        self.layout.addWidget(toolbar)

        pg.setConfigOption("antialias", True)  # Smooths line edges but reduces performance
        pg.setConfigOption("background", BACKGROUND_COLOUR)
        self._graph = SineGraph()
        self.layout.addWidget(self._graph)

        toolbar.home_button.clicked.connect(self._graph.auto_range)
        toolbar.theme_toggle.clicked.connect(self._change_theme)

    def _change_theme(self):
        self._dark_mode = not self._dark_mode

        if self._dark_mode:
            self.setStyleSheet(f"background-color: {BACKGROUND_COLOUR}")
            self._graph.setBackground(BACKGROUND_COLOUR)
        else:
            self.setStyleSheet("background-color: white")
            self._graph.setBackground("w")


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
