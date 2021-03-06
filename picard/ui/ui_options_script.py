# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScriptingOptionsPage(object):
    def setupUi(self, ScriptingOptionsPage):
        ScriptingOptionsPage.setObjectName("ScriptingOptionsPage")
        ScriptingOptionsPage.resize(605, 377)
        self.vboxlayout = QtWidgets.QVBoxLayout(ScriptingOptionsPage)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.enable_tagger_scripts = QtWidgets.QGroupBox(ScriptingOptionsPage)
        self.enable_tagger_scripts.setCheckable(True)
        self.enable_tagger_scripts.setObjectName("enable_tagger_scripts")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.enable_tagger_scripts)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.enable_tagger_scripts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_script = QtWidgets.QPushButton(self.groupBox)
        self.add_script.setObjectName("add_script")
        self.horizontalLayout.addWidget(self.add_script)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.script_list = QtWidgets.QListWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.script_list.sizePolicy().hasHeightForWidth())
        self.script_list.setSizePolicy(sizePolicy)
        self.script_list.setObjectName("script_list")
        self.formWidget = QtWidgets.QWidget(self.splitter)
        self.formWidget.setObjectName("formWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.formWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.script_name = QtWidgets.QLineEdit(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.script_name.sizePolicy().hasHeightForWidth())
        self.script_name.setSizePolicy(sizePolicy)
        self.script_name.setObjectName("script_name")
        self.verticalLayout_2.addWidget(self.script_name)
        self.tagger_script = QtWidgets.QTextEdit(self.formWidget)
        self.tagger_script.setObjectName("tagger_script")
        self.verticalLayout_2.addWidget(self.tagger_script)
        self.verticalLayout_3.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.groupBox)
        self.script_error = QtWidgets.QLabel(self.enable_tagger_scripts)
        self.script_error.setText("")
        self.script_error.setAlignment(QtCore.Qt.AlignCenter)
        self.script_error.setObjectName("script_error")
        self.verticalLayout.addWidget(self.script_error)
        self.scripting_doc_link = QtWidgets.QLabel(self.enable_tagger_scripts)
        self.scripting_doc_link.setText("")
        self.scripting_doc_link.setWordWrap(True)
        self.scripting_doc_link.setOpenExternalLinks(True)
        self.scripting_doc_link.setObjectName("scripting_doc_link")
        self.verticalLayout.addWidget(self.scripting_doc_link)
        self.vboxlayout.addWidget(self.enable_tagger_scripts)

        self.retranslateUi(ScriptingOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(ScriptingOptionsPage)
        ScriptingOptionsPage.setTabOrder(self.enable_tagger_scripts, self.add_script)
        ScriptingOptionsPage.setTabOrder(self.add_script, self.script_list)
        ScriptingOptionsPage.setTabOrder(self.script_list, self.script_name)
        ScriptingOptionsPage.setTabOrder(self.script_name, self.tagger_script)

    def retranslateUi(self, ScriptingOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.enable_tagger_scripts.setTitle(_("Tagger Script(s)"))
        self.add_script.setToolTip(_("Add new script"))
        self.add_script.setText(_("Add new script"))
        self.script_name.setPlaceholderText(_("Display Name"))

