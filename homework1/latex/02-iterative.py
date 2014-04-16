#!/usr/bin/env python

import time;

def iterative(base, exp):
  if exp == 0:
    return 1;
  
  product = base;
  for i in range(1, exp):
    product *= base;
  return product;

if __name__ == "__main__":
  print("Exponent\tIterative");

  for x in range(0, 10001, 1000):
    start = time.time();
    iterative(3, x);
    end = time.time();
    
    print("%i\t%g" % (x, end - start));