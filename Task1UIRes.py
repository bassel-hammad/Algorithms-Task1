from PyQt5 import QtCore, QtGui, QtWidgets
from patient import Patient
from datetime import datetime

COLORS = ["#ecf0f1", "#bdc3c7", "#7f8c8d", "#95a5a6", "#2c3e50", "#34495e"]
FONT_COLORS = ["#2C3E50", "#2C3E50", "#ECF0F1", "#2C3E50", "#ECF0F1", "#ECF0F1"]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        self.arrivalTimeEdit.setTime(QtCore.QTime(8, 0))
        self.departureTimeEdit.setTime(QtCore.QTime(8, 0))
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

        self.addPatientButton.clicked.connect(self.add_patient)
        self.deletePatientButton.clicked.connect(self.delete_patient)

        self.updateButton.clicked.connect(self.update_schedule)
        self.sorted_patients = {
            "severity":[],
            "arrival":[],
            "departure":[]
        }
        self.waiting = 0





    def reset_inputs(self):
        self.idLineEdit.clear()
        self.nameLineEdit.clear()
        self.arrivalTimeEdit.setTime(QtCore.QTime(8, 0))
        self.departureTimeEdit.setTime(QtCore.QTime(17, 0))
        self.severitySpinBox.setValue(0)


    def add_patient(self):
        id = self.idLineEdit.text()
        name = self.nameLineEdit.text()
        arrival_time = self.arrivalTimeEdit.time().toString("HH:mm")
        departure_time = self.departureTimeEdit.time().toString("HH:mm")
        severity = self.severitySpinBox.value()
        new_patient = Patient(id, name, arrival_time, departure_time, severity)
        self.patients.append(new_patient)
        self.insert_patient(new_patient)
        self.add_patient_to_combo_box(new_patient)
        self.reset_inputs()



    def color_cells(self, room_index, start_slot, end_slot, color):
        for col in range(start_slot, end_slot + 1):
            item = self.tableWidget.item(room_index, col)
            if item is not None:
                item.setBackground(color)  
            else:
                new_item = QtWidgets.QTableWidgetItem()
                new_item.setBackground(color)
                self.tableWidget.setItem(room_index, col, new_item)

  
    def insert_patient(self, new_patient):
        if len(self.sorted_patients["severity"])==0 :
            for key in self.sorted_patients:
                self.sorted_patients[key].append(new_patient)
        else: 
            for i in range(len(self.sorted_patients["severity"])):
                if new_patient.severity > self.sorted_patients["severity"][i].severity:  
                    self.sorted_patients["severity"].insert(i, new_patient)  
                    break
            else:
                self.sorted_patients["severity"].append(new_patient)

            for i in range(len(self.sorted_patients["arrival"])):
                if new_patient.arrival_time < self.sorted_patients["arrival"][i].arrival_time: 
                    self.sorted_patients["arrival"].insert(i, new_patient)  
                    break
            else:

                self.sorted_patients["arrival"].append(new_patient)


            for i in range(len(self.sorted_patients["departure"])):
                if new_patient.departure_time < self.sorted_patients["departure"][i].departure_time:  
                    self.sorted_patients["departure"].insert(i, new_patient)  
                    break
            else:
                self.sorted_patients["departure"].append(new_patient)


    def delete_patient(self):
        index = self.patientsComboBox.currentIndex()
        if index >= 0 and index < len(self.patients):  
            patient_to_delete = self.patients[index]
            for key in self.sorted_patients:
                if patient_to_delete in self.sorted_patients[key]:
                    self.sorted_patients[key].remove(patient_to_delete)
            del self.patients[index]

            self.patientsComboBox.removeItem(index)

    def add_patient_to_combo_box(self, patient):
        patient_info = f"{patient.name} (ID: {patient.id}, Severity: {patient.severity}) (Arrival: {patient.arrival_time}, Departure: {patient.departure_time}) "
        self.patientsComboBox.addItem(patient_info)



    def update_schedule(self):
        if(self.severityRadioButton.isChecked()):
            algo = "severity"
        elif(self.arrivalRadioButton.isChecked()):
            algo = "arrival"
        elif (self.departureRadioButton.isChecked()):
            algo = "departure"
        else:
            return
        self.rooms= [
            [0,0,0],
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]
        
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(4)
        time_slots = ["8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", 
                      "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", 
                      "4:00 PM", "5:00 PM"]
        self.tableWidget.setColumnCount(len(time_slots))
        self.tableWidget.setHorizontalHeaderLabels(time_slots)
        patient_in_rooms =0
        for patient in self.sorted_patients[algo]:
            
            arrival_hour = int(patient.arrival_time.split(':')[0]) - 8
            if 'PM' in patient.arrival_time and arrival_hour != 12:
                arrival_hour += 12
            departure_hour = int(patient.departure_time.split(':')[0]) - 8
            if 'PM' in patient.departure_time and departure_hour != 12:
                departure_hour += 12

            if 0 <= arrival_hour < 10 and 0 <= departure_hour < 10:
                time_slot_index = arrival_hour
                for room in self.rooms:

                    if arrival_hour >= room[1] or (departure_hour <= room[0]):
                        
                        room_index = self.rooms.index(room)
                        room[0] = min(room[0],arrival_hour) if sum(room)!=0 else arrival_hour
                        room[1] = max(room[1],departure_hour)
                        

                        item = QtWidgets.QTableWidgetItem(patient.name)

                        # Set font to bold and increase size for visibility
                        font = QtGui.QFont()
                        font.setBold(True)
                        font.setPointSize(10)  # Adjust the size as needed
                        item.setFont(font)

                        # Optional: Set text color to ensure contrast
                        item.setForeground(QtGui.QBrush(QtGui.QColor(FONT_COLORS[room[2]%6]))) 

                        # Set the item in the table and color the cell
                        self.tableWidget.setItem(room_index, time_slot_index, item)
                        self.color_cells(room_index, time_slot_index, departure_hour - 1, QtGui.QColor((COLORS[room[2]%6])))

                        patient_in_rooms +=1
                        room[2]+=1
                        break
                    
                waiting = len(self.sorted_patients[algo]) - patient_in_rooms
                self.waitingLcdNumber.display(waiting)
            


    



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
