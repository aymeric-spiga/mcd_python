#!/bin/bash

# This script will delete all /home/marshttp/www-mars/mcd_python/img/* files
# which have not been accessed in more than 'age' days or
# which are larger than 'size' bytes.  It is designed to
# be run by a nightly cron job.

age=5 # days
filesize=100000 # bytes

# 1. Keep a trace of the 'img' directory contents
touch /home/marshttp/www-mars/mcd_python/mcd_stats
cp -f /home/marshttp/www-mars/mcd_python/mcd_stats  /home/marshttp/www-mars/mcd_python/mcd_stats.tmp
ls -lt --sort=time /home/marshttp/www-mars/mcd_python/img | cut -c 39- >> /home/marshttp/www-mars/mcd_python/mcd_stats.tmp
sort -r /home/marshttp/www-mars/mcd_python/mcd_stats.tmp > /home/marshttp/www-mars/mcd_python/mcd_stats.tmp2
uniq /home/marshttp/www-mars/mcd_python/mcd_stats.tmp2 /home/marshttp/www-mars/mcd_python/mcd_stats
rm -f /home/marshttp/www-mars/mcd_python/mcd_stats.tmp /home/marshttp/www-mars/mcd_python/mcd_stats.tmp2

# 2. Cleanup img directory

find /home/marshttp/www-mars/mcd_python/img/ -atime +${age} -exec rm {} \;
find /home/marshttp/www-mars/mcd_python/img/ -size +${filesize} -exec rm {} \;

