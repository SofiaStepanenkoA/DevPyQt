# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(474, 350)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 20, 461, 301))
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 71, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_2 = QSlider(self.verticalLayoutWidget)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout.addWidget(self.verticalSlider_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(80, 30, 71, 231))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_3 = QSlider(self.verticalLayoutWidget_2)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_2.addWidget(self.verticalSlider_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalLayoutWidget_3 = QWidget(self.groupBox)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(150, 30, 71, 231))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_6 = QSlider(self.verticalLayoutWidget_3)
        self.verticalSlider_6.setObjectName(u"verticalSlider_6")
        self.verticalSlider_6.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalLayoutWidget_4 = QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(360, 30, 81, 231))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_7 = QSlider(self.verticalLayoutWidget_4)
        self.verticalSlider_7.setObjectName(u"verticalSlider_7")
        self.verticalSlider_7.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_4.addWidget(self.verticalSlider_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.verticalLayoutWidget_5 = QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(220, 30, 71, 231))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_8 = QSlider(self.verticalLayoutWidget_5)
        self.verticalSlider_8.setObjectName(u"verticalSlider_8")
        self.verticalSlider_8.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_5.addWidget(self.verticalSlider_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.verticalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u043c\u0438 \u0434\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044f\u043c\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c 1", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c 2", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c 3", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0449\u0430\u044f \u0442\u044f\u0433\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0414\u0432\u0438\u0433\u0430\u0442\u0435\u043b\u044c 4", None))
    # retranslateUi

