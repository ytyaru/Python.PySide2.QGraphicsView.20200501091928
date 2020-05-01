#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PySide2 import QtCore, QtGui, QtWidgets 
 
class GraphicView(QtWidgets.QGraphicsView):
    def __init__(self):
        QtWidgets.QGraphicsView.__init__(self)
        self.setWindowTitle("QGraphicsView")
        scene = QtWidgets.QGraphicsScene(self)
        scene.setSceneRect(0, 0, 160, 120)
        self.setScene(scene)
        line = QtCore.QLineF(10,10,100,100)
        node = QtWidgets.QGraphicsLineItem(line)
        scene.addItem(node)
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = GraphicView()
    widget.show()
    sys.exit(app.exec_())

