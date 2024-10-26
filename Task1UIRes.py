from PyQt5 import QtCore, QtGui, QtWidgets
from patient import Patient
from datetime import datetime



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # Initialize the patient list
        self.patients = []

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 703)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)
        self.severitySpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.severitySpinBox.setObjectName("severitySpinBox")
        self.gridLayout_6.addWidget(self.severitySpinBox, 2, 1, 1, 1)
        self.addPatientButton = QtWidgets.QPushButton(self.groupBox)
        self.addPatientButton.setObjectName("addPatientButton")
        self.gridLayout_6.addWidget(self.addPatientButton, 2, 4, 1, 3)
        self.idLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.idLineEdit.setObjectName("idLineEdit")
        self.gridLayout_6.addWidget(self.idLineEdit, 0, 5, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 2, 0, 1, 1)
        self.arrivalTimeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.arrivalTimeEdit.setObjectName("arrivalTimeEdit")
        self.gridLayout_6.addWidget(self.arrivalTimeEdit, 1, 1, 1, 1)
        self.nameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.gridLayout_6.addWidget(self.nameLineEdit, 0, 1, 1, 2)
        self.departureTimeEdit = QtWidgets.QTimeEdit(self.groupBox)
        self.departureTimeEdit.setObjectName("departureTimeEdit")
        self.gridLayout_6.addWidget(self.departureTimeEdit, 1, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 1, 5, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 6, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.severityRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.severityRadioButton.setObjectName("severityRadioButton")
        self.gridLayout_7.addWidget(self.severityRadioButton, 3, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 3, 0, 1, 1)
        self.patientsComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.patientsComboBox.setObjectName("patientsComboBox")
        self.gridLayout_7.addWidget(self.patientsComboBox, 1, 0, 1, 7)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)
        self.updateButton = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.gridLayout_7.addWidget(self.updateButton, 4, 0, 1, 3)
        self.waitingLcdNumber = QtWidgets.QLCDNumber(self.groupBox_2)
        self.waitingLcdNumber.setObjectName("waitingLcdNumber")
        self.gridLayout_7.addWidget(self.waitingLcdNumber, 4, 5, 1, 2)
        self.deletePatientButton = QtWidgets.QPushButton(self.groupBox_2)
        self.deletePatientButton.setObjectName("deletePatientButton")
        self.gridLayout_7.addWidget(self.deletePatientButton, 0, 1, 1, 6)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 4, 4, 1, 1)
        self.departureRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.departureRadioButton.setObjectName("departureRadioButton")
        self.gridLayout_7.addWidget(self.departureRadioButton, 3, 4, 1, 1)
        self.arrivalRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.arrivalRadioButton.setObjectName("arrivalRadioButton")
        self.gridLayout_7.addWidget(self.arrivalRadioButton, 3, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 6, 2, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(84)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(72)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 7, 1, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5.addLayout(self.gridLayout, 0, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 1, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the "Add Patient" button and "Delete Patient" button
        self.addPatientButton.clicked.connect(self.add_patient)
        self.deletePatientButton.clicked.connect(self.delete_patient)
        # Connect updateButton to update schedule function
        self.updateButton.clicked.connect(self.update_schedule)



    def add_patient(self):
        # Collect data from the input fields
        id = self.idLineEdit.text()
        name = self.nameLineEdit.text()
        arrival_time = self.arrivalTimeEdit.time().toString("HH:mm")
        departure_time = self.departureTimeEdit.time().toString("HH:mm")
        severity = self.severitySpinBox.value()
        # Create a Patient instance
        new_patient = Patient(id, name, arrival_time, departure_time, severity)
        # Add the patient to the list
        self.patients.append(new_patient)
        # Add the patient to the combo box
        self.add_patient_to_combo_box(new_patient)
        # Optionally, clear input fields after adding
        self.idLineEdit.clear()
        self.nameLineEdit.clear()
        self.arrivalTimeEdit.setTime(QtCore.QTime(0, 0))
        self.departureTimeEdit.setTime(QtCore.QTime(0, 0))
        self.severitySpinBox.setValue(0)

    def delete_patient(self):
        # Get the index of the selected patient in the combo box
        index = self.patientsComboBox.currentIndex()
        if index >= 0:  # Check if a patient is selected
            # Remove the selected patient from the patients list
            del self.patients[index]
            # Remove the patient from the combo box
            self.patientsComboBox.removeItem(index)
            for patient in self.patients:
                print(f"ID: {patient.id}, Name: {patient.name}")

    def add_patient_to_combo_box(self, patient):
        # Format the patient information for display in the combo box
        patient_info = f"{patient.name} (ID: {patient.id}, Severity: {patient.severity}) (Arrival: {patient.arrival_time}, Departure: {patient.departure_time}) "
        self.patientsComboBox.addItem(patient_info)
        for patient in self.patients:
                print(f"ID: {patient.id}, Name: {patient.name}")

    def sort_patients_by_severity(self):
        # Create a new sorted array of patients by severity in descending order
        severity_sorted_patients = sorted(self.patients, key=lambda patient: patient.severity, reverse=True)     
        print("Patients sorted by severity (descending):")
        for patient in severity_sorted_patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Severity: {patient.severity}")

    def sort_patients_by_arrival(self):
    # Function to convert time string to datetime object
        def parse_time(patient):
            return datetime.strptime(patient.arrival_time, "%H:%M")      
        # Sort the patients by arrival time in ascending order
        arrival_sorted_patients = sorted(self.patients, key=parse_time)
        # Print or update the UI with sorted patients
        print("Sorted Patients by Arrival Time (Ascending):")
        for patient in arrival_sorted_patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Arrival Time: {patient.arrival_time}")

    def sort_patients_by_departure(self):
    # Function to convert time string to datetime object
        def parse_time(patient):
            return datetime.strptime(patient.departure_time, "%H:%M")      
        # Sort the patients by departure time in ascending order
        departure_sorted_patients = sorted(self.patients, key=parse_time)
        # Print or update the UI with sorted patients
        print("Sorted Patients by Departure Time (Ascending):")
        for patient in departure_sorted_patients:
            print(f"ID: {patient.id}, Name: {patient.name}, Departure Time: {patient.departure_time}")

    def update_schedule(self):
        if(self.severityRadioButton.isChecked()):
            self.sort_patients_by_severity()
        elif(self.arrivalRadioButton.isChecked()):
            self.sort_patients_by_arrival()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Add Patient"))
        self.label_2.setText(_translate("MainWindow", "Name :"))
        self.label_4.setText(_translate("MainWindow", "Arrival Time"))
        self.addPatientButton.setText(_translate("MainWindow", "Add Patient"))
        self.label_6.setText(_translate("MainWindow", "Severity :"))
        self.label_3.setText(_translate("MainWindow", "ID :"))
        self.label_5.setText(_translate("MainWindow", "Expected Departure Time"))
        self.groupBox_2.setTitle(_translate("MainWindow", "My Patients"))
        self.severityRadioButton.setText(_translate("MainWindow", "Severity"))
        self.label_8.setText(_translate("MainWindow", "Sorting Criteria"))
        self.label_7.setText(_translate("MainWindow", "Current Patients :"))
        self.updateButton.setText(_translate("MainWindow", "Update Schedule"))
        self.deletePatientButton.setText(_translate("MainWindow", "Delete Patient"))
        self.label_9.setText(_translate("MainWindow", "Waiting:"))
        self.departureRadioButton.setText(_translate("MainWindow", "Departure"))
        self.arrivalRadioButton.setText(_translate("MainWindow", "Arrival"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Room 1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Room 2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Room 3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Room 4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "8:00"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "9:00"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "10:00"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "11:00"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "12:00"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "1:00"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "2:00"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "3:00"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "4:00"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "5:00"))
        self.label.setText(_translate("MainWindow", "ICU Scheduler"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
