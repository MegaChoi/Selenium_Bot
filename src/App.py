import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
class MainWindow(qtw.QWidget):
    def __init__(self) :
        super().__init__()
        #title
        self.setWindowTitle("May dap v1.0")
        #layout
        # self.setLayout(qtw.QVBoxLayout())
        self.show()
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()