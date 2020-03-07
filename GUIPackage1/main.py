#**************************************************************
#**************************************************************
# # First application using PySide2 and QtQuick/QML
# import sys
# import os
# from PySide2 import QtWidgets
# from PySide2.QtQuick import QQuickView
# from PySide2.QtCore import QUrl

# app = QtWidgets.QApplication([])
# view = QQuickView()
# # url = QUrl("/home/cybernetor066/Desktop/Software-IT-Web-Dev/GIT-Repos/python-desktopApps-devCentre/GUIPackage1/view.qml")
# # Or you resolve the file path like this,
# current_dir = os.path.dirname(__file__)
# file_path = os.path.join(current_dir, "view.qml")
# url = QUrl(file_path)
# view.setSource(url)
# view.setResizeMode(QQuickView.SizeRootObjectToView)
# view.show()
# app.exec_()



# #**************************************************************
# #**************************************************************
# # A simple button tutorial(handling signals and slots)
# import sys, os
# from PySide2 import QtWidgets
# # from PySide2.QtWidgets import QApplication, QPushButton
# from PySide2.QtCore import Slot

# @Slot()
# def say_hello():
#     print("Button clicked!, Hello!!")

# # create the Qt Application
# app = QtWidgets.QApplication(sys.argv)

# # create the button and connect the button to the function
# button = QtWidgets.QPushButton("Click me")
# button.clicked.connect(say_hello)

# # show the button and run the main Qt loop
# button.show()
# app.exec_()



# #**************************************************************
# #**************************************************************
# # Dialog application
# import sys
# from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

# class Form(QDialog):
#     def __init__(self, parent=None):
#         super(Form, self).__init__(parent)
#         self.setWindowTitle("My Form")
        
#         # create widgets
#         self.edit = QLineEdit("Write your name here..")
#         self.button = QPushButton("Show greetings")

#         # Now we creat a layout to add and organise the widgets
#         layout = QVBoxLayout()
#         layout.addWidget(self.edit)
#         layout.addWidget(self.button)

#         # set the dialog layout
#         self.setLayout(layout)

#         # add button signal to greeting slot
#         self.button.clicked.connect(self.say_hello)


#     def say_hello(self):
#         print("Button clicked!, {}".format(self.edit.text()))



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     form = Form()
#     form.show()
#     sys.exit(app.exec_())




# #**************************************************************
# #**************************************************************
# # The use of UI files.
# import sys, os
# from PySide2.QtUiTools import QUiLoader
# from PySide2.QtWidgets import QApplication, QMainWindow
# from PySide2.QtCore import QFile
# from ui_mainwindow import Ui_MainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     current_dir = os.path.dirname(__file__)
#     file_path = os.path.join(current_dir, "mainwindow.ui")

#     # retrieve the file and open it for reading
#     ui_file = QFile(file_path)
#     ui_file.open(QFile.ReadOnly)

#     # load the ui file and show it
#     loader = QUiLoader()
#     window = loader.load(ui_file)
#     ui_file.close()
#     window.show()

#     sys.exit(app.exec_())





# #*************************************************************
# #*************************************************************
# # Data visualisation tool
# # Chapter1(reading data from a csv)
# import sys, os
# import argparse             # To intercept and parse input from the command line.
# import pandas as pd

# def read_data(fname):
#     return pd.read_csv(fname)


# if __name__ == "__main__":
#     options = argparse.ArgumentParser()
#     options.add_argument("-f", "--file", type=str, required=True)
#     args = options.parse_args()
#     data = read_data(args.file)
#     print(data)


# # Chapter2(filtering data)
# import argparse
# import pandas as pd
# from PySide2.QtCore import QDateTime, QTimeZone

# def transform_date(utc, timezone=None):
#     utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
#     new_date = QDateTime().fromString(utc, utc_fmt)
#     if timezone:
#         new_date.setTimeZone(timezone)
#     return new_date

# def read_data(fname):
#     # read the csv content
#     df = pd.read_csv(fname)

#     # remove wrong magnitudes
#     df = df.drop(df[df.mag < 0].index)
#     magnitudes = df["mag"]

#     # my local timezone
#     timezone = QTimeZone(b"Europe/Berlin")

#     # get the timestamp transfered to our timezone
#     times = df["time"].apply(lambda x: transform_date(x, timezone))

#     return times, magnitudes

# if __name__ == "__main__":
#     options = argparse.ArgumentParser()
#     options.add_argument("-f", "--file", type=str, required=True)
#     args = options.parse_args()
#     data = read_data(args.file)
#     print(data)


# # Chapter3(create an empty QMainWindow)
# import sys, os
# from PySide2.QtUiTools import QUiLoader
# from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar
# from PySide2.QtCore import QFile, Slot, qApp
# from PySide2.QtGui import QKeySequence
# from ui_mainwindow1 import Ui_MainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         # Or
#         # super(MainWindow, self).__init__()

