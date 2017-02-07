# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(431, 425)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.context = QtGui.QLabel(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.context.sizePolicy().hasHeightForWidth())
        self.context.setSizePolicy(sizePolicy)
        self.context.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.context.setObjectName("context")
        self.gridLayout_3.addWidget(self.context, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lw_FileList = QtGui.QListWidget(self.groupBox)
        self.lw_FileList.setObjectName("lw_FileList")
        self.gridLayout.addWidget(self.lw_FileList, 2, 0, 1, 3)
        self.pb_loadFiles = QtGui.QPushButton(self.groupBox)
        self.pb_loadFiles.setObjectName("pb_loadFiles")
        self.gridLayout.addWidget(self.pb_loadFiles, 3, 0, 1, 1)
        self.pb_delFiles = QtGui.QPushButton(self.groupBox)
        self.pb_delFiles.setObjectName("pb_delFiles")
        self.gridLayout.addWidget(self.pb_delFiles, 3, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.te_notes = QtGui.QTextEdit(self.groupBox_2)
        self.te_notes.setObjectName("te_notes")
        self.gridLayout_2.addWidget(self.te_notes, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.pb_submit = QtGui.QPushButton(Dialog)
        self.pb_submit.setObjectName("pb_submit")
        self.gridLayout_3.addWidget(self.pb_submit, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.context.setText(QtGui.QApplication.translate("Dialog", "Your Current Context: ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", " Files To Review", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_loadFiles.setText(QtGui.QApplication.translate("Dialog", "Add Images", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_delFiles.setText(QtGui.QApplication.translate("Dialog", "Remove Images", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_submit.setText(QtGui.QApplication.translate("Dialog", "Submit", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
