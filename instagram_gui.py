# importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PyQt5 import QtWidgets, uic , QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys , warnings , requests , io
warnings.filterwarnings("ignore")
template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1151</width>
    <height>857</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <pointsize>10</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <property name="styleSheet">
   <string notr="true">QMainWindow{
	background-color: rgb(254, 255, 227);
}
</string>
  </property>
  <property name="animated">
   <bool>true</bool>
  </property>
  <property name="documentMode">
   <bool>false</bool>
  </property>
  <property name="tabShape">
   <enum>QTabWidget::Rounded</enum>
  </property>
  <widget class="QWidget" name="centralwidget">
   <property name="autoFillBackground">
    <bool>false</bool>
   </property>
   <property name="styleSheet">
    <string notr="true"/>
   </property>
   <widget class="Line" name="line_25">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>50</y>
      <width>351</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QPushButton" name="send_message">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>700</y>
      <width>251</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
	color: gold;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
	border: 2px solid rgb(58, 134, 255);
	border-radius: 20px;
}
QPushButton:hover {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
  color: white;
}</string>
    </property>
    <property name="text">
     <string>Send Message</string>
    </property>
   </widget>
   <widget class="QPushButton" name="download">
    <property name="geometry">
     <rect>
      <x>820</x>
      <y>700</y>
      <width>251</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
	color: gold;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
	border: 2px solid rgb(58, 134, 255);
	border-radius: 20px;
}
QPushButton:hover {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
  color: white;
}</string>
    </property>
    <property name="text">
     <string>Download</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="message_box">
    <property name="geometry">
     <rect>
      <x>450</x>
      <y>330</y>
      <width>251</width>
      <height>321</height>
     </rect>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="styleSheet">
     <string notr="true">QTextEdit {
   	border-radius: 10px;
	border: 2px solid rgb(255, 69, 0);
    color: rgb(0, 0, 255);
 }    
</string>
    </property>
    <property name="placeholderText">
     <string>Message ...</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>200</y>
      <width>91</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway ExtraLight</family>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>@</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>80</y>
      <width>351</width>
      <height>80</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway ExtraLight</family>
      <pointsize>17</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Send Direct Message</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>80</y>
      <width>211</width>
      <height>80</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway ExtraLight</family>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="text">
     <string>Account Info</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>810</x>
      <y>130</y>
      <width>241</width>
      <height>80</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway ExtraLight</family>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="text">
     <string>400522148</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>800</x>
      <y>70</y>
      <width>271</width>
      <height>80</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway ExtraLight</family>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="autoFillBackground">
     <bool>false</bool>
    </property>
    <property name="text">
     <string>Seyed ali Kamali</string>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="QLineEdit" name="entered_id">
    <property name="geometry">
     <rect>
      <x>485</x>
      <y>220</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway</family>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">    QLineEdit {
   		 border-radius: 10px;
		border: 2px solid rgb(255, 69, 0);
    	color: rgb(0, 0, 255);
    }    
</string>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="placeholderText">
     <string>Id</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ask_path">
    <property name="geometry">
     <rect>
      <x>820</x>
      <y>329</y>
      <width>251</width>
      <height>331</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
	color: gold;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
	border: 2px solid rgb(58, 134, 255);
	border-radius: 20px;
}
QPushButton:hover {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
  color: white;
}</string>
    </property>
    <property name="text">
     <string>Select Where you
 wnat to save
 stories</string>
    </property>
   </widget>
   <widget class="QPushButton" name="followers_count">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>700</y>
      <width>251</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
	color: gold;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
	border: 2px solid rgb(58, 134, 255);
	border-radius: 20px;
}
QPushButton:hover {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
  color: white;
}</string>
    </property>
    <property name="text">
     <string>Followers Count</string>
    </property>
   </widget>
   <widget class="QPushButton" name="followings_count">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>620</y>
      <width>251</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
	color: gold;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
	border: 2px solid rgb(58, 134, 255);
	border-radius: 20px;
}
QPushButton:hover {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
  color: white;
}</string>
    </property>
    <property name="text">
     <string>Following Count</string>
    </property>
   </widget>
   <widget class="QPushButton" name="posts_count">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>540</y>
      <width>251</width>
      <height>50</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
	color: gold;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
	border: 2px solid rgb(58, 134, 255);
	border-radius: 20px;
}
QPushButton:hover {
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.857143, y2:0.857955, stop:1 rgba(10, 242, 251, 255), stop:0 rgba(224, 6, 159, 255));
  color: white;
}</string>
    </property>
    <property name="text">
     <string>Posts Count</string>
    </property>
   </widget>
   <widget class="QLabel" name="Image">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>270</y>
      <width>211</width>
      <height>191</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Raleway ExtraLight</family>
      <pointsize>20</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="alignment">
     <set>Qt::AlignCenter</set>
    </property>
   </widget>
   <widget class="Line" name="line_26">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>780</y>
      <width>351</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>60</y>
      <width>20</width>
      <height>731</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_2">
    <property name="geometry">
     <rect>
      <x>740</x>
      <y>60</y>
      <width>20</width>
      <height>731</height>
     </rect>
    </property>
    <property name="toolTipDuration">
     <number>-1</number>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_27">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>50</y>
      <width>351</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_3">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>60</y>
      <width>20</width>
      <height>731</height>
     </rect>
    </property>
    <property name="toolTipDuration">
     <number>-1</number>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_28">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>780</y>
      <width>351</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_4">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>60</y>
      <width>20</width>
      <height>731</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_29">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>770</x>
      <y>50</y>
      <width>351</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_5">
    <property name="geometry">
     <rect>
      <x>1110</x>
      <y>60</y>
      <width>20</width>
      <height>731</height>
     </rect>
    </property>
    <property name="toolTipDuration">
     <number>-1</number>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="Line" name="line_30">
    <property name="enabled">
     <bool>true</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>770</x>
      <y>780</y>
      <width>351</width>
      <height>21</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="Line" name="line_6">
    <property name="geometry">
     <rect>
      <x>760</x>
      <y>60</y>
      <width>20</width>
      <height>731</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">color : rgb(255, 69, 0);</string>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Plain</enum>
    </property>
    <property name="lineWidth">
     <number>2</number>
    </property>
    <property name="midLineWidth">
     <number>1</number>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