#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.setWindowTitle("Earthqakes information")

#         # menu
#         self.menu = self.menuBar()
#         self.menu.setNativeMenuBar(False)
#         self.file_menu = self.menu.addMenu("File")

#         # exit QAction for the exit situated under the 'File' menu
#         exit_action = QAction("Exit", self)
#         exit_action.setShortcut(QKeySequence.Quit)
#         exit_action.triggered.connect(self.close)
#         self.file_menu.addAction(exit_action)

#         # status bar
#         self.status = self.statusBar()
#         self.status.showMessage("Data is loaded and plotted")

#         # window dimensions
#         geometry = qApp.desktop().availableGeometry(self)
#         self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())




# # Chapter4(Add a QTableView)
# # Implementing the model for the QTableView, allows you to:- set the headers, -manipulate the formats of 
# # the cell values, -set style properties like text alignment -and set color properties for the cell or its
# # content.
# from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex
# from PySide2.QtGui import QColor

# class CustomTableModel(QAbstractTableModel):
#     def __init__(self, data=None):
#         QAbstractTableModel.__init__(self)
#         # super(CustomTableModel, self).__init__()
#         self.load_data(data)

#     def load_data(self, data):
#         self.input_dates = data[0].values
#         self.input_magnitudes = data[1].values

#         self.column_count = 2
#         self.row_count = len(self.input_magnitudes)

#     def rowCount(self, parent=QModelIndex()):
#         return self.row_count

#     def columnCount(self, parent=QModelIndex()):
#         return self.column_count


#     def headerData(self, section, orientation, role):
#         if role != Qt.DisplayRole:
#             return None
#         if orientation == Qt.Horizontal:
#             return ("Date", "Magnitude")[section]
#         else:
#             return "{}".format(section)
            
    
#     def data(self, index, role=Qt.DisplayRole):
#         column = index.column()
#         row = index.row()

#         if role == Qt.DisplayRole:
#             if column == 0:
#                 raw_date = self.input_dates[row]
#                 date = "{}".format(raw_date.toPython())
#                 return date[:-3]
#             elif column == 1:
#                 return "{:.2f}".format(self.input_magnitudes[row])
#         elif role == Qt.BackgroundRole:
#             return QColor(Qt.white)
#         elif role == Qt.TextAlignmentRole:
#             return Qt.AlignRight

#         return None

# # Now create a QWidget that has a QTableView and connect it to your CustomTableModel
# from PySide2.QtWidgets import (
#     QHBoxLayout, QHeaderView, QSizePolicy,
#     QTableView, QWidget
# )

# class Widget(QWidget):
#     def __init__(self, data):
#         super(Widget, self).__init__()

#         # getting the model
#         self.model = CustomTableModel(data)

#         # creating the QTableView
#         self.table_view = QTableView()
#         self.table_view.setModel(self.model)

#         # QTableView headers
#         self.horizontal_header = self.table_view.horizontalHeader()
#         self.vertical_header = self.table_view.verticalHeader()
        
#         self.horizontal_header.setSectionResizeModel(QHeaderView.ResizeToContents)
#         self.vertical_header.setSectionResizeModel(QHeaderView.ResizeToContents)
#         self.horizontal_header.setStretchLastSection(True)

#         # QWidget layout
#         self.main_layout = QHBoxLayout()
#         size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

#         # left layout
#         size.setHorizontalStretch(1)
#         self.table_view.setSizePolicy(size)
#         self.main_layout.addWidget(self.table_view)

#         # set the layout to the QWidget
#         self.setLayout(self.main_layout)

# Then last but not the least is to effect this Widget() class into our MainWindow() class
# and also showing it in our main()


# # Chapter5(Add a chart view)
# from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex, QDateTime
# from PySide2.QtGui import QColor, QPainter
# from PySide2.QtCharts import QtCharts

# class CustomTableModel(QAbstractTableModel):
#     def __init__(self, data=None):
#         QAbstractTableModel.__init__(self)
#         # super(CustomTableModel, self).__init__()
#         self.load_data(data)

#     def load_data(self, data):
#         self.input_dates = data[0].values
#         self.input_magnitudes = data[1].values

#         self.column_count = 2
#         self.row_count = len(self.input_magnitudes)

#     def rowCount(self, parent=QModelIndex()):
#         return self.row_count

#     def columnCount(self, parent=QModelIndex()):
#         return self.column_count


#     def headerData(self, section, orientation, role):
#         if role != Qt.DisplayRole:
#             return None
#         if orientation == Qt.Horizontal:
#             return ("Date", "Magnitude")[section]
#         else:
#             return "{}".format(section)
            
    
#     def data(self, index, role=Qt.DisplayRole):
#         column = index.column()
#         row = index.row()

