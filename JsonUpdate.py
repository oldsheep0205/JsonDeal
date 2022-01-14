# coding=gbk
import json
from typing import List, Dict
import os
from GeneralTool import GeneralTool
import sys
import time
import demjson

_BASEPATH = "./base"
_NAMEANCHOR = "patch_"



class JsonUpdate:
    '''
    路径结构：
    vallain
          -base 
          -patch_a
          ...
          -处理器.exe
    '''
    _filefrompatch = []#all jsons from patch
    _filefrombase = []  #all jsons from base
    _latestdict = []
    _foldername = []
    _patchlist = []
    


    def __init__(self):
        '''
        Constructor
        '''
        print("自动适配器启动")
        print('')

        self._filefrompatch = []
        self._patchlist = []
        self._foldername = ''

        for i in os.listdir():  #读取所有需要刷的patch文件夹
            if i[:6] == _NAMEANCHOR and os.path.isdir(i):
                self._patchlist.append(i)

        try:
            for i in os.listdir(_BASEPATH):  #读取base各个json
                if ".json" in i:
                    self._filefrombase.append(i)
        except:
            print("请把此程序放入vallain文件夹下，与base和patch_文件同级！")
            print("五秒后自动退出...")
            time.sleep(5)
            sys.exit(0)

    def loopPatch(self):
        '''
        轮回每个mod
        '''
        for modfolder in self._patchlist:

            self._foldername = modfolder
            self._filefrompatch = []
        
            
            for i in os.listdir("./" + self._foldername + '/'): 
                if ".json" in i:
                    self._filefrompatch.append(i)   # 读取每个mod文件夹里的东西
            print("************************************************")
            print("[操作] 正在适配 " + self._foldername)
            print('')
            self.autoUpdateJson()
            
            

    def autoUpdateJson(self):
        """
        auto update the json to the latest version.
        idea:
        1. read all json from your patch_
        2. for each json, check whether it is in base, if so, read one block from base
        3. read one block from your patch_, check whether needs rewrite(check key)
        4. if need, write.
        """

        for i in self._filefrompatch:
            dictpatch = []

            if i in self._filefrombase:

                print("[操作]检测文件: " + i)
                print("[操作]清理不规范行为")
    
                datalist = GeneralTool.parse_json("./" + self._foldername + "/" + i)#one block from patch
                
                if datalist[0] == False:
                    continue

                data = datalist[1]
                dictpatch = data[0]
                isupdate = True

                try: 
                    with open("./base/" + i, "r", encoding='UTF-8') as f: #one set of key from patch
                        data = json.load(f)
                        self._latestdict = data[0]
                except UnicodeDecodeError:
                    with open("./base/" + i, "r") as f: #one set of key from patch
                        data = json.load(f)
                        self._latestdict = data[0]

                if list(dictpatch.keys()) == list(self._latestdict.keys()):  # Is more attribute?
                    
                    isupdate = False
                    for j, k in zip(dictpatch.values(), self._latestdict.values()): # Is type of attribute change?
                        if type(j) != type(k):
                            isupdate = True
                            break

                if isupdate:
                    GeneralTool.mkDir("./output/update/" + self._foldername + "/")
                    print("[操作] " + i + " 需要更新！开始更新...")
                    self.updateJsonHelper(i)
                    print("[操作] " + i + " 更新完成！")
                    print("")
                else:
                    print("[操作]文件 " + i + " 无需更新！")
                    print('')


    def updateJsonHelper(self, filename) -> None:

        """
        create a new folder and output good json
        """
        rawdata: List[Dict]
        output = []
  
        rawdata = GeneralTool.parse_json("./" + self._foldername + '/' + filename)[1]

        for eachblock in rawdata:   # make dict = base dict, then change value from patch value
            tempdict = self._latestdict.copy()

            for key, value in eachblock.items():

                if key not in tempdict.keys():  # new version cut down key, then escape.
                    continue
                
                if type(value) == type(tempdict[key]):  # type not change.
                    tempdict[key] = value
                    
                elif self.isNum(tempdict[key])[0]: # if value from base is a number:

                    if self.isDigital(value)[0] and self.isDigital(value)[1] == 'int':
                        tempdict[key] = int(value) # old data is a str of int
                        
                    elif self.isDigital(value)[0] and self.isDigital(value)[1] == 'float':
                        tempdict[key] = float(value) # old data is a str of float
                        
                elif self.isDigital(tempdict[key])[0]: # if value from base is a str:

                    if self.isDigital(tempdict[key])[1] == 'int' and self.isNum(value)[0]:
                        tempdict[key] = str(int(value))

                    elif self.isDigital(tempdict[key])[1] == 'float' and self.isNum(value)[0]:
                        tempdict[key] = str(float(value))
                        
                    
            
            output.append(tempdict)

        print("更新完成！")
        print("[操作]开始写入...")

        with open("./output/update/" + self._foldername + '/' + filename, "w") as outfile:
            outfile.write(json.dumps(output, indent = 2, ensure_ascii = False))
        print("[操作]写入完成")

            
    def isNum(self, input1):
        
        '''
        输入是数字类型
        '''
        
        if isinstance(input1, int):
            return [True, 'int']
        elif isinstance(input1, float):
            return [True, 'float']

        return [False, '']
            
    def isDigital(self, input1):
        '''
        输入是非数字类型
        '''

        if not (isinstance(input1, int) or isinstance(input1, float) or isinstance(input1, str)):
            return [False, ""]

        test = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
        
        typein = "int"
        for i in input1:
            if i not in test:
                return [False, ""]
            elif i == '.':
                typein = "float"

        return [True, typein]