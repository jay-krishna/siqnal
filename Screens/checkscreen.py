# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/matrix/Desktop/siqnal/qt/checkscreen.ui'
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


class Ui_checkscreen(object):
    def setupUi(self, checkscreen):
        checkscreen.setObjectName(_fromUtf8("checkscreen"))
        checkscreen.resize(688, 500)
        checkscreen.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(checkscreen)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.LogoDisplay = QtGui.QLabel(checkscreen)
        sizePolicy = QtGui.QSizePolicy(
            QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LogoDisplay.sizePolicy().hasHeightForWidth())
        self.LogoDisplay.setSizePolicy(sizePolicy)
        self.LogoDisplay.setMinimumSize(QtCore.QSize(0, 150))
        self.LogoDisplay.setText(_fromUtf8(""))
        self.LogoDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.LogoDisplay.setObjectName(_fromUtf8("LogoDisplay"))
        self.verticalLayout.addWidget(self.LogoDisplay)
        self.line = QtGui.QFrame(checkscreen)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.ProgramDisplay = QtGui.QLabel(checkscreen)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.ProgramDisplay.setFont(font)
        self.ProgramDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.ProgramDisplay.setObjectName(_fromUtf8("ProgramDisplay"))
        self.verticalLayout.addWidget(self.ProgramDisplay)
        self.line_2 = QtGui.QFrame(checkscreen)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ProjectName = QtGui.QLabel(checkscreen)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sans Serif"))
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ProjectName.setFont(font)
        self.ProjectName.setAlignment(QtCore.Qt.AlignCenter)
        self.ProjectName.setObjectName(_fromUtf8("ProjectName"))
        self.horizontalLayout.addWidget(self.ProjectName)
        self.line_5 = QtGui.QFrame(checkscreen)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.CodeSource = QtGui.QLabel(checkscreen)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.CodeSource.setFont(font)
        self.CodeSource.setAlignment(QtCore.Qt.AlignCenter)
        self.CodeSource.setObjectName(_fromUtf8("CodeSource"))
        self.horizontalLayout.addWidget(self.CodeSource)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_3 = QtGui.QFrame(checkscreen)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.MentorNameDisplay = QtGui.QLabel(checkscreen)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.MentorNameDisplay.setFont(font)
        self.MentorNameDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.MentorNameDisplay.setObjectName(_fromUtf8("MentorNameDisplay"))
        self.horizontalLayout_2.addWidget(self.MentorNameDisplay)
        self.line_6 = QtGui.QFrame(checkscreen)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout_2.addWidget(self.line_6)
        self.AuthorNameDisplay = QtGui.QLabel(checkscreen)
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
        self.line_4 = QtGui.QFrame(checkscreen)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.ProgressBar = QtGui.QProgressBar(checkscreen)
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName(_fromUtf8("ProgressBar"))
        self.verticalLayout.addWidget(self.ProgressBar)
        self.ProgressDisplay = QtGui.QTextEdit(checkscreen)
        self.ProgressDisplay.setReadOnly(True)
        self.ProgressDisplay.setOverwriteMode(False)
        self.ProgressDisplay.setObjectName(_fromUtf8("ProgressDisplay"))
        self.verticalLayout.addWidget(self.ProgressDisplay)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.StartButton = QtGui.QPushButton(checkscreen)
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.horizontalLayout_3.addWidget(self.StartButton)
        self.ProceedButton = QtGui.QPushButton(checkscreen)
        self.ProceedButton.setEnabled(False)
        self.ProceedButton.setObjectName(_fromUtf8("ProceedButton"))
        self.horizontalLayout_3.addWidget(self.ProceedButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(checkscreen)
        QtCore.QMetaObject.connectSlotsByName(checkscreen)

    def retranslateUi(self, checkscreen):
        checkscreen.setWindowTitle(_translate("checkscreen", "Dialog", None))
        self.ProgramDisplay.setText(_translate(
            "checkscreen", "Google Summer of Code 2017", None))
        self.ProjectName.setText(_translate(
            "checkscreen", "Project Name: SIQNAL", None))
        self.CodeSource.setText(_translate(
            "checkscreen", "Code: <a href=\'https://github.com/aerospaceresearch/siqnal\'>Github</a>", None))
        self.MentorNameDisplay.setText(_translate(
            "checkscreen", "Mentor: Andreas Horning", None))
        self.AuthorNameDisplay.setText(_translate(
            "checkscreen", "Author: Jay Krishna", None))
        self.StartButton.setText(_translate("checkscreen", "Start", None))
        self.ProceedButton.setText(_translate("checkscreen", "Proceed", None))
