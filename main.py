import os
import configparser
import sys
import shutil
import logging
import logging.handlers
import threading
import subprocess


class Main:    
    def __init__(self):        

        self.initConfig()
        self.initlog()

        print("init ok")        

    def writeConfig(self):
        self.writeLog("write log")

        _Config['Common'] = {
            'programName' : 'test programs',
            'Version' : '1.0'
        }

        with open(_ConfigFileName, 'w') as f:
            _Config.write(f)


    def loadConfig(self):
        self.writeLog('config load start')

        #config 읽기 ( 최초에 파일이 없으면 생성)
        if(os.path.isfile(_ConfigFileName) == False):
            self.writeConfig()

        programName = _Config.get('Common', 'programName')
        version = _Config.get('Common', 'Version')

        self.writeLog(programName)
        self.writeLog(version)

        self.writeLog('config load ok')
        
    def initConfig(self):    
        global _ConfigFileName
        global _Config

        _ConfigFileName = 'config.ini'
        _Config = configparser.ConfigParser()

    def initlog(self): 
        global _Logger

        # logger 인스턴스를 생성 및 로그 레벨 설정
        _Logger = logging.getLogger("crumbs")
        _Logger.setLevel(logging.DEBUG)

        # fileHandler와 StreamHandler를 생성
        fileHandler = logging.FileHandler('./log.log')
        streamHandler = logging.StreamHandler()

        # Handler를 logging에 추가
        _Logger.addHandler(fileHandler)
        _Logger.addHandler(streamHandler)


    def main(self):
        self.writeLog('Start')

        self.loadConfig()

        return 0

    def writeLog(self, msg):
        print(msg)

        _Logger.info(msg)


#project start
# 현재 폴더 위치에서 실행

# 중복 실행 방지 ( 추 후 추가 )
        
# Main class object 생성 및 메인 함수 실행
main = Main()
main.main()





