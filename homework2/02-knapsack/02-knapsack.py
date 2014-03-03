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
        return "%i\t%i\t%g" % (self.weight, self.price, self.value);
    
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
        best_price = 0;
        best_set = [];
        pset = powerset(items);
        for s in pset:
            weight = 0;
            price = 0;
            for item in s:
                weight += item.weight;
                price += item.price;
            if weight <= self.capacity:
                if price >= best_price:
                    best_price = price;
                    best_set = s;
        self.items = sorted(best_set, key=lambda item: item.value, reverse=True);
    
    def greedy_fractional_fill(self, items):
        return;
        
    def report_contents(self):
        print "Capacity: " + str(self.capacity);
        print "Weight:   " + str(self.weight());
        print "Price:    " + str(self.price());
        print "Items:    " + str(len(self.items));
        print "\tWeight\tPrice\tValue\tQuantity";
        for item in self.items:
            print "\t" + str(item);
        print;

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
    
    print "Greedy Fill";
    knapsack = Knapsack(80);
    knapsack.greedy_fill(knapsack_items);
    knapsack.report_contents();
    
    print "Greedy Fractional Fill";
    knapsack.empty();
    knapsack.greedy_fractional_fill(knapsack_items);
    knapsack.report_contents();
