# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/matrix/Desktop/siqnal/qt/analysisscreen.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(869, 535)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 30))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.LogoDisplay = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LogoDisplay.sizePolicy().hasHeightForWidth())
        self.LogoDisplay.setSizePolicy(sizePolicy)
        self.LogoDisplay.setText(_fromUtf8(""))
        self.LogoDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.LogoDisplay.setObjectName(_fromUtf8("LogoDisplay"))
        self.horizontalLayout_3.addWidget(self.LogoDisplay)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_3.addWidget(self.line_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.ProgramNameDisplay = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ProgramNameDisplay.setFont(font)
        self.ProgramNameDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgramNameDisplay.setObjectName(_fromUtf8("ProgramNameDisplay"))
        self.verticalLayout.addWidget(self.ProgramNameDisplay)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ProjectNameDIsplay = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ProjectNameDIsplay.setFont(font)
        self.ProjectNameDIsplay.setAlignment(QtCore.Qt.AlignCenter)
        self.ProjectNameDIsplay.setObjectName(_fromUtf8("ProjectNameDIsplay"))
        self.horizontalLayout.addWidget(self.ProjectNameDIsplay)
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.horizontalLayout.addWidget(self.line_7)
        self.CodeSourceDisplay = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.CodeSourceDisplay.setFont(font)
        self.CodeSourceDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.CodeSourceDisplay.setObjectName(_fromUtf8("CodeSourceDisplay"))
        self.horizontalLayout.addWidget(self.CodeSourceDisplay)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.MentorNameDisplay = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.MentorNameDisplay.setFont(font)
        self.MentorNameDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.MentorNameDisplay.setObjectName(_fromUtf8("MentorNameDisplay"))
        self.horizontalLayout_2.addWidget(self.MentorNameDisplay)
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.horizontalLayout_2.addWidget(self.line_8)
        self.AuthorNameDisplay = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.AuthorNameDisplay.setFont(font)
        self.AuthorNameDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.AuthorNameDisplay.setObjectName(_fromUtf8("AuthorNameDisplay"))
        self.horizontalLayout_2.addWidget(self.AuthorNameDisplay)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_3.addWidget(self.line_3)
        self.MainTab = QtGui.QTabWidget(self.centralwidget)
        self.MainTab.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MainTab.sizePolicy().hasHeightForWidth())
        self.MainTab.setSizePolicy(sizePolicy)
        self.MainTab.setMinimumSize(QtCore.QSize(0, 0))
        self.MainTab.setObjectName(_fromUtf8("MainTab"))
        self.Signal1 = QtGui.QWidget()
        self.Signal1.setObjectName(_fromUtf8("Signal1"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.Signal1)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.FileLogoDisplay = QtGui.QLabel(self.Signal1)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FileLogoDisplay.sizePolicy().hasHeightForWidth())
        self.FileLogoDisplay.setSizePolicy(sizePolicy)
        self.FileLogoDisplay.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.FileLogoDisplay.setFont(font)
        self.FileLogoDisplay.setText(_fromUtf8(""))
        self.FileLogoDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.FileLogoDisplay.setObjectName(_fromUtf8("FileLogoDisplay"))
        self.verticalLayout_4.addWidget(self.FileLogoDisplay)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.FileNameDisplay = QtGui.QLineEdit(self.Signal1)
        self.FileNameDisplay.setReadOnly(True)
        self.FileNameDisplay.setPlaceholderText(_fromUtf8(""))
        self.FileNameDisplay.setObjectName(_fromUtf8("FileNameDisplay"))
        self.horizontalLayout_5.addWidget(self.FileNameDisplay)
        self.FileSelectButton = QtGui.QPushButton(self.Signal1)
        self.FileSelectButton.setObjectName(_fromUtf8("FileSelectButton"))
        self.horizontalLayout_5.addWidget(self.FileSelectButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.SampleFreqLabel = QtGui.QLabel(self.Signal1)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SampleFreqLabel.sizePolicy().hasHeightForWidth())
        self.SampleFreqLabel.setSizePolicy(sizePolicy)
        self.SampleFreqLabel.setMinimumSize(QtCore.QSize(138, 0))
        self.SampleFreqLabel.setObjectName(_fromUtf8("SampleFreqLabel"))
        self.horizontalLayout_6.addWidget(self.SampleFreqLabel)
        self.SampleFreqInput = QtGui.QLineEdit(self.Signal1)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SampleFreqInput.sizePolicy().hasHeightForWidth())
        self.SampleFreqInput.setSizePolicy(sizePolicy)
        self.SampleFreqInput.setObjectName(_fromUtf8("SampleFreqInput"))
        self.horizontalLayout_6.addWidget(self.SampleFreqInput)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.CentreFreqLabel = QtGui.QLabel(self.Signal1)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CentreFreqLabel.sizePolicy().hasHeightForWidth())
        self.CentreFreqLabel.setSizePolicy(sizePolicy)
        self.CentreFreqLabel.setMinimumSize(QtCore.QSize(149, 0))
        self.CentreFreqLabel.setObjectName(_fromUtf8("CentreFreqLabel"))
        self.horizontalLayout_7.addWidget(self.CentreFreqLabel)
        self.CentreFreqInput = QtGui.QLineEdit(self.Signal1)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CentreFreqInput.sizePolicy().hasHeightForWidth())
        self.CentreFreqInput.setSizePolicy(sizePolicy)
        self.CentreFreqInput.setObjectName(_fromUtf8("CentreFreqInput"))
        self.horizontalLayout_7.addWidget(self.CentreFreqInput)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.ImportValueButton = QtGui.QPushButton(self.Signal1)
        self.ImportValueButton.setObjectName(_fromUtf8("ImportValueButton"))
        self.verticalLayout_4.addWidget(self.ImportValueButton)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.line = QtGui.QFrame(self.Signal1)
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_8.addWidget(self.line)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(
            QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_5 = QtGui.QLabel(self.Signal1)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_5.addWidget(self.label_5)
        self.TimeLaunchButton = QtGui.QPushButton(self.Signal1)
        self.TimeLaunchButton.setObjectName(_fromUtf8("TimeLaunchButton"))
        self.verticalLayout_5.addWidget(self.TimeLaunchButton)
        self.FourierLaunchButton = QtGui.QPushButton(self.Signal1)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.FourierLaunchButton.sizePolicy().hasHeightForWidth())
        self.FourierLaunchButton.setSizePolicy(sizePolicy)
        self.FourierLaunchButton.setObjectName(
            _fromUtf8("FourierLaunchButton"))
        self.verticalLayout_5.addWidget(self.FourierLaunchButton)
        self.PowerLaunchButton = QtGui.QPushButton(self.Signal1)
        self.PowerLaunchButton.setObjectName(_fromUtf8("PowerLaunchButton"))
        self.verticalLayout_5.addWidget(self.PowerLaunchButton)
        self.SpectrogramLaunchButton = QtGui.QPushButton(self.Signal1)
        self.SpectrogramLaunchButton.setObjectName(
            _fromUtf8("SpectrogramLaunchButton"))
        self.verticalLayout_5.addWidget(self.SpectrogramLaunchButton)
        self.Spectrogram2LaunchButton = QtGui.QPushButton(self.Signal1)
        self.Spectrogram2LaunchButton.setObjectName(
            _fromUtf8("Spectrogram2LaunchButton"))
        self.verticalLayout_5.addWidget(self.Spectrogram2LaunchButton)
        self.BandpassLaunchButton = QtGui.QPushButton(self.Signal1)
        self.BandpassLaunchButton.setObjectName(
            _fromUtf8("BandpassLaunchButton"))
        self.verticalLayout_5.addWidget(self.BandpassLaunchButton)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.MainTab.addTab(self.Signal1, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.MainTab.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.MainTab)
        self.MainTab.raise_()
        self.line_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.MainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.ProgramNameDisplay.setText(_translate(
            "MainWindow", "Google Summer of Code 2017", None))
        self.ProjectNameDIsplay.setText(_translate(
            "MainWindow", "Project Name: SIQNAL", None))
        self.CodeSourceDisplay.setText(_translate(
            "MainWindow", "Code: <a href=\"https://github.com/aerospaceresearch/siqnal\">Github</a>", None))
        self.MentorNameDisplay.setText(_translate(
            "MainWindow", "Mentor: Andreas Horning", None))
        self.AuthorNameDisplay.setText(_translate(
            "MainWindow", "Author: Jay Krishna", None))
        self.FileSelectButton.setText(
            _translate("MainWindow", "Select File", None))
        self.SampleFreqLabel.setText(_translate(
            "MainWindow", "Sampling Frequency(MHz)", None))
        self.CentreFreqLabel.setText(_translate(
            "MainWindow", "Centre Frequency(MHz)", None))
        self.ImportValueButton.setText(
            _translate("MainWindow", "Import", None))
        self.label_5.setText(_translate(
            "MainWindow", "Visualization Section", None))
        self.TimeLaunchButton.setText(_translate(
            "MainWindow", "Time Domain Analysis", None))
        self.FourierLaunchButton.setText(_translate(
            "MainWindow", "Fourier Analysis", None))
        self.PowerLaunchButton.setText(_translate(
            "MainWindow", "Power Spectral Analysis", None))
        self.SpectrogramLaunchButton.setText(_translate(
            "MainWindow", "Spectrogram Analysis", None))
        self.Spectrogram2LaunchButton.setText(
            _translate("MainWindow", "Spectrogram Test", None))
        self.BandpassLaunchButton.setText(
            _translate("MainWindow", "Bandpass Filter", None))
        self.MainTab.setTabText(self.MainTab.indexOf(
            self.Signal1), _translate("MainWindow", "Signal 1", None))
        self.MainTab.setTabText(self.MainTab.indexOf(
            self.tab_3), _translate("MainWindow", "Analysis", None))
