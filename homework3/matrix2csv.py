#!/usr/bin/env python

import sys;

def ReadFile(file):
  f = open(file, 'r');
  lines = f.readlines();
  f.close();
  arrs = [];
  for line in lines:
    arr = [];
    for token in line.split(','):
      if len(token) > 0:
        arr.append(int(token));
    arrs.append(arr);
  return arrs;

def WriteFile(file, arr):
  f = open(file, "w");
  f.write(" ".join(str(x) for x in arr));
  f.close();

if __name__ == '__main__':

  if len(sys.argv) == 1:
    print "please provide an input file";
    sys.exit(0);

  input_file = sys.argv[1];

  data = ReadFile(input_file);

  for i in xrange(len(data)):
    sys.stdout.write(str(i));
    for j in xrange(len(data[i])):
      if data[i][j] == 1:
        sys.stdout.write(";" + str(j));
    sys.stdout.write("\n");
