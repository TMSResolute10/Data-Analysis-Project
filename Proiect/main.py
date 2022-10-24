import sys
from model import *
from PySide2 import *
from gui import *

app = QApplication(sys.argv)
main_frame = Frame()
main_frame.show()
sys.exit(app.exec_())
