#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 0006 13:03
# @Author  : Aisonk
# @Function    : 电话号码的字母组合
class Solution(object):
    def letterCombinations(self, digits):
        """
        输入：digits = "23"
        输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
        :type digits: str
        :rtype: List[str]
        """
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        path = []
        if len(digits) == 0:
            return []
        self.backtrack(digits, 0, res, path, mapping)
        return res

    def backtrack(self, digits, digits_index, res, path, mapping):
        if len(path) == len(digits):
            res.append(''.join(path))
            return
        letter = mapping[digits[digits_index]]
        for lt in letter:
            path.append(lt)
            self.backtrack(digits, digits_index+1, res, path, mapping)
            path.pop()

s = Solution()
digits = '234'
print(s.letterCombinations(digits))