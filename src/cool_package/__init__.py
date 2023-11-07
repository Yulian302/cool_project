import os
import sys

__all__ = ['module1']

is_sys_x64 = sys.maxsize > 2 ** 32

print('Your system is ', 'x64' if is_sys_x64 else 'x32')
