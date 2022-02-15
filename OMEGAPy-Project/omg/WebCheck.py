from PyQt5 import QtWebEngineWidgets,QtWidgets
from PyQt5 import QtCore
import requests as req
import sys


class UI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        self.lo = layout
        self.setLayout(layout)
        self.Web = QtWebEngineWidgets.QWebEngineView()
    def Uri(self,Text:str):
        self.Web.setHtml(Text)
        self.lo.addWidget(self.Web)
        self.Web.show()
    def Url(self,url:str):
        self.Web.setUrl(QtCore.QUrl(url))
        self.lo.addWidget(self.Web)
        self.Web.show()
        
    


def Response(res:str):
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.Uri(res)
    window.show()
    sys.exit(app.exec_())

def Request(url:str):
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.Url(url)
    window.show()
    sys.exit(app.exec_())