#         if role == Qt.DisplayRole:
#             if column == 0:
#                 raw_date = self.input_dates[row]
#                 date = "{}".format(raw_date.toPython())
#                 return date[:-3]
#             elif column == 1:
#                 return "{:.2f}".format(self.input_magnitudes[row])
#         elif role == Qt.BackgroundRole:
#             return QColor(Qt.white)
#         elif role == Qt.TextAlignmentRole:
#             return Qt.AlignRight

#         return None

# # Now create a QWidget that has a QTableView and connect it to your CustomTableModel
# from PySide2.QtWidgets import (
#     QHBoxLayout, QHeaderView, QSizePolicy,
#     QTableView, QWidget
# )

# class Widget(QWidget):
#     def __init__(self, data):
#         super(Widget, self).__init__()

#         # getting the model
#         self.model = CustomTableModel(data)

#         # creating the QTableView
#         self.table_view = QTableView()
#         self.table_view.setModel(self.model)

#         # QTableView headers
#         self.horizontal_header = self.table_view.horizontalHeader()
#         self.vertical_header = self.table_view.verticalHeader()        
#         self.horizontal_header.setSectionResizeModel(QHeaderView.ResizeToContents)
#         self.vertical_header.setSectionResizeModel(QHeaderView.ResizeToContents)
#         self.horizontal_header.setStretchLastSection(True)

#         # creating QChart
#         self.chart = QtCharts.QChart()
#         self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

#         # creating QChartView
#         self.chart_view = QtCharts.QChartView(self.chart)
#         self.chart_view.setRenderHint(QPainter.Antialiasing)

#         # QWidget layout
#         self.main_layout = QHBoxLayout()
#         size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

#         # left layout
#         # place the Qableview towards the left handside
#         size.setHorizontalStretch(1)
#         self.table_view.setSizePolicy(size)
#         self.main_layout.addWidget(self.table_view)

#         # right layout
#         # place the QChartView towards the right handside
#         size.setHorizontalStretch(4)
#         self.chart_view.setSizePolicy(size)
#         self.main_layout.addWidget(self.chart_view)

#         # set the layout to the QWidget
#         self.setLayout(self.main_layout)







# # Chapter6(plot the data in the chartview) And Overall codes combined
# # for this you need to go over our data and include the data on a QLineSeries and after adding the data to the
# # series, you can modify the axis to properly display the QDateTime on the X-axis and the magnitude values on
# # the Y-axis
# import sys, os
# import argparse
# import pandas as pd

# from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex, QDateTime, QTimeZone
# from PySide2.QtGui import QColor, QPainter
# from PySide2.QtCharts import QtCharts

# from PySide2.QtUiTools import QUiLoader
# from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar
# from PySide2.QtCore import QFile, Slot, qApp
# from PySide2.QtGui import QKeySequence
# from ui_mainwindow1 import Ui_MainWindow

# # filtering the data
# def transform_date(utc, timezone=None):
#     utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
#     new_date = QDateTime().fromString(utc, utc_fmt)
#     if timezone:
#         new_date.setTimeZone(timezone)
#     return new_date

# def read_data(fname):
#     # read the csv content
#     df = pd.read_csv(fname)

#     # remove wrong magnitudes
#     df = df.drop(df[df.mag < 0].index)
#     magnitudes = df["mag"]

#     # my local timezone
#     timezone = QTimeZone(b"Europe/Berlin")

#     # get the timestamp transfered to our timezone
#     times = df["time"].apply(lambda x: transform_date(x, timezone))

#     return times, magnitudes


# # creating the mainwindow
# class MainWindow(QMainWindow):
#     def __init__(self, widget):
#         QMainWindow.__init__(self)
#         # Or
#         # super(MainWindow, self).__init__()

#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.setWindowTitle("Earthqakes information")
#         self.setCentralWidget(widget)

#         # menu
#         self.menu = self.menuBar()
#         self.menu.setNativeMenuBar(False)
#         self.file_menu = self.menu.addMenu("File")

#         # exit QAction for the exit situated under the 'File' menu
#         exit_action = QAction("Exit", self)
#         exit_action.setShortcut(QKeySequence.Quit)
#         exit_action.triggered.connect(self.close)
#         self.file_menu.addAction(exit_action)

#         # status bar
#         self.status = self.statusBar()
#         self.status.showMessage("Data is loaded and plotted")

#         # window dimensions
#         geometry = qApp.desktop().availableGeometry(self)
#         self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)


# # creating the QTable model
# class CustomTableModel(QAbstractTableModel):
#     def __init__(self, data=None):
#         # QAbstractTableModel.__init__(self)
#         # or
#         super(CustomTableModel, self).__init__()
#         self.load_data(data)

