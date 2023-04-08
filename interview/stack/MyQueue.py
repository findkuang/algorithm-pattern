#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/10 0010 19:47
# @Author  : Aisonk
# @Function    : 用两个栈实现一个队列
class MyQueue(object):

    def __init__(self):
        # 入栈
        self.stack_in = []
        # 出栈
        self.stack_out = []

    def push(self, x):
        """
        如果out_stack不为空，则将out_stack中的数据还原到in_stack中
        :type x: int
        :rtype: None
        """
        if self.stack_out:
            while self.stack_out:
                self.stack_in.append(self.stack_out.pop())
        return self.stack_in.append(x)

    def pop(self):
        """
        如果out_stack是空，则将in_stack中的数据加入到out_stack中
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self):
        """
        int peek() 返回队列开头的元素,但是不会删除头元素
        :rtype: int
        """
        # stack_out不为空返回最后一个；否则返回stack_in[0]
        if self.stack_out:
            return self.stack_out[-1]
        else:
            if self.stack_in:
                return self.stack_in[0]
            else:
                return None

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack_in and not self.stack_out:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()