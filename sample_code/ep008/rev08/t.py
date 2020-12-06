#!/usr/bin/env python2
import time


class C:
    pass


while True:
    try:
        print('zzz')
        raise C()
    except BaseException:
        print('got BaseException')
        raise
    except:
        print('some other error happened!')
        raise
