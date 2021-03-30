# art forked from https://gist.github.com/yuanqing/ffa2244bd134f911d365#file-gistfile2-txt

import datetime
import time
import os
art = """
000000
00  00
00  00
00  00
000000
*
1111
  11
  11
  11
111111
*
222222
    22
222222
22
222222
*
333333
    33
333333
    33
333333
*
44  44
44  44
444444
    44
    44
*
555555
55
555555
    55
555555
*
666666
66
666666
66  66
666666
*
777777
    77
    77
    77
    77
*
888888
88  88
888888
88  88
888888
*
999999
99  99
999999
    99
999999
*
@@
@@

@@
@@
"""


class TimePrinter:
    def __init__(self) -> None:
        self.digits = [i.strip('\n') for i in art.split('*')]

    def print_time(self, hh, mm, ss):
        hhmmss = str(hh)+':'+str(mm)+':'+str(ss)
        timedigits = []
        for i in hhmmss:
            if i != ':':
                timedigits.append(self.digits[int(i)])
            else:
                timedigits.append(self.digits[10])

        lines = ['']*5
        for i in timedigits:
            i = i.split('\n')
            for j in range(5):
                lines[j] += i[j]+'\t'
        for line in lines:
            print(line, flush=True)


if __name__ == '__main__':
    tp = TimePrinter()
    while True:
        os.system('cls')
        timenow = datetime.datetime.now().strftime('%H%M%S')
        tp.print_time(timenow[0:2], timenow[2:4], timenow[4:6])
        time.sleep(1)
