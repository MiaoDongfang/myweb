import datetime
import re
def _static_file_generator(fpath):
    BLOCK_SIZE=8192
    with open(fpath,'rb') as f:
        block=f.read(BLOCK_SIZE)
        while block:
            yield block
            block=f.read(BLOCK_SIZE)

fpath='D:/study/python/awesome-python-webapp/www/models.py'
print _static_file_generator(fpath)

print datetime.timedelta(hours=8,minutes=0)

_RE_TZ=re.compile(r'^([\+\-])([0-9]{1,2})(\:)([0-9]{1,2})')

mt=_RE_TZ.match("+8:00")
print mt.group(1)
print mt.group(2)
print mt.group(3)
