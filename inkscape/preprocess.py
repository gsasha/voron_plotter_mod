import re
import sys
for line in sys.stdin.readlines():
  line = re.sub('\(([^\)]+)\)', '; \\1', line)
  line = re.sub('G0(\d)', 'G\\1', line)
  line = re.sub('([XYZIJF]) ([0-9\-\.]+)', '\\1\\2', line)
  print(line,end='')
