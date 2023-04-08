#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/4 0004 23:28
# @Author  : Aisonk
# @Function    :
# !encoding=utf8
def ip_add_func(ip: str):
    ip_list = ip.split('.')
    for i in range(len(ip_list) - 1, -1, -1):
        if int(ip_list[i]) < 255:
            ip_list[i] = str(int(ip_list[i]) + 1)
            return '.'.join(ip_list)
        else:
            ip_list[i] = '0'
    return "非法ip"


if __name__ == '__main__':
    # ip = '0.0.0.0'
    ip = '0.0.1.251'
    # ip = '255.255.255.0'
    # ip = '255.255.255.254'
    # ip = '10.10.0.254'
    # ip = '255.255.255.255'
    print(ip_add_func(ip))
