# coding=gbk
'''
Created on 2022.1.8

@author: 红尘
'''

from JsonProcess import JsonProcess
import time
import sys
from JsonUpdate import JsonUpdate
from GeneralTool import GeneralTool
from Logger import Logger

_VERSION = "v2.6"
_NAME = "鬼谷八荒json多功能批量处理器"
_WEBSITE = "https://bbs.3dmgame.com/thread-6254819-1-1.html"


def welcomeGUI():

    print("************************************************")
    print(_NAME+ ' ' + _VERSION)
    print("作者:红尘")
    print("QQ: 93633818")
    print("QQ群: 995876973")
    print("b站id: 爱喝白酒的红尘")
    print("3dm帖子指路：" + _WEBSITE)
    print("鸣谢：如风，昊天 对本工具作出的杰出贡献")
    print("************************************************")
    print("请将此文件放入vallain文件夹下，与base文件夹和patch_文件同级！！！！！")
    print("请将此文件放入vallain文件夹下，与base文件夹和patch_文件同级！！！！！")
    print("请将此文件放入vallain文件夹下，与base文件夹和patch_文件同级！！！！！")
    print("************************************************")
    print("")
    print("1. 单独json操作")
    print("2. mod适配新版本")
    print("9. 退出")
    print("")

    while True:
        
        print("请选择: ")
        choose = sys.stdin.readline().strip('\n')
        
        if choose == "9":
            print("")
            print("谢谢使用，再见！")
            input("按enter键退出")
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
            print("操作结束")
            print("输出结果在output文件夹下的update文件夹")
            print("")
            print("************************************************")
            print("************************************************")
            print("忠告：json是不允许有注释的，我帮你删了，不要养成这个习惯")
            print('忠告：json文件的结尾是不允许有逗号的，希望注意')
            print("若真的对注释心有执念，可以在源文件对照查看")
            print("************************************************")
            print("************************************************")
            print('')
            print('')
            time.sleep(4)
            welcomeGUI()

        else:
            print("")
            print("输入不合法,请重试!")
            print("")
    

def guiInputPath():

    print("***********************************************")
    print("输出文件在本目录的output文件夹中")
    print("注意，是输入路径。比如你想更改patch_abc文件夹里的localtext.json，就输入patch_abc/localtext.json")
    print("否则找不到文件")
    print("***********************************************")
    
    while True:
        
        isrepeat = True
        print("请输入文件路径或输入9退出:")
        path = sys.stdin.readline().strip('\n')
        
        if path == "9":
            print("")
            print("谢谢使用，再见！")
            input("按enter键退出")
            sys.exit(0)

        try:
            if path[-4:].lower() != "json":
                path += ".json"

            file = open("./" + path)
            isrepeat = False
            file.close()
        except:
            print("")
            print("无法找到此json，请检查后重试！")
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
    print("操作文件：" + inputpath[2:])
    print("严禁手动修改或移动正在操作的文件！！！")
    print("************************************************")

    while True:
        print("************************************************")
        print("1. 按给定id依次重新修改id")
        print("2. 批量添加新键值--未完成")
        print("3. 修改所有给定键的值--未完成")
        print("9. 退出")
        print("************************************************")
        print("请输入文件名或输入9退出:")
        

        a = sys.stdin.readline().strip('\n')


        if a == "9":
            print("")
            print("谢谢使用，再见！")
            input("按enter键退出")
            sys.exit(0)

        elif a == "1":
            GeneralTool.mkDir("./output/process/" + inputpath[2:].split("/")[0])        
            startid = -1
            isrepeat = True
            time.sleep(0.5)
            print('')
            print("正在重修id...")
            while True:
                
                print("")
                startid = input("请输入起始id: ")
                try:
                    int(startid)
                    isrepeat = False
                except:
                    print("")
                    print("违规输入，请重试！")
                    print("")
                if isrepeat == False:
                    print("")
                    break

            time.sleep(0.3)            
            print("起始id为: " + str(startid))
            print("开始修改...")
            jp1.processId(startid)
            print("操作结束")
            print("输出结果在output文件夹")
            print("")
            print("************************************************")
            print("************************************************")
            print("忠告：json是不允许有注释的，我帮你删了，不要养成这个习惯")
            print('忠告：json文件的结尾是不允许有逗号的，希望注意')
            print("************************************************")
            print("************************************************")
            print('')
            print
            time.sleep(4)
            welcomeGUI()
            break
        
        elif a == "2" or a == "3":
            print("开发中，敬请期待！")
            print("")
            print("")
        else:
            print("输入不合法，请重试！")
            print("")
            print("")
            

if __name__ == '__main__':
    
    log_path = './Logs/'

    GeneralTool.mkDir("./output/")
    GeneralTool.mkDir(log_path)

    # 日志文件名按照程序运行时间设置
    sys.stdout = Logger(stream=sys.stdout)
    sys.stderr = Logger(stream=sys.stdout)
    
    welcomeGUI()
        
    
    
    