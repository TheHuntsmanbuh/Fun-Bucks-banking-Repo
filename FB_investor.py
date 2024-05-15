import os
import random
from random import randint
import sys
import pyqtgraph as pg
import threading
import traceback, sys
#pyqt6 imports fr
import time
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import * 
from PyQt6.QtCore import *
 
from PyQt6.QtWidgets import *
prev = 0
ulmt = 50000
llmt = 0.0001 




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        global prev
        global pen
        # fbstocks vs time dynamic plot
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        self.plot_graph.setBackground("black")
        pen = pg.mkPen(color=(0, 255, 0))
        self.plot_graph.setTitle("Fun-Stocks", color="g", size="20pt")
        styles = {"color": "green", "font-size": "18px"}
        self.plot_graph.setLabel("left", "value$", **styles)
        self.plot_graph.setLabel("bottom", "seconds", **styles)
        self.plot_graph.addLegend()
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.setYRange(0, 100)
        self.time = list(range(100))
        
        self.fbval = [0 for _ in range(100)]
        # Get a line reference
        self.line = self.plot_graph.plot(
            self.time,
            self.fbval,
            name="fbvalue",
            pen=pen,
            symbol="o",
            symbolSize=4,
            symbolBrush="b",

        )
        # Add a timer to simulate new stock value
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        global ulmt
        global llmt
        global prev
        global pen
        self.time = self.time[1:]
        self.time.append(self.time[-1] + 1)
        self.fbval = self.fbval[1:]
        self.fbval.append(prev + randint(-10, 10))
        if self.time[1] > self.time[-1]:
            pen = pg.mkPen(color=(255, 0, 0))
            print("dingle")
        elif self.time[1] < self.time[-1]:
            pen = pg.mkPen(color=(0, 255, 0))
            print("dingle")
        prev = 0
        prev = prev + self.fbval[-1]
        prev = self.clamp(prev, llmt, ulmt)
        self.line.setData(self.time, self.fbval)
    def clamp(self, n, min, max):
        if n < min: 
            return min
        elif n > max: 
            return max
        else: 
            return n

app = QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()