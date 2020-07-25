from PyQt5.QtWidgets import QToolBar, QToolButton


class Toolbar(QToolBar):

    def __init__(self):
        super().__init__()
        self.home_button = QToolButton()
        self.home_button.setText("🏠")
        self._set_font_size(self.home_button)
        self.addWidget(self.home_button)

        self.add_button = QToolButton()
        self.add_button.setText("📄")
        self._set_font_size(self.add_button)
        self.addWidget(self.add_button)

        self.theme_toggle = QToolButton()
        self.theme_toggle.setText("💡")
        self._set_font_size(self.theme_toggle)
        self.theme_toggle.clicked.connect(self._change_theme_toggle_icon)
        self.addWidget(self.theme_toggle)

    @staticmethod
    def _set_font_size(button: QToolButton):
        font = button.font()
        font.setPointSize(14)
        button.setFont(font)

    def _change_theme_toggle_icon(self):
        self.theme_toggle.setText("🔦" if self.theme_toggle.text() == "💡" else "💡")
