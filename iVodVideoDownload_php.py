# -*- coding: utf-8 -*-
# iVod影片下載handler
import urllib2, sys, re, os, xml.etree.ElementTree, subprocess as sp
from PyQt4.QtGui import *
from PyQt4.QtCore import *
reload(sys)
sys.setdefaultencoding('utf8')

e = xml.etree.ElementTree.parse('setting.xml').getroot()
phpExecutionPath =e.findall('phpLocation')[0].text
# 輸入參數
# argURLandFileNameList list[str,str] #  下載位置 和 檔名 List[URL,FileName]
# argSaveFolder : str # 下載目錄
# argHD : boolean # 是否下載高畫質
# argQTStatus : QTextBrowser # 顯示進度的控制項
class iVodVideoDownload(QMainWindow):
    def __init__(self, argURLandFileNameList, argSaveFolder, argHD, argQTStatus):
        if not self.hasPHP(phpExecutionPath):
            raise Exception("Can't find PHP; please install PHP and change location above")
        QWidget.__init__(self)
        self.SaveFolder = argSaveFolder
        self.QtStatus = argQTStatus
        self.Manifest = []
        self.header = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
        for URLAndFileName in argURLandFileNameList:
            URL = URLAndFileName[0]
            FileName = argSaveFolder + "/" + URLAndFileName[1]
            if argHD:
                URL = str(URLAndFileName[0]).replace('300K', '1M')
            # 檢查URL然後抓資料
            if URL != '':
                html = urllib2.urlopen(urllib2.Request(URL, None, self.header)).read()
            # Find RealURL
            # readyPlayer('http://ivod.ly.gov.tw/public/scripts/','http://h264media01.ly.gov.tw:1935/vod/_definst_/mp4:1MClips/a7d6027a1ded6aa66237e895a7b354309c450e450740cf30da2b760e9327b2fda041cae092e76417.mp4/manifest.f4m');
            match_readyplayer = re.findall(r"readyPlayer\('.*\)", html)

            manifest_url = re.findall(r",\'.*\)", match_readyplayer[0])[0][2:-2]
            manifest_html = urllib2.urlopen(urllib2.Request(manifest_url, None, self.header)).read()

            duration_sec = re.findall(r'<duration>.*<', manifest_html)[0][10:-2]
            duration_min = float(duration_sec) / 60.0
            tempFileName = argSaveFolder + "/tmp.flv"
            self.Manifest.append([URL, manifest_url, FileName])
            self.process = QProcess(self)
            self.process.readyReadStandardOutput.connect(self.dataReady)
            self.process.finished.connect(self.finish)

    def downloadFile(self):
        downloadfailed = []
        self.QtStatus.append(unicode('PHP Location:') + phpExecutionPath)
        for manifest in self.Manifest:
            tempFileName = self.SaveFolder + "/tmp.flv"
            FileName = manifest[2]

            # xdownload = AdobeHDS.M6(manifest[1],tempFileName)

            self.running = False

            self.QtStatus.append(unicode('下載檔名:') + FileName)
            self.QtStatus.append(unicode('原始URL:') + manifest[0])
            self.QtStatus.append(unicode('Manifest URL:') + manifest[1])

            # call php
            self.callAdobeHDS(manifest[1], tempFileName)

            # 更新QT元件
            while self.running:
                QApplication.processEvents()

            # 如果有暫存檔案存在 下載失敗 刪除暫存檔
            if not os.path.isfile(tempFileName):
                downloadfailed.append(FileName)
                for s in os.listdir('./'):
                    if s.find('Seg1-Frag') != -1:
                        os.remove(s)
            # 轉換下載名稱 若有重複更改新下載名
            else:
                while (os.path.isfile(FileName)):
                    FileName = FileName[0:-4] + "_1.flv"
                os.rename(tempFileName, FileName)
        if len(downloadfailed) != 0:
            for s in downloadfailed:
                self.QtStatus.append(s + u'  download 失敗')

    def callAdobeHDS(self, manifestURL, tmpFileLocation):
        self.running = True
        self.process.start(phpExecutionPath,
                           ["AdobeHDS.php", "--quality", "high", "--useragent", self.header['User-agent'],
                            '--delete', '--outfile', tmpFileLocation, '--manifest',
                            manifestURL])  # , shell=True, stdout=subprocess.PIPE)

    def finish(self):
        self.running = False

    def dataReady(self):
        cursor = self.QtStatus.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(str(self.process.readAllStandardOutput()))
        self.QtStatus.ensureCursorVisible()

    def hasPHP(self, arg):
        try:
            sp.check_call([arg, '-v'])
            return True
        except:
            return False

# 測試區塊
# global mainForm
# def button_click():
#     status = mainForm.findChild(QTextBrowser,"Status");
#     listURL = [["http://ivod.ly.gov.tw/Play/VOD/76472/300K","test.flv"]]
#     download = iVodVideoDownload(listURL, "./",True,status)
#     download.downloadFile()
#
# def main():
#     app = QApplication(sys.argv)
#     global mainForm
#     mainForm = QWidget()
#     mainForm.resize(800,400)
#     layout = QVBoxLayout()
#     edit = QTextBrowser()
#     edit.setObjectName("Status")
#     edit.setWindowTitle("QTextEdit Standard Output Redirection")
#     layout.addWidget(edit)
#     button = QPushButton()
#     button.clicked.connect(button_click)
#     layout.addWidget(button)
#     mainForm.setLayout(layout)
#     mainForm.show()
#     app.exec_()
#
#
# if __name__ == '__main__':
#     main()