class Instagram:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions() 
        prefs = {"profile.default_content_setting_values.notifications":2,"profile.managed_default_content_settings.images": 2} #parametrs to disable asking notification and loading images
        chrome_options.add_experimental_option("prefs", prefs) # set prefs
        self.driver = webdriver.Chrome(options =chrome_options) #initial chrome driver
        self.driver.set_page_load_timeout(10) #set page load time to 10 seconds    
        
        login_state = False
        while login_state == False:
            login_state = self.login()
            print(login_state)
        
        self.Not_now_button() 

        self.profile = False
        while self.profile == False:
            self.profile = self.get_info()
            

    def login(self):
        """ login to instagram main page by username and password"""
        try:
            self.driver.get("https://www.instagram.com/?hl=en")
            #driver.find_element(by=By.NAME, value='username').click()

            input_username_Element = self.driver.find_element(by=By.NAME, value='username') #find username input
            input_username_Element.send_keys('insta_for_sel_ap@hi2.in') #type username

            input_password_Element = self.driver.find_element(by=By.NAME, value='password') #find username password
            input_password_Element.send_keys('AP_1401@sel') #type password

            #driver.find_element(by=By.CSS_SELECTOR, value='.sqdOP > .qF0y9').click()   
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Log In']"))).click() #click on login button
            return True
        except:
            return False
        
    def Not_now_button(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Not Now']"))).click() #click on Not now button on Save Your Login Info
            return True
        except: 
            return False
        
    def get_info(self):
        try:
            self.driver.get("https://www.instagram.com/insta_for_sel_ap/")
            post_count = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[text()=' posts']"))).text
            try: name = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[2]/span").text
            except: name = None
            try: bio = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[2]/div").text
            except: bio = None    
            try: id_ = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[2]/div").text
            except: id_ = None        
            return   {
            'post_count': post_count,#driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[1]/div/span").text,
            'followers_count': self.driver.find_element(By.XPATH, "//div[text()=' followers']").text, 
            'following_count': self.driver.find_element(By.XPATH, "//div[text()=' following']").text,
            'profile_photo': self.driver.find_element(By.XPATH,"//img[starts-with (@alt,'Change profile photo')]").get_attribute("src"),   
            'name': name,
            'bio': bio,
            'id': id_,
            }
        except:
            return False
        
    def send_direct(self,id_contanct ,msg):
        self.driver.get(f"https://www.instagram.com/{id_contanct}/")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Follow']"))).click()
        except:
            pass
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Message']"))).click()
        try:
            input_message_Element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Message...']")))
            input_message_Element.click()
            input_message_Element.send_keys(msg)
            input_message_Element.send_keys(Keys.ENTER)
            return True
        except Exception as e: 
            return False
        
    def get_scr(self):
        try:
            return {"type":"video","url": self.driver.find_element(By.XPATH, "//video[starts-with (@poster,'data')]").find_element(By.XPATH,'//source').get_attribute("src")}
        except:
            try:
                return {"type":"img","url": self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[6]/div/div/img").get_attribute("src")}
            except: 
                return {"type":"unknow","url":"Cant find url"}
            
    def get_stories(self):
        list_data = []
        try:
            self.driver.get("https://www.instagram.com/")

            while self.driver.current_url == 'https://www.instagram.com/':
                try:
                    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//button[starts-with (@aria-label,'Story by')]"))).click()
                except:
                    pass

            while self.driver.current_url != 'https://www.instagram.com/':
                try:
                    list_data.append(self.get_scr())
                    WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Next']"))).click()
                except:
                    self.driver.find_elements(By.CSS_SELECTOR, ".coreSpriteRightChevron")[0].click()

            return list_data
        except:
            return False


# function to alter image
def mask_image(imgdata, imgtype ='jpg', size = 175):

	# Load image
	image = QImage.fromData(imgdata, imgtype)

	# convert image to 32-bit ARGB (adds an alpha
	# channel ie transparency factor):
	image.convertToFormat(QImage.Format_ARGB32)

	# Crop image to a square:
	imgsize = min(image.width(), image.height())
	rect = QRect(
		(image.width() - imgsize) / 2,
		(image.height() - imgsize) / 2,
		imgsize,
		imgsize,
	)
	
	image = image.copy(rect)

	# Create the output image with the same dimensions
	# and an alpha channel and make it completely transparent:
	out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
	out_img.fill(Qt.transparent)

	# Create a texture brush and paint a circle
	# with the original image onto the output image:
	brush = QBrush(image)

	# Paint the output image
	painter = QPainter(out_img)
	painter.setBrush(brush)

	# Don't draw an outline
	painter.setPen(Qt.NoPen)

	# drawing circle
	painter.drawEllipse(0, 0, imgsize, imgsize)

	# closing painter event
	painter.end()

	# Convert the image to a pixmap and rescale it.
	pr = QWindow().devicePixelRatio()
	pm = QPixmap.fromImage(out_img)
	pm.setDevicePixelRatio(pr)
	size *= pr
	pm = pm.scaled(size, size, Qt.KeepAspectRatio,Qt.SmoothTransformation)

	# return back the pixmap data
	return pm


DATA_INSTA = Instagram()

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(io.StringIO(template), self)

        self.setWindowTitle("Instagram")
        
        # image path
        imgpath = "image.jpg"
        self.info = DATA_INSTA.profile
        print(self.info)
        # loading image
        r = requests.get(self.info['profile_photo'])
        if r.status_code == 200:
            with open(imgpath, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        imgdata = open(imgpath, 'rb').read()
        pixmap = mask_image(imgdata)
        self.ilabel = self.findChild(QtWidgets.QLabel, 'Image')
        self.ilabel.setPixmap(pixmap)


        
        self.findChild(QtWidgets.QPushButton, 'posts_count').setText(self.info['post_count'])
        self.findChild(QtWidgets.QPushButton, 'followings_count').setText(self.info['following_count'])
        self.findChild(QtWidgets.QPushButton, 'followers_count').setText(self.info['followers_count'])
        
        self.findChild(QtWidgets.QPushButton, 'ask_path').clicked.connect(self.saveFileDialog)
        self.findChild(QtWidgets.QPushButton, 'download').clicked.connect(self.download_stories)
        self.findChild(QtWidgets.QPushButton, 'send_message').clicked.connect(self.Send_direct)
        

        self.show()

    def saveFileDialog(self):
        global folder_selected    
        dialog = QFileDialog()
        folder_selected = dialog.getExistingDirectory(self, 'Select an awesome directory')
        
    def download_stories(self):
        if 'folder_selected' in globals() and not folder_selected == "":
            print(folder_selected)
            data_stories_list = DATA_INSTA.get_stories()
            x = 0
            for data in data_stories_list:
                try:
                    x += 1
                    if data["type"] == "video":
                        open(f"{folder_selected}/instagram{x}.mp4", "wb").write(requests.get(data["url"]).content)
                    elif data["type"] == "img":
                        open(f"{folder_selected}/instagram{x}.jpg", "wb").write(requests.get(data["url"]).content)
                except Exception as e:
                    print(e)
                    
        else:
            QMessageBox.warning(self,"Error","You didn't select where you want to save stories")
            return False

    def Send_direct(self):
        try:
            message = self.findChild(QtWidgets.QTextEdit, 'message_box').toPlainText()
            id_ = self.findChild(QtWidgets.QLineEdit, 'entered_id').text()
        except Exception as e:
            print(e)
        if id_ == "":
            QMessageBox.warning(self,"Error","You didn't enter any id.")
            return False
        
        if message == "":
            QMessageBox.warning(self,"Error","You didn't enter any message.")
            return False
        
        try:
            DATA_INSTA.send_direct(id_,message)
        except :
            pass
                
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    sys.exit(app.exec_())
