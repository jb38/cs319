#!/usr/bin/env python

class Activity():
    def __init__(self, start, finish):
        self.start  = start;
        self.finish = finish;

if __name__ == '__main__':
    activities = [
        Activity(1, 3),
        Activity(2, 5),
        Activity(4, 5),
        Activity(6, 7),
        Activity(4, 7)
    ];
    
    activities = sorted(activities, key = lambda activity: activity.finish);
    lecture_halls = [];
    
    while len(activities) > 0:
        lecture_hall = [];
        last_activity = None;
        for activity in activities:
            if last_activity == None or activity.start >= last_activity.finish:
                last_activity = activity;
                lecture_hall.append(activity);
        for activity in lecture_hall:
            activities.remove(activity);
        lecture_halls.append(lecture_hall);
    
    for lecture_hall in lecture_halls:
        print "Lecture Hall";
        for activity in lecture_hall:
            print "  " + str(activity.start) + " -> " + str(activity.finish);
