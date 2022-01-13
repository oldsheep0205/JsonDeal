# coding=gbk
import json
import re
import os


comment_re = re.compile(
    '(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?',
    re.DOTALL | re.MULTILINE
)

class GeneralTool:
    '''
    tools
    '''

    @staticmethod
    def parse_json(filename): #return[status, content] test whether to skip
        """ Parse a JSON file
            First remove comments and then use the json module package
            Comments look like :
                // ...
            or
                /*
                ...
                */
        """
        print("[����]�����淶��Ϊ")
        content = ''
        try:
            with open(filename, "r", encoding='UTF-8-sig') as f:
                content = ''.join(f.readlines())
                ## Looking for comments

        except UnicodeDecodeError:
            with open(filename, "r") as f:
                content = ''.join(f.readlines())
                ## Looking for comments
                
        finally:
            match = comment_re.search(content)
            while match:
                # single line comment
                content = content[:match.start()] + content[match.end():]
                match = comment_re.search(content)
            # Return json file

        
        
        try:
            content = GeneralTool.detectComma(content)
            content = GeneralTool.checkTrash(content, ',', '}')
            

        except:
            print('')
            print("������λmod���ߣ����ϷŸ���json�ļ�����ͷ�������ɶ��")
            print('')
            return [False, json.loads(content)]

        print('[����]������ɣ�')
        print('')
        try:
            return [True, json.loads(content, strict=False)]

        except json.decoder.JSONDecodeError:
            decoded_data=content.encode().decode('utf-8-sig') 
            return [True, json.loads(decoded_data, strict=False)]

    @staticmethod
    def mkDir(input1):
        """
        create output folder
        """

        folder = os.path.exists(input1)

        if not folder:
            os.mkdir(input1)

    @staticmethod
    def detectComma(input1):
        output = "["
        
        scoor = ecoor = 0
        for i in range(len(input1)):
            
            if input1[i] == '{':
                scoor = i
            elif input1[i] == '}':
                ecoor = i
    
            if scoor != 0 and ecoor != 0:
                output += (GeneralTool.checkTrash(input1[scoor:ecoor+1], ',', ':')) + ','
                scoor = ecoor = 0
                
        return output[:-1] + ']'

    @staticmethod
    def checkTrash(content, anchor1, anchor2):
        
        cutcoor = 0
        stacklist = []

        for i in range(-1, -9999, -1):
    
                stacklist.append(content[i])
                if content[i] == anchor1:
                    stacklist.pop()
                    
                if content[i] == anchor2:
                    cutcoor = i
                    break
    
        out = content[:cutcoor]    
        while len(stacklist) != 0:
            out += stacklist.pop()

        return out