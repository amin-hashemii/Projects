from tkinter import E
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtCore import QUrl
import os
import audio_metadata

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow:QtWidgets.QMainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 330)

        img = QtGui.QImage('back.jpg')
        img = img.scaled(QtCore.QSize(804, 330))
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(img))
        MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(110, 280, 75, 23))
        self.pushButton_play.setObjectName("pushButton_play")

        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(390, 190, 111, 101))
        self.dial.setObjectName("dial")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(550, 0, 256, 330))
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)

        self.label_vol = QtWidgets.QLabel(self.centralwidget)
        self.label_vol.setGeometry(QtCore.QRect(410, 285, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.label_vol.setFont(font)
        self.label_vol.setObjectName("label_vol")

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(10, 20, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")

        self.label_fileName = QtWidgets.QLabel(self.centralwidget)
        self.label_fileName.setGeometry(QtCore.QRect(70, 20, 251, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.label_fileName.setFont(font)
        self.label_fileName.setObjectName("label_fileName")

        self.label_album = QtWidgets.QLabel(self.centralwidget)
        self.label_album.setGeometry(QtCore.QRect(10, 50, 53, 13))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_album.setFont(font)
        self.label_album.setObjectName("label_album")

        self.label_fileAlbum = QtWidgets.QLabel(self.centralwidget)
        self.label_fileAlbum.setGeometry(QtCore.QRect(70, 50, 251, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.label_fileAlbum.setFont(font)
        self.label_fileAlbum.setObjectName("label_fileAlbum")

        self.label_artist = QtWidgets.QLabel(self.centralwidget)
        self.label_artist.setGeometry(QtCore.QRect(10, 80, 53, 13))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_artist.setFont(font)
        self.label_artist.setObjectName("label_artist")

        self.label_fileArtist = QtWidgets.QLabel(self.centralwidget)
        self.label_fileArtist.setGeometry(QtCore.QRect(70, 80, 251, 16))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(True)
        self.label_fileArtist.setFont(font)
        self.label_fileArtist.setObjectName("label_fileArtist")

        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(110, 250, 71, 21))
        self.label_time.setObjectName("label_time")

        self.pushButton_pre = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pre.setGeometry(QtCore.QRect(70, 280, 31, 23))
        self.pushButton_pre.setText("<<")
        self.pushButton_pre.setObjectName("pushButton_pre")

        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(190, 280, 31, 23))
        self.pushButton_next.setText(">>")
        self.pushButton_next.setObjectName("pushButton_next")
        
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(70, 250, 31, 23))
        self.pushButton_back.setText("<-5s")
        self.pushButton_back.setObjectName("pushButton_for")

        self.pushButton_for = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_for.setGeometry(QtCore.QRect(190, 250, 31, 23))
        self.pushButton_for.setText("5s->")
        self.pushButton_for.setObjectName("pushButton_for")

        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open.setGeometry(QtCore.QRect(440, 10, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setObjectName("pushButton_open")

        self.pushButton_open_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_file.setGeometry(QtCore.QRect(440, 40, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_open_file.setFont(font)
        self.pushButton_open_file.setObjectName("pushButton_open_file")

        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(440, 70, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setObjectName("pushButton_delete")

        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(440, 100, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("self.pushButton_clear")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Player
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)
        self.playlist_files = {}

        # Player Variables
        self.is_playing = False
        self.is_mataGet = False
        
        # Signals
        self.pushButton_open.clicked.connect(self.open_folder)
        self.pushButton_open_file.clicked.connect(self.open_file)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_play.clicked.connect(self.play)
        self.dial.valueChanged.connect(self.vol_change)
        self.player.positionChanged.connect(self.time_change)
        self.pushButton_for.clicked.connect(lambda:self.player.setPosition(self.player.position()+5000))
        self.pushButton_back.clicked.connect(lambda:self.player.setPosition(self.player.position()-5000))
        self.playlist.currentMediaChanged.connect(self.reset)
        self.pushButton_next.clicked.connect(lambda:self.playlist.next())
        self.pushButton_pre.clicked.connect(lambda:self.playlist.previous())
        self.pushButton_clear.clicked.connect(self.clear)

        # set  
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(20)
        self.dial.setNotchesVisible(True)

        # StyleSheet
        self.label_time.setStyleSheet('color:cyan;')
        self.pushButton_for.setStyleSheet('color:rgb(255, 0, 127);')
        self.pushButton_back.setStyleSheet('color:rgb(255, 0, 127);')
        self.pushButton_play.setStyleSheet('color:rgb(0, 204, 0);')
        self.pushButton_next.setStyleSheet('color:rgb(255, 0, 127);')
        self.pushButton_pre.setStyleSheet('color:rgb(255, 0, 127);')
        self.label_album.setStyleSheet('color:rgb(240, 52, 171);')
        self.label_artist.setStyleSheet('color:rgb(240, 52, 171);')
        self.label_name.setStyleSheet('color:rgb(240, 52, 171);')
        self.label_fileName.setStyleSheet('color:rgb(127, 0, 255);')
        self.label_fileAlbum.setStyleSheet('color:rgb(127, 0, 255);')
        self.label_fileArtist.setStyleSheet('color:rgb(127, 0, 255);')
        self.dial.setStyleSheet('background-color:blue;')
        self.label_vol.setStyleSheet("color:rgb(127, 0, 255);")
        self.pushButton_open.setStyleSheet('color:rgb(0, 128, 255)')
        self.pushButton_open_file.setStyleSheet('color:rgb(0, 128, 255)')
        self.pushButton_delete.setStyleSheet('color:red;')
        self.pushButton_clear.setStyleSheet('color:red;')
        

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MP3 Player"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.label_name.setText(_translate("MainWindow", "Name :"))
        self.label_fileName.setText(_translate("MainWindow", "None"))
        self.label_album.setText(_translate("MainWindow", "Album : "))
        self.label_fileAlbum.setText(_translate("MainWindow", "None"))
        self.label_artist.setText(_translate("MainWindow", "Artist : "))
        self.label_fileArtist.setText(_translate("MainWindow", "None"))
        self.pushButton_open.setText(_translate("MainWindow", "Open folder"))
        self.pushButton_open_file.setText(_translate("MainWindow", "Open file"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete From List"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear the List"))
        self.label_time.setText(_translate("MainWindow", "00:00 / 00:00"))

    def clear(self):
        self.playlist.clear()
        self.listWidget.clear()
        self.playlist_files = {}
        self.is_mataGet = False
        self.is_playing = False

    def reset(self):
        self.is_mataGet = False
        self.is_playing = False

    def set_labels(self):
        album = 'None'
        artist = 'None'
        name = 'None'
        metadata = audio_metadata.load(self.playlist_files[self.listWidget.item(self.playlist.currentIndex()).text()])
        try:
            album = metadata['tags']['album'][0]
            artist = metadata['tags']['artist'][0]
            name = metadata['tags']['title'][0]
        except:
            pass
        self.label_fileName.setText(name)
        self.label_fileArtist.setText(artist)
        self.label_fileAlbum.setText(album)
        self.listWidget.setCurrentRow(self.playlist.currentIndex())

    def time_change(self):
        if not self.is_mataGet:
            self.set_labels()
            self.is_mataGet = True
        dur_sec = int(self.player.duration()/1000)
        dur_min = dur_sec//60
        dur_sec -= dur_min*60
        sec = int(self.player.position()/1000)
        min = sec//60
        sec -= min*60
        self.label_time.setText(f'{min}:{sec} / {dur_min}:{dur_sec}')

    def vol_change(self):
        self.label_vol.setText('Value: '+str(self.dial.value()))
        self.player.setVolume(self.dial.value())
        val = 0
        old_range = 100-0 # OldRange = (OldMax - OldMin)  
        new_range = 255-0 # NewRange = (NewMax - NewMin) 
        # NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
        val = (((self.dial.value() - 0) * new_range) / old_range) + 0
        self.label_vol.setStyleSheet(f'color:rgb({val}, 50, 125);')

    def delete(self):
        i = self.listWidget.currentRow()
        if i != -1:
            if self.listWidget.count() == 0:
                self.clear()
            self.playlist.removeMedia(i)
            self.listWidget.takeItem(i)
            self.set_labels()
            self.is_mataGet = True

    def open_folder(self):
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if folder:
            for root, _, fs in os.walk(folder):
                for file in fs:
                    if file[-3:] == 'mp3' or file[-3:] == 'mp3':
                        self.listWidget.addItem(os.path.basename(file))
                        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(os.path.join(root, file))))
                        self.playlist_files[file] = os.path.join(root, file)

    def open_file(self):
        file = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open File', filter='*.mp3 *.wav')
        if file[0]:
            file = file[0][0]
            self.listWidget.addItem(os.path.basename(file))
            self.playlist.addMedia(QMediaContent(QUrl(file)))
            self.playlist_files[os.path.basename(file)] = file

    def play(self):
        if self.is_playing:
            self.player.pause()
            self.is_playing = False
            self.pushButton_play.setText('Play')

        elif not self.playlist.isEmpty():
            self.player.play()
            self.is_playing = True
            self.pushButton_play.setText('Pause')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
