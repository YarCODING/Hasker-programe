# this is main file :)
from design import*
import sys
import os
from PyQt5 import QtWidgets
import requests

dir = None
class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainwin()
        self.ui.setupUi(self)
        self.ui.result_lb.hide()

        self.ui.get_btn.clicked.connect(self.get_result)
        self.ui.papka_btn.clicked.connect(self.open_folder)
        self.ui.lineEdit.textChanged.connect(lambda: self.ui.result_lb.hide())


    def get_result(self):
        global dir
        link = self.ui.lineEdit.text()
        if link and dir:
            try:
                r = requests.get(link).text
                
                name = link.split('.')
                name = name[0]
                if name.__contains__('https://'):
                    name = name.replace('https://', '')
                elif name.__contains__('http://'):
                    name = name.replace('http://', '')
                name = name + '.html'

                filedir = dir + '/' + name
                with open(filedir, 'w+', encoding='utf-8') as f:
                    f.write(r)

                    self.ui.result_lb.show()
                    self.ui.result_lb.setText(f"Файл {name} збережено в {dir}")
                
            except:
                pass
    
    def open_folder(self):
        global dir
        dir = QtWidgets.QFileDialog.getExistingDirectory()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())