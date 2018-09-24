import os
import sys
print("CPU:{}".format(os.cpu_count()),end=',')
print("RECLIMIT:{}".format(sys.getrecursionlimit()),end=',')
print("EXEPATH:{}".format(sys.executable),end=',')
print("ENDIAN:{}".format(sys.byteorder),end=',')
print("UNICODE:{}".format(sys.maxunicode))
