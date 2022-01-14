# coding=gbk
import sys
import os
import time


# ����̨�����¼���ļ�
class Logger(object):
    def __init__(self, file_name="Default.log", stream=sys.stdout):

        self.terminal = stream
        log_path = './Logs/'
        log_file_name = log_path + 'log-' + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '.log'
        self.log = open(log_file_name, "a")
        
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


if __name__ == '__main__':
    # �Զ���Ŀ¼�����־�ļ�
    log_path = './Logs/'
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    # ��־�ļ������ճ�������ʱ������
    log_file_name = log_path + 'log-' + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '.log'
    # ��¼������ print ��Ϣ
    sys.stdout = Logger(log_file_name)
    # ��¼ traceback �쳣��Ϣ
    sys.stderr = Logger(log_file_name)
    
    sys.stdout = Logger(stream=sys.stdout)

    print(5555)
    print(2/0)
