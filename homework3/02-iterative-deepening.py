#!/usr/bin/env python

class Graph:
  def __init__(self, num_vertices = 0):
    self.p = [[0 for x in xrange(num_vertices)] for x in xrange(num_vertices)];

  def is_edge(self, i, j):
    return self.p[i][j] != 0;

  def set_edge(self, i, j, value):
    self.p[i][j] = value;

  def num_nodes(self):
    return len(self.p[0]);

  def __str__(self):
    return str(self.p);

def IDS(graph, vertex, depth = 2, visited = None):

  if visited is None:
    visited = [False for x in xrange(graph.num_nodes())];

  visited[vertex] = True;

  print str(vertex),

  queue = [];

  for w in xrange(g.num_nodes()):
    if w is vertex:
      continue;
    if g.is_edge(vertex, w) and not visited[w]:
      if depth > 0:
        IDS(graph, w, depth - 1, visited);
      else:
        queue.append(w);

  for w in queue:
    IDS(graph, w, 2, visited);

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

if __name__ == '__main__':
  # read the input
  data = ReadFile('input.txt');
  # create the data structure
  num_vertices = len(data[0]);
  g = Graph(num_vertices);
  # populate the graph
  for i in xrange(num_vertices):
    for j in xrange(num_vertices):
      g.set_edge(i, j, data[i][j]);
  # perform the DFS
  IDS(g, 0);
