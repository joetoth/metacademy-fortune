import os
import sys
from os import listdir
from os.path import isfile, join
from subprocess import call

def generate():
  fortune = ''
  dir = 'metacademy-content/concepts'
  for f in listdir('metacademy-content/concepts'):
    tfile = os.path.join(dir, f, 'title.txt')
    sfile = os.path.join(dir, f, 'summary.txt')
    if os.path.exists(tfile):
      with open(tfile, 'r') as t:
        title = t.read().strip().upper()
    if os.path.exists(sfile):
      with open(sfile, 'r') as s:
        summary = s.read().strip()
    fortune += '{}: {}\nhttps://metacademy.org/graphs/concepts/{}\n%\n'.format(title, summary, f)

  with open('metacademy-fortune', 'w') as f:
    f.write(fortune)

  call(['strfile', 'metacademy-fortune', 'metacademy-fortune.dat'])


if __name__ == "__main__":
  generate()