#     def load_data(self, data):
#         self.input_dates = data[0].values
#         self.input_magnitudes = data[1].values

#         self.column_count = 2
#         self.row_count = len(self.input_magnitudes)

#     def rowCount(self, parent=QModelIndex()):
#         return self.row_count

#     def columnCount(self, parent=QModelIndex()):
#         return self.column_count


#     def headerData(self, section, orientation, role):
#         if role != Qt.DisplayRole:
#             return None
#         if orientation == Qt.Horizontal:
#             return ("Date", "Magnitude")[section]
#         else:
#             return "{}".format(section)
            
    
#     def data(self, index, role=Qt.DisplayRole):
#         column = index.column()
#         row = index.row()

#         if role == Qt.DisplayRole:
#             if column == 0:
#                 raw_date = self.input_dates[row]
#                 date = "{}".format(raw_date.toPython())
#                 return date[:-3]
#             elif column == 1:
#                 return "{:.2f}".format(self.input_magnitudes[row])
#         elif role == Qt.BackgroundRole:
#             return QColor(Qt.white)
#         elif role == Qt.TextAlignmentRole:
#             return Qt.AlignRight

#         return None



# # Now create a QWidget that has a QTableView and connect it to our CustomTableModel
# from PySide2.QtWidgets import (
#     QHBoxLayout, QHeaderView, QSizePolicy,
#     QTableView, QWidget
# )

# class Widget(QWidget):
#     def __init__(self, data):
#         QWidget.__init__(self)
#         # or
#         # super(Widget, self).__init__()

#         # getting the model
#         self.model = CustomTableModel(data)

#         # creating the QTableView
#         self.table_view = QTableView()
#         self.table_view.setModel(self.model)

#         # QTableView headers
#         self.horizontal_header = self.table_view.horizontalHeader()
#         self.vertical_header = self.table_view.verticalHeader()        
#         self.horizontal_header.setSectionResizeMode(QHeaderView.ResizeToContents)
#         self.vertical_header.setSectionResizeMode(QHeaderView.ResizeToContents)
#         self.horizontal_header.setStretchLastSection(True)

#         # creating QChart
#         self.chart = QtCharts.QChart()
#         self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
#         self.add_series("Magnitude (Column 1)", [0, 1])

#         # creating QChartView
#         self.chart_view = QtCharts.QChartView(self.chart)
#         self.chart_view.setRenderHint(QPainter.Antialiasing)

#         # QWidget layout
#         self.main_layout = QHBoxLayout()
#         size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

#         # left layout
#         # place the Qableview towards the left handside
#         size.setHorizontalStretch(1)
#         self.table_view.setSizePolicy(size)
#         self.main_layout.addWidget(self.table_view)

#         # right layout
#         # place the QChartView towards the right handside
#         size.setHorizontalStretch(4)
#         self.chart_view.setSizePolicy(size)
#         self.main_layout.addWidget(self.chart_view)

#         # set the layout to the QWidget
#         self.setLayout(self.main_layout)

#     def add_series(self, name, columns):
#         # create QLineSeries
#         self.series = QtCharts.QLineSeries()
#         self.series.setName(name)

#         # filling the QLineSeries
#         for i in range(self.model.rowCount()):
#             # getting the data
#             t = self.model.index(i, 0).data()
#             date_fmt = "yyyy-MM-dd HH:mm:ss.zzz"

#             x = QDateTime().fromString(t, date_fmt).toSecsSinceEpoch()
#             y = float(self.model.index(i, 1).data())

#             if x > 0 and y > 0:
#                 self.series.append(x, y)
        
#         self.chart.addSeries(self.series)

#         # setting the X-axis
#         self.axis_x = QtCharts.QDateTimeAxis()
#         self.axis_x.setTickCount(10)
#         self.axis_x.setFormat("dd.MM (h:mm)")
#         self.axis_x.setTitleText("Date")
#         self.chart.addAxis(self.axis_x, Qt.AlignBottom)
#         self.series.attachAxis(self.axis_x)

#         # setting the Y-axis
#         self.axis_y = QtCharts.QValueAxis()
#         self.axis_y.setTickCount(10)
#         self.axis_y.setLabelFormat("%.2f")
#         self.axis_y.setTitleText("Magnitude")
#         self.chart.addAxis(self.axis_y, Qt.AlignLeft)
#         self.series.attachAxis(self.axis_y)

#         # getting the color from QChart to use it on the QTableView
#         self.model.color = "{}".format(self.series.pen().color().name())


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     options = argparse.ArgumentParser()
#     options.add_argument("-F", "--file", type=str, required=True)
#     args = options.parse_args()
#     data = read_data(args.file)
#     widget = Widget(data)
#     window = MainWindow(widget)
#     window.show()
#     sys.exit(app.exec_())



