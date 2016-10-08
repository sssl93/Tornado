#!/usr/bin/env python
# -*- coding:utf-8 -*-
def w1(func):
    def inner(*args,**kwargs):
        print '# 验证1'
        func(*args,**kwargs)
        print '# 验证2'
        func(*args,**kwargs)
        print '# 验证3'
        return func(*args,**kwargs)
    return inner

def w2(func):
    def inner(*args,**kwargs):
        print '# 验证4'
        print '# 验证5'
        func(*args,**kwargs)
        print '# 验证6'
        return func(*args,**kwargs)
    return inner


@w1
@w2
def f1(arg1,arg2,arg3):
    print 'f1'
f1(1,2,3)