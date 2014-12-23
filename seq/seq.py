#!/usr/bin/env python

# Jim Blaney
# Hood College
# 2 May 2014
# CS 319 - Algorithm Analysis

# Problem: You are given an array, A, of real numbers. Find the set, T,
#          of contiguous numbers in A that provide the maximum sum. The
#          set T must contain at least one number.

import os;

# find the positive difference between the values of a list
# the returned list will be one element shorter than the input
def pos_deltas(sequence):
  deltas = [];

  for i in xrange(len(sequence) - 1):
    deltas.append(abs(sequence[i] - sequence[i + 1]));

  return deltas;

# returns a list of two-element lists -- the start and end
# indexes of contiguous "parity groups"
def split_parity_groups(deltas):
  splits = [];

  last_parity = deltas[0] % 2;
  start = 0;

  for i in xrange(len(deltas)):
    current_parity = deltas[i] % 2;
    if current_parity is not last_parity:
      splits.append([start, i - 1]);
      last_parity = current_parity;
      start = i;

  splits.append([start, len(deltas) - 1]);

  return splits;

# assembles lists that correlate with the second-degree
# delta indexes
def resolve_splits(seq, splits):
  sequences = [];

  for split in splits:
    mn = split[0];
    mx = split[1] + 4;
    sequences.append(seq[mn:mx]);

  return sequences;

# removes leading and tailing values that are negative so that
# the first and last elements in the list are non-negative
def reduce_seqs(seqs):
  sequences = [];

  for seq in seqs:
    while len(seq) > 1 and seq[0] < 0:
      seq = seq[1:];
    while len(seq) > 1 and seq[-1] < 0:
      seq = seq[:-1];
    if len(seq) > 0:
      sequences.append(seq);

  return sequences;

# sums up a list of lists of numbers
def seq_sums(s):
  sums = [];

  for seq in s:
    sums.append(sum(seq));

  return sums;

def kadane_max_subarray_sum(A):
  max_ending_here = max_so_far = A[0];
  for x in A[1:]:
    max_ending_here = max(x, max_ending_here + x);
    max_so_far = max(max_so_far, max_ending_here);
  return max_so_far;

def random_sequence(lower, upper, length):
  seq = [];
  range = upper - lower;
  for i in xrange(length):
    seq.append(int(os.urandom(4).encode('hex'), 16) % range + lower);
  return seq;

def run_test(lower, upper, length):

  seq = random_sequence(lower, upper, length);
  # seq = [-10,-2,8,-5,7,10,2,5,9,-8,3,-1,0,-6,1,6,4];
  # seq = [
  #         4,  10,   5,   8,  -4,  -3,   3,   2, -10,  -9,
  #        -1,   6,   0,   1,  -8,   7,  -7,  -2,  -5,   9,
  #        -6,  -7,   5,  10,  -9,   6,  -4,  -3,  -5,   1,
  #         3,  -1,   7,  -2,   9,   2,   0,   4,   8, -10,
  #        -6,  -8,   2,  -9,  -6,   3, -10,   9,  -7,   0,
  #         4,  -1,   8,  -4,   5,  -5,  -3,   7,  -8,   1
  #       ];

  seqs = reduce_seqs(                # 5. head/tail should be non-negative
          resolve_splits(            # 4. construct parity sequences
            seq,
            split_parity_groups(     # 3. split by parity
              pos_deltas(            # 2. second-degree deltas
                pos_deltas(seq))))); # 1. first-degree deltas

  sums = seq_sums(seqs);             # 6. calculate sums

  max_index = max(enumerate(sums), key = lambda x: x[1])[0]; # 7. compare sums

  # print seq;
  #
  # for i in xrange(len(seqs)):        # 8. report findings
  #   if i is max_index:
  #     print "*",
  #   else:
  #     print " ",
  #   print str(seqs[i]) + " -> " + str(sums[i]);

  # 9. check against the known best solution
  max_sum = kadane_max_subarray_sum(seq);

  if sums[max_index] is max_sum:
    # print "Kadane's algorithm confirms";
    return True;
  else:
    # print "Kadane's algorithm differs (%i)" % (max_sum);
    return False;


if __name__ == '__main__':

  results = [];

  for i in range(100):
    results.append(run_test(-50, 50, 1000));

  hits = sum(results);

  print hits;