# # #*************************************************************
# # #*************************************************************
# # Expenses tool tutorial
# ################################################################################
# #############################################################################
# ##
# ## Copyright (C) 2020 The Qt Company Ltd.
# ## Contact: http://www.qt.io/licensing/
# ##
# ## This file is part of the Qt for Python examples of the Qt Toolkit.
# ##
# ## $QT_BEGIN_LICENSE:BSD$
# ## You may use this file under the terms of the BSD license as follows:
# ##
# ## "Redistribution and use in source and binary forms, with or without
# ## modification, are permitted provided that the following conditions are
# ## met:
# ##   * Redistributions of source code must retain the above copyright
# ##     notice, this list of conditions and the following disclaimer.
# ##   * Redistributions in binary form must reproduce the above copyright
# ##     notice, this list of conditions and the following disclaimer in
# ##     the documentation and/or other materials provided with the
# ##     distribution.
# ##   * Neither the name of The Qt Company Ltd nor the names of its
# ##     contributors may be used to endorse or promote products derived
# ##     from this software without specific prior written permission.
# ##
# ##
# ## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# ## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# ## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# ## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# ## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# ## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# ## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# ## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# ## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# ## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
# ##
# ## $QT_END_LICENSE$
# ##
# #############################################################################

# import sys, os
# from PySide2.QtWidgets import (
#     QMainWindow, QApplication, QMenuBar, QAction, QTableWidgetItem, QLabel, QVBoxLayout,
#     QWidget, QTableWidget, QHeaderView, QHBoxLayout, QLineEdit, QPushButton
# )
# from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex, QTimeZone, Slot
# from PySide2.QtGui import QPainter
# from PySide2.QtCharts import QtCharts

# class MainWindow(QMainWindow):
#     def __init__(self, widget):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle("Expenses tutorial")

#         # create a menu bar
#         self.menu = self.menuBar()
#         self.menu.setNativeMenuBar(False)
#         self.file_menu = self.menu.addMenu("File")

#         # add a file menu with the following options
#         # -Exit
#         exit_action = QAction("Exit", self)
#         exit_action.setShortcut("Ctrl+Q")
#         exit_action.triggered.connect(self.exit_app)
#         self.file_menu.addAction(exit_action)
#         self.setCentralWidget(widget)       # set the central widget.


#     # first signal/slot connection(element.signal_name.connect(slot_name))
#     # the exit option must be connected to a slot that triggers the application to exit
#     @Slot()
#     def exit_app(self, checked):
#         QApplication.quit()




# # create an empty central widget and data
# class Widget(QWidget):
#     def __init__(self):
#         super(Widget, self).__init__()

#         # initialise general row to zero position
#         self.items = 0

#         # example data
#         self._data = {
#             "Water": 24.5, "Electricity": 55.1, "Rent": 850.0,
#             "Supermarket": 230.4, "Internet": 29.99, "Bars": 21.85,
#             "Public transportation": 60.0, "Coffee": 22.45, "Restaurants": 120
#         }

#         # left handside layout
#         # ******************************************
#         self.table = QTableWidget()
#         self.table.setColumnCount(2)
#         self.table.setHorizontalHeaderLabels(["Description", "Price"])
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         # fill the example data on the table view
#         self.fill_table()



#         # right handside layout
#         # ******************************************

#         # initialise the edit modes
#         self.description = QLineEdit()
#         self.price = QLineEdit()

#         # chart view
#         self.chart_view = QtCharts.QChartView()
#         self.chart_view.setRenderHint(QPainter.Antialiasing)


#         # add element action
#         self.add = QPushButton("Add")
#         self.add.clicked.connect(self.add_element)

#         # clear action
#         self.clear = QPushButton("Clear")
#         self.clear.clicked.connect(self.clear_table)        

#         # quit application action
#         self.quit = QPushButton("Quit")
#         self.quit.clicked.connect(self.quit_application)

#         # plot action
#         self.plot = QPushButton("Plot")
#         self.plot.clicked.connect(self.plot_data)

#         # signals and slots for the verification
#         self.description.textChanged[str].connect(self.check_disable)
#         self.price.textChanged[str].connect(self.check_disable)

#         # disabling the 'Add' button.
#         self.add.setEnabled(False)

#         # continue with the right handside layout
#         self.right = QVBoxLayout()
#         self.right.setMargin(10)
#         self.right.addWidget(QLabel("Description"))
#         self.right.addWidget(self.description)
#         self.right.addWidget(QLabel("Price"))
#         self.right.addWidget(self.price)
#         self.right.addWidget(self.add)
#         self.right.addWidget(self.plot)
#         self.right.addWidget(self.chart_view)
#         self.right.addWidget(self.clear)
#         self.right.addWidget(self.quit)


