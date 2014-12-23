#!/usr/bin/env python

import os;
import itertools;

def calc_cost(cost_matrix, permutation):
  cost = 0;

  for x in xrange(len(permutation)):
    cost += cost_matrix[x][permutation[x]];

  print "... %i -> %s" % (cost, str(permutation));

  return cost;

def brute_force(cost_matrix):
  best_permutation = None;
  best_cost = 9999;

  for permutation in itertools.permutations(xrange(len(cost_matrix))):
    cost = calc_cost(cost_matrix, permutation);
    if cost < best_cost:
      best_cost = cost;
      best_permutation = permutation;

  return best_cost, best_permutation;

def powerset(iterable):
    s = list(iterable);
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1));

def expanding_assignment(cost_matrix, assignments = None, cost = 0):

  if assignments is None:
    assignments = [];

  # figure out the best/earliest assignment
  best_cost = None;
  best_index = None;

  row = cost_matrix[len(assignments)];

  for current_index in xrange(len(row)):
    if current_index in assignments:
      continue;

    current_cost = row[current_index];
    if best_cost is None or current_cost < best_cost:
      best_cost = current_cost;
      best_index = current_index;

  cost += best_cost;
  assignments.append(best_index);

  # make the recursive call
  if len(assignments) < len(cost_matrix):
    cost, ignored = expanding_assignment(cost_matrix, assignments, cost);

  return cost, assignments;

if __name__ == '__main__':

  people = ['Mother', 'Father', 'Daughter', 'Son'];
  rooms  = ['Den', 'Kitchen', 'Basement', 'Bathroom'];

  cost_matrix = [
    [ 9, 2, 11, 8],
    [13, 3,  9, 7],
    [15, 5, 12, 6],
    [14, 8,  2, 9]
  ];

  cost, permutation = brute_force(cost_matrix);

  print "BRUTE FORCE";
  for x in xrange(len(people)):
    print "  %s -> %s" % (people[x], rooms[permutation[x]]);

  print "  %i -> %s" % (cost, str(permutation));

  cost, permutation = expanding_assignment(cost_matrix);

  print "EXPANDING ASSIGNMENT";
  for x in xrange(len(people)):
    print "  %s -> %s" % (people[x], rooms[permutation[x]]);

  print "  %i -> %s" % (cost, str(permutation));
