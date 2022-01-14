# coding=gbk
import json
from stack import MyStack
import time
from GeneralTool import GeneralTool

_PATH = "./output/process/"



class JsonProcess:
    """
    main process part!
    """
    _filepath: str
    _resetkey: str
    _numstart: int
    _stack: MyStack
    
    def __init__(self, inputpath):

        self._filepath = inputpath
        self._stack = MyStack()
        
    
    def processId(self, num):

        
        
        self._numstart = int(num)
        print("[����]��ȡԴ�ļ�...")
        print('')
        time.sleep(1)
        datalist = GeneralTool.parse_json(self._filepath) #List[Dict]
        print("[����]��ȡ���")
        print('')
        if datalist[0] == False:
            print("����ļ��ǿյģ�������ֹ...")
            print("[����]û���κ����")
            print('')
            return
        time.sleep(1)
           
        print("[����]�޸�����...")
        print('')
        data = datalist[1]

        try:
            for i in data:
                oldid = i["id"]
                print(oldid)
                self._stack.push(oldid)  # push to stack

                for key, value in i.items():
                    strint = str(self._numstart)

                    if key == "id":
                        
                        if self._stack.checkIn(value):
                            self._numstart -= 1
                            i[key] = int(str(self._numstart) + str(self._stack.checkGap(value)))
                            oldid = oldid // 10
                        else:
                            i[key] = self._numstart

                        print("id " + str(oldid) + " ---> " + str(i[key]))
                    # change id part
    
                    elif isinstance(value, str):
                        
                        if str(oldid) in value:
                            before = value
                            temp = value[:-len(str(oldid))]
                            i[key] = temp + strint
                            print(key + ": " + before + " ---> " + i[key])
                        #change complex value part such as drama_dialogue90003014

                        elif value.isdigit() and int(value) == oldid + 1:
                            before = value
                            i[key] = str(self._numstart + 1)
                            print(key + ": " + before + " ---> " + i[key])
                    #change nextdialogue
                        
                self._numstart += 1
                
            print("[����]�޸����")
            print('')

        except Exception as e:
            print("[ʧ��]\t\t" + e)

        print("[����]��ʼд�����ļ�...")
        time.sleep(1)
        try:
            with open("./output/process/" + self._filepath, "w") as outfile: 
                outfile.write(json.dumps(data, indent = 2, ensure_ascii = False))
                print("[����]д�����")
                
        except Exception as e:
            print("[ʧ��]\t\t" + e)

        return
            
            
            
            
            
            
            
            
            