#         # Setting the layout
#         # QWidget layout
#         # the QHBoxLayout() provides the container to place widgets horizontally
#         self.layout = QHBoxLayout()

#         # self.table_view.setSizePolicy(size)
#         self.layout.addWidget(self.table)
#         self.layout.addLayout(self.right)

#         # set the layout to the QWidget
#         self.setLayout(self.layout)



#     @Slot()
#     def add_element(self):
#         des = self.description.text()
#         price = self.price.text()

#         self.table.insertRow(self.items)
#         self.table.setItem(self.items, 0, QTableWidgetItem(des))
#         self.table.setItem(self.items, 1, QTableWidgetItem(price))

#         self.description.setText("")
#         self.price.setText("")


#     @Slot()
#     def check_disable(self, s):
#         if not self.description.text() or not self.price.text():
#             self.add.setEnabled(False)
#         else:
#             self.add.setEnabled(True)


#     @Slot()
#     def plot_data(self):
#         # get the information
#         series = QtCharts.QPieSeries()
#         for i in range(self.table.rowCount()):
#             text = self.table.item(i, 0).text()
#             number = float(self.table.item(i, 1).text())
#             series.append(text, number)

#         chart = QtCharts.QChart()
#         chart.addSeries(series)
#         chart.legend().setAlignment(Qt.AlignLeft)
#         self.chart_view.setChart(chart)


#     @Slot()
#     def clear_table(self):
#         self.table.setRowCount(0)
#         self.items = 0


#     @Slot()
#     def quit_application(self):
#         QApplication.quit()



#     def fill_table(self, data=None):
#         data = self._data if not data else data
#         for desc, price in data.items():
#             self.table.insertRow(self.items)
#             self.table.setItem(self.items, 0, QTableWidgetItem(desc))
#             self.table.setItem(self.items, 1, QTableWidgetItem(str(price)))

#             # increment general row position
#             self.items += 1




# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     widget = Widget()
#     # using QWidget as the central widget
#     window = MainWindow(widget)
#     window.resize(1000, 600)
#     window.show()
#     sys.exit(app.exec_())







# #*************************************************************
# #*************************************************************
# # QML application tutorial
# import os, sys
# import json
# from urllib import request
# from PySide2.QtQuick import QQuickView
# from PySide2.QtCore import QStringListModel, QUrl
# from PySide2.QtGui import QGuiApplication

# if __name__ == "__main__":
#     # get our data
#     url = "http://country.io/names.json"
#     response = request.urlopen(url)
#     data = json.loads(response.read().decode('utf-8'))

#     # format and sort the data
#     data_list = list(data.values())
#     data_list.sort()

#     # now set up the application window using QGuiApplication which manages the application-wide settings
#     app = QGuiApplication(sys.argv)
#     view = QQuickView()
#     view.setResizeMode(QQuickView.SizeRootObjectToView)

#     # expose the list to the qml code
#     my_model = QStringListModel()
#     my_model.setStringList(data_list)
#     view.rootContext().setContextProperty("myModel", my_model)

#     # load the view2.qml file to the QQuickView() and call show to display the application window
#     # load the qml file
#     current_dir = os.path.dirname(__file__)
#     file_path = os.path.join(current_dir, "view2.qml")
#     url = QUrl(file_path)
#     view.setSource(url)
#     # Or
#     # qml_file = os.path.join(os.path.dirname(__file__), "view2.qml")
#     # view.setSource(QUrl.fromLocalFile(os.path.abspath(qml_file)))

#     # show the window with an error handling capacity
#     if view.status() == QQuickView.Error:
#         sys.exit(-1)
#     view.show()

#     # finally execute the application to start the event loop and clean up
#     app.exec_()
#     del view











# #*************************************************************
# #*************************************************************
# # QML integration tutorial
# # This tutorial provides a quick walk-through of a python application that loads and interacts with 
# # a qml file.This tutorial will help us to understand how to use python as backend for certain signals
# # from the ui elements in the qml interface.

# #############################################################################
# ##
# ## Copyright (C) 2019 The Qt Company Ltd.
# ## Contact: http://www.qt.io/licensing/
# ##
# ## This file is part of the Qt for Python examples of the Qt Toolkit.
# ##
# ## $QT_BEGIN_LICENSE:BSD$
# ## You may use this file under the terms of the BSD license as follows:
# ##
# ## "Redistribution and use in source and binary forms, with or without
# ## modification, are permitted provided that the following conditions are
# ## met:
# ##   * Redistributions of source code must retain the above copyright
# ##     notice, this list of conditions and the following disclaimer.
# ##   * Redistributions in binary form must reproduce the above copyright
# ##     notice, this list of conditions and the following disclaimer in
# ##     the documentation and/or other materials provided with the
# ##     distribution.
# ##   * Neither the name of The Qt Company Ltd nor the names of its
# ##     contributors may be used to endorse or promote products derived
# ##     from this software without specific prior written permission.
# ##
# ##
# ## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# ## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# ## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# ## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# ## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# ## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# ## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# ## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# ## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# ## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# ## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
# ##
# ## $QT_END_LICENSE$
# ##
# #############################################################################
# import os, sys
# from PySide2.QtWidgets import QApplication
# from PySide2.QtCore import QObject, Slot, Qt
# from PySide2.QtGui import QGuiApplication
# from PySide2.QtQml import QQmlApplicationEngine
# from style_rc import *



