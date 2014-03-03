#!/usr/bin/env python

import os;
import sys;
import time;

sys.setrecursionlimit(20000);

class FirstPivotSelector():
    def GetPivot(self, theList, start, end):
        return start;
    def Name(self):
        return "First";

class LastPivotSelector():
    def GetPivot(self, theList, start, end):
        return end;
    def Name(self):
        return "Last";

class MiddlePivotSelector:
    def GetPivot(self, theList, start, end):
        return int((start + end) / 2);
    def Name(self):
        return "Middle";

class RandomPivotSelector:
    def GetPivot(self, theList, start, end):
        random_int = int(os.urandom(4).encode('hex'), 16);
        random_int %= (end - start);
        random_int += start;
        return random_int;
    def Name(self):
        return "Random";

class MedianPivotSelector:
    def GetPivot(self, theList, start, end):
        mid = int((start + end) / 2)
        list = [theList[start], theList[mid], theList[end]];
        if (theList[start] > theList[mid]):
            if (theList[mid] > theList[end]):
                return mid;
            elif (theList[start] > theList[end]):
                return end;
            else:
                return start;
        else:
            if (theList[start] > theList[end]):
                return start;
            elif (theList[mid] > theList[end]):
                return end;
            else:
                return mid;
        return start;
    def Name(self):
        return "Median";
        
class Quicksort():
    def __init__(self, p):
        self.pivot_selector = p;

    def Sort(self, arr):
        less = [];
        pivot_list = [];
        more = [];
        if len(arr) <= 1:
            return arr;
        else:
            pivot_index = self.pivot_selector.GetPivot(arr, 0, len(arr) - 1);
            pivot = arr[pivot_index]
            for i in arr:
                if i < pivot:
                    less.append(i);
                elif i > pivot:
                    more.append(i);
                else:
                    pivot_list.append(i);
            less = self.Sort(less);
            more = self.Sort(more);
            return less + pivot_list + more;

def ReadFile(file):
    f = open(file, "r");
    content = f.readline();
    f.close();
    arr = [];
    for token in content.split(" "):
        if len(token) > 0:
            arr.append(int(token));
    return arr;

def WriteFile(file, arr):
    f = open(file, "w");
    f.write(" ".join(str(x) for x in arr));
    f.close();
        
if __name__ == "__main__":
    print "Count\tStrategy\tFormat\tTime";
    pivot_selectors = [
        FirstPivotSelector(),
        LastPivotSelector(),
        MiddlePivotSelector(),
        RandomPivotSelector(),
        RandomPivotSelector(),
        RandomPivotSelector(),
        RandomPivotSelector(),
        RandomPivotSelector(),
        MedianPivotSelector()
    ];
    for pivot_selector in pivot_selectors:
        count = 0;
        for f in sorted(os.listdir("data")):
            arr = ReadFile("data/" + f);
            q = Quicksort(pivot_selector);
            start_time = time.time();
            arr = q.Sort(arr);
            end_time = time.time();
            #print arr;
            #WriteFile("data-sorted/" + f, arr); #bootstrap for generating sorted files
            print("%i\t%s\tUnsorted\t%g" % (len(arr), pivot_selector.Name(), end_time - start_time));
        for f in sorted(os.listdir("data-sorted")):
            arr = ReadFile("data-sorted/" + f);
            q = Quicksort(pivot_selector);
            start_time = time.time();
            arr = q.Sort(arr);
            end_time = time.time();
            #print arr;
            print("%i*\t%s\tSorted\t%g" % (len(arr), pivot_selector.Name(), end_time - start_time));
    #a = Andy();
    #g = Quicksort(Andy());
    #g.Partition("lab on fire");
