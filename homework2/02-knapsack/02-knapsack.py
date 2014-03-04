#!/usr/bin/env python

import copy;

# BEGIN http://rosettacode.org/wiki/Power_set#Python
def list_powerset(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result], lst, [[]]);
 
def powerset(s):
    return frozenset(map(frozenset, list_powerset(list(s))))
# END

class KnapsackItem():
    def __init__(self, weight, price):
        self.weight = weight;
        self.price = price;
        self.value = self.price / float(self.weight);
    
    def __repr__(self):
        return "%i\t%i\t%03.2f" % (self.weight, self.price, self.value);
    
class Knapsack():
    def __init__(self, capacity):
        self.capacity = capacity;
        self.items = [];
        
    def add_item(self, item):
        if self.can_add(item):
            self.items.append(item);
            return True;
        else:
            return False;
    
    def can_add(self, item):
        return self.capacity >= self.weight() + item.weight;
    
    def weight(self):
        sum_of_weights = 0;
        for item in self.items:
            sum_of_weights += item.weight;
        return sum_of_weights;
    
    def price(self):
        sum_of_prices = 0;
        for item in self.items:
            sum_of_prices += item.price;
        return sum_of_prices;
        
    def empty(self):
        self.items = [];

    def greedy_fill(self, items):
        items = sorted(copy.deepcopy(items), key = lambda item: item.value, reverse = True);
        print "\tWeight\tPrice\tValue"
        for item in items:
            if self.add_item(item):
                print "Item:\t" + str(item);
                
    # not used for this assignment
    def greedy_powerset_fill(self, items):
        best_price = 0;
        best_set = [];
        pset = powerset(items);
        for set in pset:
            weight = 0;
            price = 0;
            for item in set:
                weight += item.weight;
                price += item.price;
            if weight <= self.capacity:
                if price >= best_price:
                    best_price = price;
                    best_set = set;
        self.items = sorted(best_set, key=lambda item: item.value, reverse=True);
        print "\tWeight\tPrice\tValue";
        for item in self.items:
            print "Item:\t" + str(item);
    
    def greedy_fractional_fill(self, items):
        return;
        
    def report_contents(self):
        print "Capacity: " + str(self.capacity);
        print "Weight:   " + str(self.weight());
        print "Price:    " + str(self.price());
        print "Items:    " + str(len(self.items));
        #print "\tWeight\tPrice\tValue\tQuantity";
        #for item in self.items:
        #    print "\t" + str(item);
        print;

def zeroOneKnapsack(v, w, W):
	# c is the cost matrix
	c = [];
	n = len(v);
	c = zeros(n, W + 1); # create the empty matrix
	for i in range(0, n):
		#for ever possible weight
		for j in range(0, W + 1):
		    #can we add this item to this?
			if (w[i] > j):
				c[i][j] = c[i - 1][j]
			else:
				c[i][j] = max(c[i-1][j], v[i] + c[i-1][j - w[i]])
	print c;
	return [c[n-1][W], getUsedItems(w,c)]

# w = list of item weight or cost
# c = the cost matrix created by the dynamic programming solution
def getUsedItems(w,c):
    # item count
	i = len(c) - 1
	currentW = len(c[0])-1
	# set everything to not marked
	marked = []
	for i in range(i+1):
		marked.append(0)			
	while (i >= 0 and currentW >=0):
		if (i == 0 and c[i][currentW] >0 )or c[i][currentW] != c[i-1][currentW]:
			marked[i] =1
			currentW = currentW-w[i]
		i = i-1
	return marked

def zeros(rows,cols):
	row = []
	data = []
	for i in range(cols):
		row.append(0)
	for i in range(rows):
		data.append(row[:])
	return data

if __name__ == '__main__':
    knapsack_items = [
      KnapsackItem(20, 15),
      KnapsackItem(24,  9),
      KnapsackItem(14, 27),
      KnapsackItem(20, 12),
      KnapsackItem(18, 36),
      KnapsackItem(20, 12),
      KnapsackItem(10,  9),
      KnapsackItem( 6, 12)
    ];
    
    print "Available Items:";
    print "Weight\tPrice\tValue";
    for knapsack_item in knapsack_items:
      print knapsack_item;
    print;
    
    print "Greedy 0-1 Fill";
    knapsack = Knapsack(80);
    knapsack.greedy_fill(knapsack_items);
    knapsack.report_contents();

    print "Greedy Powerset Fill";
    knapsack.empty();
    knapsack.greedy_powerset_fill(knapsack_items);
    knapsack.report_contents();
    
    print "Greedy Fractional Fill";
    knapsack.empty();
    knapsack.greedy_fractional_fill(knapsack_items);
    knapsack.report_contents();
    
    print;
    
    v = [15,  9, 27, 12, 36, 12,  9, 12];
    w = [20, 24, 14, 20, 18, 20, 10,  6];
    
    print str(zeroOneKnapsack(v, w, 80));
    
    v = [5, 6, 2];
    w = [2, 3, 2];
    
    print str(zeroOneKnapsack(v, w, 4));