# class Bridge(QObject):
    
#     @Slot(str, result=str)
#     def getColor(self, color_name):
#         if color_name.lower() == "red":
#             return "#ef9a9a"
#         elif color_name.lower() == "green":
#             return "#a5d6a7"
#         elif color_name.lower() == "blue":
#             return "#90caf9"
#         else:
#             return "white"
    

#     @Slot(float, result=int)
#     def getSize(self, s):
#         size = int(s*42)  # maximum font size
#         if size <= 0:
#             return 1
#         else:
#             return size

    
#     @Slot(str, result=bool)
#     def getItalic(self, s):
#         if s.lower() == "italic":
#             return True
#         else:
#             return False


#     @Slot(str, result=bool)
#     def getBold(self, s):
#         if s.lower() == "bold":
#             return True
#         else:
#             return False


#     @Slot(str, result=bool)
#     def getUnderline(self, s):
#         if s.lower() == "underline":
#             return True
#         else:
#             return False


#     @Slot()
#     def exitApp(self):
#         QGuiApplication.quit()
        

#     # Then go back to the qml file and connect the signals to the slots defined in this Bridge() class
#     # Generate an rc file running, pyside2-rcc style.qrc > style_rc.py 
#     # And finally import it from your main.py script.


# # now set up the application using QGuiApplication.
# if __name__ == '__main__':
#     app = QGuiApplication(sys.argv)
#     engine = QQmlApplicationEngine()

#     # Create the instance of the Python object
#     bridge = Bridge()

#     # Expose the Python object to QML
#     context = engine.rootContext()
#     context.setContextProperty("con", bridge)

#     # load the qml file
#     qmlFile = os.path.join(os.path.dirname(__file__), 'view3.qml')
#     engine.load(qmlFile)

#     if not engine.rootObjects():
#         sys.exit(-1)

#     sys.exit(app.exec_())










# *************************************************************
# *************************************************************
#  Data visualisation tool(Second version)
# #############################################################################

# #############################################################################
# #############################################################################
# # **
# # **
# # ** BEGIN_LICENSE: ALL$
# # **
# # ** Copyright (C) 2018 The Qt Company Ltd.
# # ** Contact: https://www.qt.io/licensing/
# # **
# # ** This file is part of Qt for Python.
# # **
# # ** $QT_BEGIN_LICENSE:LGPL$
# # ** Commercial License Usage
# # ** Licensees holding valid commercial Qt licenses may use this file in
# # ** accordance with the commercial license agreement provided with the
# # ** Software or, alternatively, in accordance with the terms contained in
# # ** a written agreement between you and The Qt Company. For licensing terms
# # ** and conditions see https://www.qt.io/terms-conditions. For further
# # ** information use the contact form at https://www.qt.io/contact-us.
# # **
# # ** GNU Lesser General Public License Usage
# # ** Alternatively, this file may be used under the terms of the GNU Lesser
# # ** General Public License version 3 as published by the Free Software
# # ** Foundation and appearing in the file LICENSE.LGPL3 included in the
# # ** packaging of this file. Please review the following information to
# # ** ensure the GNU Lesser General Public License version 3 requirements
# # ** will be met: https://www.gnu.org/licenses/lgpl-3.0.html.
# # **
# # ** GNU General Public License Usage
# # ** Alternatively, this file may be used under the terms of the GNU
# # ** General Public License version 2.0 or (at your option) the GNU General
# # ** Public license version 3 or any later version approved by the KDE Free
# # ** Qt Foundation. The licenses are as published by the Free Software
# # ** Foundation and appearing in the file LICENSE.GPL2 and LICENSE.GPL3
# # ** included in the packaging of this file. Please review the following
# # ** information to ensure the GNU General Public License requirements will
# # ** be met: https://www.gnu.org/licenses/gpl-2.0.html and
# # ** https://www.gnu.org/licenses/gpl-3.0.html.
# # **
# # ** $QT_END_LICENSE$
# # **
# #############################################################################
# #############################################################################

