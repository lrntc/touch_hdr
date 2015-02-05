import sys
import subprocess
import detect_camera
import touch_hdr_variables
from PySide.QtCore import *
from PySide.QtGui import *

class TouchHDRMenu(QWidget):
    def __init__(self):
        super(TouchHDRMenu, self).__init__()
        self.check = QCheckBox("HDR", self)
        self.btn_take_fast_hdr = QPushButton("Quick HDR", self)
        self.btn_take_picture = QPushButton("Capture", self)

        self.controlsLayout = QGridLayout()
        self.controlsLayout.addWidget(self.check, 0,0)
        self.controlsLayout.addWidget(self.btn_take_fast_hdr, 1,0)
        self.controlsLayout.addWidget(self.btn_take_picture, 0,1)

        self.setLayout(self.controlsLayout)

class AdvancedHDRLayout(QWidget):

    def select_all(self):

        self.check0.setCheckState(Qt.Checked)
        self.check1.setCheckState(Qt.Checked)
        self.check2.setCheckState(Qt.Checked)
        self.check3.setCheckState(Qt.Checked)
        self.check4.setCheckState(Qt.Checked)
        self.check5.setCheckState(Qt.Checked)
        self.check6.setCheckState(Qt.Checked)
        self.check7.setCheckState(Qt.Checked)
        self.check8.setCheckState(Qt.Checked)
        self.check9.setCheckState(Qt.Checked)
        self.check10.setCheckState(Qt.Checked)
        self.check11.setCheckState(Qt.Checked)
        self.check12.setCheckState(Qt.Checked)
        self.check13.setCheckState(Qt.Checked)
        self.check14.setCheckState(Qt.Checked)
        self.check15.setCheckState(Qt.Checked)
        self.check16.setCheckState(Qt.Checked)
        self.check17.setCheckState(Qt.Checked)
        self.check18.setCheckState(Qt.Checked)
        self.check19.setCheckState(Qt.Checked)
        self.check20.setCheckState(Qt.Checked)
        self.check21.setCheckState(Qt.Checked)
        self.check22.setCheckState(Qt.Checked)
        self.check23.setCheckState(Qt.Checked)
        self.check24.setCheckState(Qt.Checked)
        self.check25.setCheckState(Qt.Checked)
        self.check26.setCheckState(Qt.Checked)
        self.check27.setCheckState(Qt.Checked)
        self.check28.setCheckState(Qt.Checked)
        self.check29.setCheckState(Qt.Checked)
        self.check30.setCheckState(Qt.Checked)

    def select_half(self):

        self.check0.setCheckState(Qt.Checked)
     
        self.check2.setCheckState(Qt.Checked)
     
        self.check4.setCheckState(Qt.Checked)
     
        self.check6.setCheckState(Qt.Checked)
     
        self.check8.setCheckState(Qt.Checked)
     
        self.check10.setCheckState(Qt.Checked)
     
        self.check12.setCheckState(Qt.Checked)
     
        self.check14.setCheckState(Qt.Checked)
    
        self.check16.setCheckState(Qt.Checked)
    
        self.check18.setCheckState(Qt.Checked)
    
        self.check20.setCheckState(Qt.Checked)
    
        self.check22.setCheckState(Qt.Checked)
    
        self.check24.setCheckState(Qt.Checked)
    
        self.check26.setCheckState(Qt.Checked)
        
        self.check28.setCheckState(Qt.Checked)
        
        self.check30.setCheckState(Qt.Checked)
    
                
    def capture_photos(self):

        #self.btn_take_picture.setText("Caputuring..")

        #self.total = len(touch_hdr_variables.EV)
        
        #each step: XX Pictures to go

 #Loop though the checkboxes
        
        self.command_list = ["gphoto2"]

        for exp in range(0, len(touch_hdr_variables.EV)):
            self.temp_var = "check" + str(exp) 
            self.temp_check = getattr(self, str(self.temp_var))

            #Get checked ckeckboxes

            if self.temp_check.isChecked():
                print(exp, " Checked, and has value: ", touch_hdr_variables.EV_dict[exp])

                self.command_list.append("--set-config")
                self.command_list.append("/main/capturesettings/exposurecompensation=" + touch_hdr_variables.EV_dict[exp])
                self.command_list.append("--capture-image")
    
            else:
                print("nope")
                
        subprocess.call(self.command_list)
        print("HDR Sequence is done.")
        
           
           
    def __init__(self):
        super(AdvancedHDRLayout, self).__init__()

        self.controlsLayout = QGridLayout()

        x = 0
        y = 0

        for exp in range(0, len(touch_hdr_variables.EV)):
            print("value: ", exp, "has value ", touch_hdr_variables.EV[exp])

            #Declare variables
            self.temp_var = "check" + str(exp)
            setattr(self, str(self.temp_var), QCheckBox(touch_hdr_variables.EV[exp] , self))

            #add widgets to layout
            #self.temp_widget = "self." + str(self.temp_var)

            self.controlsLayout.addWidget(getattr(self, str(self.temp_var)), y, x)

            
            if int(x) < int(5):
    
                x = x + 1

            else:

                x = 0
                y = y + 1

        #Add menu buttons
        self.progress = QLabel("...", self)
        self.semi = QPushButton("Half", self)
        self.all = QPushButton("All", self)
        self.capture = QPushButton("Capture", self)

        self.controlsLayout.addWidget(self.progress, y, (x+1))
        self.controlsLayout.addWidget(self.semi, y, (x+2))
        self.controlsLayout.addWidget(self.all, y, (x+3))
        self.controlsLayout.addWidget(self.capture, y, (x+4))


        #Link action to menu buttons

        self.semi.clicked.connect(self.select_half)
        self.all.clicked.connect(self.select_all)
        self.capture.clicked.connect(self.capture_photos)

        self.setLayout(self.controlsLayout)

class TouchHDRWindow(QMainWindow):
    def __init__(self):
        super(TouchHDRWindow, self).__init__()
        self.widget = AdvancedHDRLayout()
        self.setCentralWidget(self.widget)

class TouchHDRWindowMenu(QMainWindow):
    def __init__(self):
        super(TouchHDRWindowMenu, self).__init__()
        self.widget = TouchHDRMenu()
        self.setCentralWidget(self.widget)

detect_camera.set_up_dslr()
        
app = QApplication(sys.argv)

window = TouchHDRWindow()
window.show()

app.exec_()
sys.exit()
