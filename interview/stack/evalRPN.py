#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/2 0002 17:09
# @Author  : Aisonk
# @Function    : 后缀表达式计算（）
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        compute = ['+', '-', '*', '/']
        stack = []
        for data in tokens:
            if data not in compute:
                stack.append(data)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                temp = eval(str(num1)+data+str(num2))
                stack.append(str(int(temp)))
        return stack[-1]
s = Solution()
nums = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(s.evalRPN(nums))