# #############################################################################
# #############################################################################
# **
# $PSF_BEGIN_LICENSE$
# **
# # PSF LICENSE AGREEMENT FOR PYTHON 3.7.0
# # 1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"), and
# #    the Individual or Organization ("Licensee") accessing and otherwise using Python
# #    3.7.0 software in source or binary form and its associated documentation.

# # 2. Subject to the terms and conditions of this License Agreement, PSF hereby
# #    grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
# #    analyze, test, perform and/or display publicly, prepare derivative works,
# #    distribute, and otherwise use Python 3.7.0 alone or in any derivative
# #    version, provided, however, that PSF's License Agreement and PSF's notice of
# #    copyright, i.e., "Copyright © 2001-2018 Python Software Foundation; All Rights
# #    Reserved" are retained in Python 3.7.0 alone or in any derivative version
# #    prepared by Licensee.

# # 3. In the event Licensee prepares a derivative work that is based on or
# #    incorporates Python 3.7.0 or any part thereof, and wants to make the
# #    derivative work available to others as provided herein, then Licensee hereby
# #    agrees to include in any such work a brief summary of the changes made to Python
# #    3.7.0.

# # 4. PSF is making Python 3.7.0 available to Licensee on an "AS IS" basis.
# #    PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY OF
# #    EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
# #    WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
# #    USE OF PYTHON 3.7.0 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

# # 5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 3.7.0
# #    FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
# #    MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 3.7.0, OR ANY DERIVATIVE
# #    THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

# # 6. This License Agreement will automatically terminate upon a material breach of
# #    its terms and conditions.

# # 7. Nothing in this License Agreement shall be deemed to create any relationship
# #    of agency, partnership, or joint venture between PSF and Licensee.  This License
# #    Agreement does not grant permission to use PSF trademarks or trade name in a
# #    trademark sense to endorse or promote products or services of Licensee, or any
# #    third party.

# # 8. By copying, installing or otherwise using Python 3.7.0, Licensee agrees
# #    to be bound by the terms and conditions of this License Agreement.
# **
# $PSF_END_LICENSE$
# **
# #############################################################################
# #############################################################################

# #############################################################################
# #############################################################################
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
# #############################################################################
# #############################################################################
# # **
# # ** END_LICENSE: ALL$
# # **
# #############################################################################
# #############################################################################
# Reforming a data visualisation tool to accept file intake from file select 
# dialog box, rather than parsing it from the command line.


# first lets perform a very simple data visualisation task
import sys, os
import pandas as pd
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar, QFileDialog
from PySide2.QtCore import QFile, Slot, qApp, QDateTime, QTimeZone
from PySide2.QtGui import QKeySequence

class MainWindow(QMainWindow):
    def __init__(self):
        # QMainWindow.__init__(self)
        # Or
        super(MainWindow, self).__init__()

        # set window title
        self.setWindowTitle("Earthqakes information")

        # menu
        self.menu = self.menuBar()
        self.menu.setNativeMenuBar(False)
        self.file_menu = self.menu.addMenu("File")

        # exit QAction for the exit situated under the 'File' menu
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exitApp)
        self.file_menu.addAction(exit_action)

        # insert file action
        addFile_action = QAction("Insert File", self)
        addFile_action.triggered.connect(self.inputFile)
        self.file_menu.addAction(addFile_action)


        # status bar
        self.status = self.statusBar()
        self.status.showMessage("Data is loaded and plotted")

        # window dimensions
        geometry = qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)

    def transform_date(self, utc, timezone=None):
        utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
        new_date = QDateTime().fromString(utc, utc_fmt)
        if timezone:
            new_date.setTimeZone(timezone)
        return new_date

    def read_data(self, fname):
        # read the csv content
        df = pd.read_csv(fname)

        # remove wrong magnitudes
        df = df.drop(df[df.mag < 0].index)
        magnitudes = df["mag"]

        # my local timezone
        timezone = QTimeZone(b"Europe/Berlin")

        # get the timestamp transfered to our timezone
        times = df["time"].apply(lambda x: self.transform_date(x, timezone))

        return times, magnitudes

    @Slot()
    def exitApp(self):
        QApplication.quit()

    @Slot()
    def inputFile(self):
        dialog = QFileDialog(self)
        # dialog.setFileMode(QFileDialog.AnyFile)
        # Or for a specific file type as as shown below
        dialog.setNameFilter(self.tr("CSV Files (*.csv)"))
        # dialog.setLabelText(QFileDialog.Accept, self.tr("Open document"))
        dialog.setViewMode(QFileDialog.Detail)
        # if dialog.exec_():
        #     fileName = dialog.selectedFiles()
        #     data = self.read_data(fileName)
        #     print(data)

        if dialog.exec_():
            fileName = dialog.selectedFiles()    # Note: A list is returned here.
            data = self.read_data(fileName[0])
            print(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())