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
        
class Quicksort():
    def __init__(self, p):
        self.pivot_selector = p;

    def Sort(self, theList, start, end):
        print "::Sort(%i -> %i)" % (start, end);
        print theList;
        
        if start < end:
            # partition the list
            pivot = self.Partition(theList, start, end);
            # sort both halves
            self.Sort(theList, start, pivot - 1);
            self.Sort(theList, pivot + 1, end);
        return theList;
        
    def Partition(self, theList, start, end):
        pivot_index = self.pivot_selector.GetPivot(theList, start, end);
        pivot = theList[pivot_index];
        
        print "::Partition(%i -> %i)" % (start, end);
        print theList;
        
        print "Pivot Index: %i (%i)" % (pivot_index, pivot);
        
        left = start + 1;
        right = end;
        done = False;

        while not done:
            while left <= right and theList[left] <= pivot:
                left += 1;

            while theList[right] >= pivot and right >=left:
                right -= 1;

            if right < left:
                done = True;
            else:
                # swap places
                temp = theList[left];
                theList[left] = theList[right];
                theList[right] = temp;

        # swap start with theList[right]
        temp = theList[start];
        theList[start] = theList[right];
        theList[right] = temp;

        print "Right: %i" % (right);
        
        return right;

def ReadFile(file):
    f = open(file, "r");
    content = f.readline();
    f.close();
    arr = [];
    for token in content.split(" "):
        if len(token) > 0:
            arr.append(int(token));
    return arr;
        
if __name__ == "__main__":
    print "Count\tStrategy\tTime";
    pivot_selectors = [
      FirstPivotSelector(),
      LastPivotSelector(),
      MiddlePivotSelector()
    ];
    for pivot_selector in pivot_selectors:
        for f in sorted(os.listdir("data")):
            arr = ReadFile("data/" + f);
            q = Quicksort(pivot_selector);
            start_time = time.time();
            q.Sort(arr, 0, len(arr) - 1);
            end_time = time.time();
            print arr;
            print("%i\t%s\t%g" % (len(arr), pivot_selector.Name(), end_time - start_time));
            break;
        break;
    #a = Andy();
    #g = Quicksort(Andy());
    #g.Partition("lab on fire");
