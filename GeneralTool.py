# coding=gbk
import json
import re
import os
import ast
import demjson


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
        
        print("[操作]清理不规范行为")
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
            content = GeneralTool.checkTrash(content, ',', '}')

        except:
            print('')
            print("敢问这位mod作者，您老放个空json文件在里头，是想干啥？")
            print('')
            return [False, json.loads(content)]

        

        content = GeneralTool.delTrashComma(content)
        content = json.dumps(content,indent=2, ensure_ascii = False)
        
        print(content)
        try:
            return [True, json.loads(content, strict=False)]

        except json.decoder.JSONDecodeError:
            decoded_data=content.encode().decode('utf-8-sig') 
            return [True, json.loads(decoded_data, strict=False)]
        """
        
        content = ''
        output = ""
        try:
            with open(filename, "r", encoding='UTF-8-sig') as f:

                content = ''.join(f.readlines())
                output = demjson.decode(content)
                ## Looking for comments

        except:
            with open(filename, "r") as f:
                content = ''.join(f.readlines())
                output = demjson.decode(content)

        if len(output) == 0:
            print('')
            print("敢问这位mod作者，您老放个空json文件在里头，是想干啥？")
            print('')
            return [False, output]


        return [True, output]



    @staticmethod
    def mkDir(input1):
        """
        create output folder
        """

        folder = os.path.exists(input1)

        if not folder:
            os.mkdir(input1)

    @staticmethod
    def delTrashComma(input1):
        out = ''
        try:
            out = ast.literal_eval(input1)
        except:
            for i in range(1, 100):
                if input1[i] == '[':
                    out = input1[i:]

            for i in range(-1, -100, -1):
                if out[i] == ']':
                    out = out[:i-1]
            out = ast.literal_eval(out)

        return ast.literal_eval(out)
        
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