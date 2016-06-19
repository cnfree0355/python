#!/usr/bin/env python
import os
import time
source = [ '/opt/rh/','aa.txt']
target_dir = '/opt/'
target = target_dir + time.strftime('%Y%m%d-%H%M%S')+'.zip'
zip_command = "zip -qr '%s' '%s'" % (target,''.join(source))
if os.system(zip_command) == 0:
  print "sucessful backup to",target
else:
  print 'Backup Failed'

