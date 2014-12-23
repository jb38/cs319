#!/usr/bin/env python

import copy; #for deep copies of lists

class KnapsackItem():
    def __init__(self, weight, price, part = 1.0):
        self.weight = weight;
        self.price = price;
        if self.weight is not 0:
          self.value = self.price / float(self.weight);
        else:
          self.value = 0;
        self.part = part;

    def __repr__(self):
        return "%i\t%i\t%03.2f\t%03.2f" % (self.weight, self.price, self.value, self.part);

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
        return self.capacity >= self.weight() + (item.weight * item.part);

    def weight(self):
        sum_of_weights = 0.0;
        for item in self.items:
            sum_of_weights += item.weight * item.part;
        return sum_of_weights;

    def price(self):
        sum_of_prices = 0.0;
        for item in self.items:
            sum_of_prices += item.price * item.part;
        return sum_of_prices;

    def item_count(self):
        sum_of_items = 0.0;
        for item in self.items:
            sum_of_items += item.part;
        return sum_of_items;

    def empty(self):
        self.items = [];

    def greedy_fill(self, items):
        items = sorted(copy.deepcopy(items), key = lambda item: item.value, reverse = True);
        print "\tWeight\tPrice\tValue\tPart"
        for item in items:
            if self.add_item(item):
                print "Item:\t" + str(item);

    def greedy_fractional_fill(self, items):
        items = sorted(copy.deepcopy(items), key = lambda item: item.value, reverse = True);
        print "\tWeight\tPrice\tValue\tPart"
        for item in items:
            if self.add_item(item):
                print "Item:\t" + str(item);
            else:
                item_copy = copy.deepcopy(item);
                item_copy.part = (self.capacity - self.weight()) / item_copy.weight;
                if self.add_item(item_copy):
                    print "Item:\t" + str(item_copy);
                break;
        return;

    def report_contents(self):
        print "Capacity: " + str(self.capacity);
        print "Weight:   " + str(self.weight());
        print "Price:    " + str(self.price());
        print "Items:    " + str(self.item_count());
        print;

if __name__ == '__main__':
    knapsack_items = [
      KnapsackItem(0, 0),
      KnapsackItem(1, 11),
      KnapsackItem(11, 21),
      KnapsackItem(21, 31),
      KnapsackItem(23, 33),
      KnapsackItem(33, 43),
      KnapsackItem(43, 53),
      KnapsackItem(45, 55),
      KnapsackItem(53, 65)
    ];

    print "Available Items:";
    print "Weight\tPrice\tValue\tPart";
    for knapsack_item in knapsack_items:
      print knapsack_item;
    print;

    print "Greedy 0-1 Fill";
    knapsack = Knapsack(110);
    knapsack.greedy_fill(knapsack_items);
    knapsack.report_contents();

    print "Greedy Fractional Fill";
    knapsack.empty();
    knapsack.greedy_fractional_fill(knapsack_items);
    knapsack.report_contents();
