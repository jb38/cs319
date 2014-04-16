#!/usr/bin/env python

import time;

def recursive(base, exp):
  if exp == 0:
    return 1;
  
  if exp > 1:
    return base * recursive(base, exp - 1);
  else:
    return base;

if __name__ == "__main__":
  print("Exponent\tRecursive");

  for x in range(0, 10001, 1000):
    start = time.time();
    recursive(3, x);
    end = time.time();
    
    print("%i\t%g" % (x, end - start));