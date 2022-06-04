import os
import sys

import PySide6
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice, QBarCategoryAxis, QValueAxis, QBarSet, \
    QBarSeries
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtCore import Qt
import numpy as np
import pandas as pd


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5饼图")

        # 显示位置
        self.setGeometry(100, 100, 800, 600)
        self.create_piechart()
        self.show()

    def create_piechart(self):
        # 创建QPieSeries对象，它用来存放饼图的数据
        self.resize(800, 600)
        # 随机找出 4 笔 7 天的温度变化
        df = pd.DataFrame(np.random.randint(20, high=35, size=(4, 2)), columns=["提交及时性","自我提交率"], index=["0:00-06:00","06:00-12:00","12:00-18:00","18:00-24:00"])
        print(df)
        # 画出4 周的温度变化折线图
        cols = list(df.columns)
        # valuesArray = list(df.values)
        series = QBarSeries()
        for i in range(len(cols)):
            setTemp = QBarSet(cols[i])
            setTemp.append(list(df.iloc[:, i]))
            series.append(setTemp)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Weather (day of the week)")

        chart.setAnimationOptions(QChart.SeriesAnimations)
        daysofweek = list(df.index)

        axisY = QValueAxis()
        axisY.applyNiceNumbers()
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(daysofweek)
        chart.addAxis(self.axis_x, Qt.AlignBottom)
        series.attachAxis(self.axis_x)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartView = QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chartView)

        series.doubleClicked.connect(self.bar_double_clicked)

    def bar_double_clicked(self, index, barset):
        print(barset.label(), barset.at(index), self.axis_x.categories()[index])


if __name__ == "__main__":
    dirname = os.path.dirname(PySide6.__file__)
    plugin_path = os.path.join(dirname, 'plugins', 'platforms')
    print(plugin_path)
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
