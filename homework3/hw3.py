#!/usr/bin/env python

import sys;
import time;

sys.setrecursionlimit(200000);

class Graph:
    def __init__(self, num_vertices = 0):
        self.p = [[0 for x in range(num_vertices)] for x in range(num_vertices)];

    def is_edge(self, i, j):
        return self.p[i][j] != 0;

    def get_adjacent(self, i):
        return [x for x in xrange(self.num_nodes()) if self.p[i][x] != 0];

    def set_edge(self, i, j, value):
        self.p[i][j] = value;

    def num_nodes(self):
        return len(self.p[0]);

    def __str__(self):
        return str(self.p);

def DFS(graph, vertex = 0, visited = None, depth = -1, is_iterative = False):

    if visited is None:
        visited = [False for x in xrange(graph.num_nodes())];

    if not visited[vertex]:
        visited[vertex] = True;
        sys.stdout.write(str(vertex) + " ");
        sys.stdout.flush();

    for w in graph.get_adjacent(vertex):
        if w is vertex:
            continue;
        if depth != 0 and (is_iterative or not visited[w]):
            DFS(graph, w, visited, depth - 1, is_iterative);

def IDS(graph):

    visited = [False for x in xrange(graph.num_nodes())];

    for depth in xrange(graph.num_nodes()):
        if all(visited):
            break;
        DFS(graph, 0, visited, depth, True);

def IDFS(graph, vertex = 0, visited = None, depth = -1):

    if visited is None:
        visited = [False for x in range(graph.num_nodes())];

    if not visited[vertex]:
        visited[vertex] = True;
        sys.stdout.write(str(vertex) + " ");
        sys.stdout.flush();

    remembered_vertices = [];

    for w in graph.get_adjacent(vertex):
        if w is vertex:
            continue;
        if depth != 0:
            remembered_vertices.extend(IDFS(graph, w, visited, depth - 1));
        elif not visited[w]:
            remembered_vertices.append(w);

    return remembered_vertices;

def IIDS(graph, vertex = 0):

    visited = [False for x in range(graph.num_nodes())];

    remembered_vertices = [vertex];

    if not all(visited):
        while len(remembered_vertices) > 0:
            remembered_vertices.extend(IDFS(graph, remembered_vertices.pop(0), visited, 0));
            remembered_vertices = unique(remembered_vertices);

def BFS(graph, vertex = 0):

    visited = [False for x in xrange(graph.num_nodes())];

    queue = [vertex];

    while len(queue) > 0:

        vertex = queue.pop(0);

        visited[vertex] = True;
        sys.stdout.write(str(vertex) + " ");
        sys.stdout.flush();

        for w in graph.get_adjacent(vertex):
            if not visited[w] and w is not vertex:
                queue.append(w);
                queue = unique(queue);

def unique(seq):
    return list(_unique(seq));

def _unique(seq):
    seen = set();
    for x in seq:
        if x in seen:
            continue;
        seen.add(x);
        yield x;

def read_file(file):
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

    do_dfs = False;
    do_bfs = False;
    do_ids = False;
    do_iids = False;
    input_file = 'input.txt';

    if len(sys.argv) == 1:
        print "Usage: %s [-dfs] [-bfs] [-ids] [-iids] [-v] [-v] input_file" % (sys.argv[0]);
        sys.exit(0);

    for i in xrange(1, len(sys.argv)):
        arg = sys.argv[i];
        if arg == "-dfs":
            do_dfs = True;
        elif arg == "-bfs":
            do_bfs = True;
        elif arg == "-ids":
            do_ids = True;
        elif arg == "-iids":
            do_iids = True;
        elif arg == "--all":
            do_dfs = True;
            do_bfs = True;
            do_ids = True;
            do_iids = True;
        elif arg == "-v":
            if VERBOSE:
                VVERBOSE = True;
            else:
                VERBOSE = True;
        else:
            input_file = arg;

    data = read_file(input_file);

    num_vertices = len(data[0]);
    g = Graph(num_vertices);

    for i in xrange(num_vertices):
        for j in xrange(num_vertices):
            g.set_edge(i, j, data[i][j]);

    if do_dfs:
        start_time = time.time();
        sys.stdout.write("DFS\n");
        DFS(g);
        end_time = time.time();
        print("\n DFS Time: %g" % (end_time - start_time));
        sys.stdout.flush();

    if do_bfs:
        start_time = time.time();
        sys.stdout.write("BFS\n");
        BFS(g);
        end_time = time.time();
        print("\n BFS Time: %g" % (end_time - start_time));
        sys.stdout.flush();

    if do_ids:
        start_time = time.time();
        sys.stdout.write("IDS\n");
        IDS(g);
        end_time = time.time();
        print("\n IDS Time: %g" % (end_time - start_time));
        sys.stdout.flush();

    if do_iids:
        start_time = time.time();
        sys.stdout.write("IIDS\n");
        IIDS(g);
        end_time = time.time();
        print("\nIIDS Time: %g" % (end_time - start_time));
        sys.stdout.flush();
