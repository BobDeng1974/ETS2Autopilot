# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/settings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(753, 583)
        self.screen_cap = QtWidgets.QLabel(MainWindow)
        self.screen_cap.setGeometry(QtCore.QRect(160, 20, 480, 270))
        self.screen_cap.setMinimumSize(QtCore.QSize(360, 200))
        self.screen_cap.setAutoFillBackground(False)
        self.screen_cap.setFrameShape(QtWidgets.QFrame.Box)
        self.screen_cap.setText("")
        self.screen_cap.setObjectName("screen_cap")
        self.cb_screen = QtWidgets.QComboBox(MainWindow)
        self.cb_screen.setGeometry(QtCore.QRect(10, 30, 131, 28))
        self.cb_screen.setObjectName("cb_screen")
        self.cb_screen.addItem("")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 20))
        self.label.setObjectName("label")
        self.slider_left = QtWidgets.QScrollBar(MainWindow)
        self.slider_left.setGeometry(QtCore.QRect(140, 320, 521, 16))
        self.slider_left.setOrientation(QtCore.Qt.Horizontal)
        self.slider_left.setObjectName("slider_left")
        self.slider_right = QtWidgets.QScrollBar(MainWindow)
        self.slider_right.setGeometry(QtCore.QRect(140, 350, 521, 16))
        self.slider_right.setSliderPosition(99)
        self.slider_right.setOrientation(QtCore.Qt.Horizontal)
        self.slider_right.setObjectName("slider_right")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(100, 318, 31, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(90, 348, 41, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.slider_top = QtWidgets.QScrollBar(MainWindow)
        self.slider_top.setGeometry(QtCore.QRect(670, 10, 16, 291))
        self.slider_top.setOrientation(QtCore.Qt.Vertical)
        self.slider_top.setObjectName("slider_top")
        self.slider_bottom = QtWidgets.QScrollBar(MainWindow)
        self.slider_bottom.setGeometry(QtCore.QRect(700, 10, 16, 291))
        self.slider_bottom.setProperty("value", 99)
        self.slider_bottom.setOrientation(QtCore.Qt.Vertical)
        self.slider_bottom.setObjectName("slider_bottom")
        self.b_refreshImage = QtWidgets.QPushButton(MainWindow)
        self.b_refreshImage.setGeometry(QtCore.QRect(20, 260, 111, 30))
        self.b_refreshImage.setObjectName("b_refreshImage")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(660, 300, 31, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(690, 300, 51, 20))
        self.label_5.setObjectName("label_5")
        self.gb_joystick = QtWidgets.QGroupBox(MainWindow)
        self.gb_joystick.setGeometry(QtCore.QRect(10, 370, 591, 211))
        self.gb_joystick.setCheckable(False)
        self.gb_joystick.setObjectName("gb_joystick")
        self.cb_devices = QtWidgets.QComboBox(self.gb_joystick)
        self.cb_devices.setGeometry(QtCore.QRect(60, 30, 171, 28))
        self.cb_devices.setObjectName("cb_devices")
        self.label_6 = QtWidgets.QLabel(self.gb_joystick)
        self.label_6.setGeometry(QtCore.QRect(10, 32, 66, 20))
        self.label_6.setObjectName("label_6")
        self.b_refreshDevices = QtWidgets.QPushButton(self.gb_joystick)
        self.b_refreshDevices.setGeometry(QtCore.QRect(240, 30, 71, 30))
        self.b_refreshDevices.setObjectName("b_refreshDevices")
        self.e_autopilot = QtWidgets.QLineEdit(self.gb_joystick)
        self.e_autopilot.setGeometry(QtCore.QRect(320, 80, 51, 32))
        self.e_autopilot.setObjectName("e_autopilot")
        self.label_8 = QtWidgets.QLabel(self.gb_joystick)
        self.label_8.setGeometry(QtCore.QRect(190, 84, 121, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.gb_joystick)
        self.label_9.setGeometry(QtCore.QRect(0, 124, 121, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.e_leftIndicator = QtWidgets.QLineEdit(self.gb_joystick)
        self.e_leftIndicator.setGeometry(QtCore.QRect(130, 120, 51, 32))
        self.e_leftIndicator.setObjectName("e_leftIndicator")
        self.label_10 = QtWidgets.QLabel(self.gb_joystick)
        self.label_10.setGeometry(QtCore.QRect(0, 164, 121, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.e_rightIndicator = QtWidgets.QLineEdit(self.gb_joystick)
        self.e_rightIndicator.setGeometry(QtCore.QRect(130, 160, 51, 32))
        self.e_rightIndicator.setObjectName("e_rightIndicator")
        self.label_11 = QtWidgets.QLabel(self.gb_joystick)
        self.label_11.setGeometry(QtCore.QRect(190, 124, 121, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.e_steering = QtWidgets.QLineEdit(self.gb_joystick)
        self.e_steering.setGeometry(QtCore.QRect(320, 120, 51, 32))
        self.e_steering.setObjectName("e_steering")
        self.e_throttle = QtWidgets.QLineEdit(self.gb_joystick)
        self.e_throttle.setGeometry(QtCore.QRect(320, 160, 51, 32))
        self.e_throttle.setObjectName("e_throttle")
        self.label_12 = QtWidgets.QLabel(self.gb_joystick)
        self.label_12.setGeometry(QtCore.QRect(190, 164, 121, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.gb_joystick)
        self.label_13.setEnabled(False)
        self.label_13.setGeometry(QtCore.QRect(409, 22, 66, 20))
        self.label_13.setObjectName("label_13")
        self.rb_gamepad = QtWidgets.QRadioButton(self.gb_joystick)
        self.rb_gamepad.setEnabled(False)
        self.rb_gamepad.setGeometry(QtCore.QRect(450, 20, 111, 25))
        self.rb_gamepad.setCheckable(True)
        self.rb_gamepad.setChecked(True)
        self.rb_gamepad.setObjectName("rb_gamepad")
        self.rb_wheel = QtWidgets.QRadioButton(self.gb_joystick)
        self.rb_wheel.setEnabled(False)
        self.rb_wheel.setGeometry(QtCore.QRect(450, 50, 131, 25))
        self.rb_wheel.setObjectName("rb_wheel")
        self.label_14 = QtWidgets.QLabel(self.gb_joystick)
        self.label_14.setGeometry(QtCore.QRect(0, 84, 121, 20))
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.e_vjoy = QtWidgets.QLineEdit(self.gb_joystick)
        self.e_vjoy.setGeometry(QtCore.QRect(130, 80, 51, 32))
        self.e_vjoy.setObjectName("e_vjoy")
        self.b_save = QtWidgets.QPushButton(MainWindow)
        self.b_save.setGeometry(QtCore.QRect(640, 540, 95, 30))
        self.b_save.setObjectName("b_save")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.cb_screen.setItemText(0, _translate("MainWindow", "Screen 1"))
        self.label.setText(_translate("MainWindow", "Choose Screen:"))
        self.label_2.setText(_translate("MainWindow", "Left"))
        self.label_3.setText(_translate("MainWindow", "Right"))
        self.b_refreshImage.setText(_translate("MainWindow", "Refresh image"))
        self.label_4.setText(_translate("MainWindow", "Top"))
        self.label_5.setText(_translate("MainWindow", "Bottom"))
        self.gb_joystick.setTitle(_translate("MainWindow", "Controller"))
        self.label_6.setText(_translate("MainWindow", "Device:"))
        self.b_refreshDevices.setText(_translate("MainWindow", "Refresh"))
        self.label_8.setText(_translate("MainWindow", "Autopilot button:"))
        self.label_9.setText(_translate("MainWindow", "Left indicator:"))
        self.label_10.setText(_translate("MainWindow", "Right indicator:"))
        self.label_11.setText(_translate("MainWindow", "Steering axis:"))
        self.label_12.setText(_translate("MainWindow", "Throttle axis:"))
        self.label_13.setText(_translate("MainWindow", "Type:"))
        self.rb_gamepad.setText(_translate("MainWindow", "Gamepad"))
        self.rb_wheel.setText(_translate("MainWindow", "Steering wheel"))
        self.label_14.setText(_translate("MainWindow", "vJoy Device:"))
        self.b_save.setText(_translate("MainWindow", "Save"))

