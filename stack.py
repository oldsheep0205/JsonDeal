# coding=gbk
from typing import List
class MyStack:
    '''
    helper class
    '''
    _stack: List


    def __init__(self):
        '''
        Constructor
        '''
        self._stack = []

    def push(self, input1):

        self._stack.append(input1)
        print("推入 " + str(input1))

    def pop(self):
        self._stack.pop()

    def isEmpty(self) -> bool:
        return len(self._stack) == 0

    def checkIn(self, input1) -> bool:

        if self.isEmpty():
            return False
        return input1 // 10 in self._stack
    
    def checkGap(self, input1) -> int:

        if self.isEmpty():
            return False
        return len(self._stack) - 1 - self._stack.index(input1 // 10) 
    
    def checkClear(self):
        if len(self._stack) > 50:
            self._stack.clear()
        