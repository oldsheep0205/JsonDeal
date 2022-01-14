# coding=gbk
'''
Created on 2022.1.8

@author: �쳾
'''

from JsonProcess import JsonProcess
import time
import sys
from JsonUpdate import JsonUpdate
from GeneralTool import GeneralTool
from Logger import Logger

_VERSION = "v2.6"
_NAME = "��Ȱ˻�json�๦������������"
_WEBSITE = "https://bbs.3dmgame.com/thread-6254819-1-1.html"


def welcomeGUI():

    print("************************************************")
    print(_NAME+ ' ' + _VERSION)
    print("����:�쳾")
    print("QQ: 93633818")
    print("QQȺ: 995876973")
    print("bվid: ���Ȱ׾Ƶĺ쳾")
    print("3dm����ָ·��" + _WEBSITE)
    print("��л����磬��� �Ա����������Ľܳ�����")
    print("************************************************")
    print("�뽫���ļ�����vallain�ļ����£���base�ļ��к�patch_�ļ�ͬ������������")
    print("�뽫���ļ�����vallain�ļ����£���base�ļ��к�patch_�ļ�ͬ������������")
    print("�뽫���ļ�����vallain�ļ����£���base�ļ��к�patch_�ļ�ͬ������������")
    print("************************************************")
    print("")
    print("1. ����json����")
    print("2. mod�����°汾")
    print("9. �˳�")
    print("")

    while True:
        
        print("��ѡ��: ")
        choose = sys.stdin.readline().strip('\n')
        
        if choose == "9":
            print("")
            print("ллʹ�ã��ټ���")
            input("��enter���˳�")
            sys.exit(0)

        elif choose == '1':
            GeneralTool.mkDir("./output/process/")
            guiInputPath()
            break
            
        elif choose == '2':
            GeneralTool.mkDir("./output/update/")
            ju1 = JsonUpdate()
            ju1.loopPatch()
            print("")
            print("��������")
            print("��������output�ļ����µ�update�ļ���")
            print("")
            print("************************************************")
            print("************************************************")
            print("�Ҹ棺json�ǲ�������ע�͵ģ��Ұ���ɾ�ˣ���Ҫ�������ϰ��")
            print('�Ҹ棺json�ļ��Ľ�β�ǲ������ж��ŵģ�ϣ��ע��')
            print("����Ķ�ע������ִ�������Դ�ļ����ղ鿴")
            print("************************************************")
            print("************************************************")
            print('')
            print('')
            time.sleep(4)
            welcomeGUI()

        else:
            print("")
            print("���벻�Ϸ�,������!")
            print("")
    

def guiInputPath():

    print("***********************************************")
    print("����ļ��ڱ�Ŀ¼��output�ļ�����")
    print("ע�⣬������·���������������patch_abc�ļ������localtext.json��������patch_abc/localtext.json")
    print("�����Ҳ����ļ�")
    print("***********************************************")
    
    while True:
        
        isrepeat = True
        print("�������ļ�·��������9�˳�:")
        path = sys.stdin.readline().strip('\n')
        
        if path == "9":
            print("")
            print("ллʹ�ã��ټ���")
            input("��enter���˳�")
            sys.exit(0)

        try:
            if path[-4:].lower() != "json":
                path += ".json"

            file = open("./" + path)
            isrepeat = False
            file.close()
        except:
            print("")
            print("�޷��ҵ���json����������ԣ�")
            print("")
            
            
        if isrepeat == False:
            time.sleep(1)
            guiMain("./" + path)
            break
    
def guiMain(inputpath):

    jp1 = JsonProcess(inputpath[2:])
    
    
    print("")
    print("")
    print("************************************************")
    print("�����ļ���" + inputpath[2:])
    print("�Ͻ��ֶ��޸Ļ��ƶ����ڲ������ļ�������")
    print("************************************************")

    while True:
        print("************************************************")
        print("1. ������id���������޸�id")
        print("2. ��������¼�ֵ--δ���")
        print("3. �޸����и�������ֵ--δ���")
        print("9. �˳�")
        print("************************************************")
        print("�������ļ���������9�˳�:")
        

        a = sys.stdin.readline().strip('\n')


        if a == "9":
            print("")
            print("ллʹ�ã��ټ���")
            input("��enter���˳�")
            sys.exit(0)

        elif a == "1":
            GeneralTool.mkDir("./output/process/" + inputpath[2:].split("/")[0])        
            startid = -1
            isrepeat = True
            time.sleep(0.5)
            print('')
            print("��������id...")
            while True:
                
                print("")
                startid = input("��������ʼid: ")
                try:
                    int(startid)
                    isrepeat = False
                except:
                    print("")
                    print("Υ�����룬�����ԣ�")
                    print("")
                if isrepeat == False:
                    print("")
                    break

            time.sleep(0.3)            
            print("��ʼidΪ: " + str(startid))
            print("��ʼ�޸�...")
            jp1.processId(startid)
            print("��������")
            print("��������output�ļ���")
            print("")
            print("************************************************")
            print("************************************************")
            print("�Ҹ棺json�ǲ�������ע�͵ģ��Ұ���ɾ�ˣ���Ҫ�������ϰ��")
            print('�Ҹ棺json�ļ��Ľ�β�ǲ������ж��ŵģ�ϣ��ע��')
            print("************************************************")
            print("************************************************")
            print('')
            print
            time.sleep(4)
            welcomeGUI()
            break
        
        elif a == "2" or a == "3":
            print("�����У������ڴ���")
            print("")
            print("")
        else:
            print("���벻�Ϸ��������ԣ�")
            print("")
            print("")
            

if __name__ == '__main__':
    
    log_path = './Logs/'

    GeneralTool.mkDir("./output/")
    GeneralTool.mkDir(log_path)

    # ��־�ļ������ճ�������ʱ������
    sys.stdout = Logger(stream=sys.stdout)
    sys.stderr = Logger(stream=sys.stdout)
    
    welcomeGUI()
        
    
    
    