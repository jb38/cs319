#!/usr/bin/env python

import sys, time;

def iterative(base, exp):
  if exp == 0:
    return 1;
  
  product = base;
  for i in range(1, exp):
    product *= base;
  return product;

def recursive(base, exp):
  if exp == 0:
    return 1;
  
  if exp > 1:
    return base * recursive(base, exp - 1);
  else:
    return base;

if __name__ == "__main__":
  sys.setrecursionlimit(10000);

  print("Exponent\tIterative\tRecursive");

  for x in range(10000):
    start_time_iterative = time.time();
    iterative(3, x);
    end_time_iterative = time.time();
    
    start_time_recursive = time.time();
    recursive(3, x);
    end_time_recursive = time.time();
    
    print("%i\t%g\t%g" % (x, end_time_iterative - start_time_iterative, end_time_recursive - start_time_recursive));
