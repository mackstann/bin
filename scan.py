from __future__ import print_function

import datetime
import os
import shutil
import subprocess


destdir = os.getcwd()
os.chdir('/tmp')

letter = '-x 215.88 -y 279.374'.split()
legal = '-x 215.88 -y 355.567'.split()
size = None
while size is None:
    print("Paper size?")
    print("[1] Letter (Default)")
    print("[2] Legal")
    s = raw_input("> ").strip()
    if s in ('1', ''):
        size = letter
        print('OK, Letter.')
    elif s == '2':
        size = legal
        print('OK, Legal.')

print()

print("Scanning...")
proc = subprocess.Popen(['scanimage'] + size + ['--resolution', '300'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print()

default_filename = 'Scanned at ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = None
filename = raw_input("Filename (without extension)? [{}] ".format(default_filename)).strip()
if filename == '':
    filename = default_filename
parts = filename.split()
if len(parts) == 3 and all(map(str.isdigit, parts)):
    y, m, d = map(int, parts)
    if y < 50:
        y += 2000
    elif y < 1990 or y > 2050:
        print("Unknown year? {}".format(y))
        raise SystemExit(1)
    filename = "{:04d}-{:02d}-{:02d}".format(y, m, d)
    print("Recognized date as: {}".format(filename))


print("Waiting for scan to complete...")
data, stderr = proc.communicate()

real_errors = [ line for line in stderr.splitlines() if line.strip() and 'rounded value' not in line ]
if real_errors:
    print('convert failed')
    print(stderr)
    raise SystemExit(1)

with open(filename+'.pnm', 'wb') as f:
    f.write(data)
ret = subprocess.call(["convert", "-quality", "90", filename+'.pnm', filename+'.jpg'])
if ret:
    raise SystemExit(ret)
os.unlink(filename+'.pnm')


final_filename_unique = final_filename = os.path.join(destdir, filename+'.jpg')
i = 0
while os.path.exists(final_filename_unique):
    i += 1
    final_filename_unique = "{} ({}).jpg".format(
        final_filename.rsplit('.', 1)[0], i)

shutil.copyfile(filename+'.jpg', final_filename_unique)
os.unlink(filename+'.jpg')
print("Saved to {}".format(final_filename_unique.split('/')[-1]))

subprocess.call(["eog", final_filename_unique])
