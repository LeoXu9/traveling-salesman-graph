import math
import random


def euclid(p, q):
    x = p[0] - q[0]
    y = p[1] - q[1]
    return math.sqrt(x * x + y * y)


class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self, n, filename):
        f = open(filename, "r")

        # Euclidean input
        if n == -1:
            cities = []
            content = f.readlines()
            f.close()
            self.n = sum(1 for line in open(filename))  # set n to number of lines in file
            for line in content:
                single_line = line.strip().split()  # a list of three elements for each line in file
                single_line[0] = int(single_line[0])
                single_line[1] = int(single_line[1])
                cities.append(single_line)

            self.perm = [x for x in range(self.n)]  # perm[i] equal to i
            self.dists = [[0 for i in range(self.n)] for j in range(self.n)]  # initialise the 2d list
            for i in range(self.n):
                for j in range(self.n):
                    self.dists[i][j] = euclid(cities[i], cities[j])

        # General input
        elif n > 0:
            content = f.readlines()
            f.close()
            self.n = n
            self.dists = [[0 for i in range(self.n)] for j in range(self.n)]
            self.perm = [i for i in range(self.n)]
            for line in content:
                single_line = line.strip().split()
                city1 = int(single_line[0])
                city2 = int(single_line[1])
                dist = int(single_line[2])
                self.dists[city1][city2] = self.dists[city2][city1] = dist

    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        result = 0
        for i in range(self.n):
            result += self.dists[self.perm[i]][self.perm[(i + 1) % self.n]]
        return result

    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self, i):
        old_tour_value = self.dists[self.perm[(i + 1) % self.n]][self.perm[(i + 2) % self.n]] + \
                         self.dists[self.perm[(i - 1) % self.n]][self.perm[i]]
        new_tour_value = self.dists[self.perm[(i - 1) % self.n]][self.perm[(i + 1) % self.n]] + \
                         self.dists[self.perm[i]][self.perm[(i + 2) % self.n]]
        if old_tour_value > new_tour_value:
            self.perm[i], self.perm[(i + 1) % self.n] = self.perm[(i + 1) % self.n], self.perm[i]
            return True
        else:
            return False

    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    def tryReverse(self, i, j):
        old_tour_value = self.dists[self.perm[(i - 1) % self.n]][self.perm[i]] + \
                         self.dists[self.perm[(j + 1) % self.n]][self.perm[j]]
        new_tour_value = self.dists[self.perm[(i - 1) % self.n]][self.perm[j]] + \
                         self.dists[self.perm[(j + 1) % self.n]][self.perm[i]]
        if old_tour_value > new_tour_value:
            self.perm[i:j + 1] = self.perm[i:j + 1][::-1]
            return True
        else:
            return False

    def swapHeuristic(self, k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self, k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for j in range(self.n - 1):
                for i in range(j):
                    if self.tryReverse(i, j):
                        better = True

    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        travelled = list()  # cities that have been traveled
        initial_city = 0  # always start from this city
        travelled.append(initial_city)
        for i in range(self.n - 1):
            min_dist = math.inf  # initialise minimum distance as infinity
            nearest_city = ""  # variable that stores the nearest city to current city
            for j in range(self.n):  # iterate through every possible distance
                if j not in travelled:
                    new_dist = self.dists[j][travelled[-1]]
                    if new_dist < min_dist:
                        min_dist = new_dist
                        nearest_city = j
            travelled.append(nearest_city)  # append the new destination to the traveled city list
        self.perm = travelled
        return

    def Improved_Greedy(self):  # this function gets every permutation with different initial cities.
        all_travelled = list()
        for k in range(self.n):
            travelled = list()  # cities that have been traveled
            travelled.append(k)
            for i in range(self.n - 1):
                min_dist = math.inf  # initialise minimum distance as infinity
                nearest_city = ""  # variable that stores the nearest city to current city
                for j in range(self.n):  # iterate through every possible distance
                    if j not in travelled:
                        new_dist = self.dists[j][travelled[-1]]
                        if new_dist < min_dist:
                            min_dist = new_dist
                            nearest_city = j
                travelled.append(nearest_city)  # append the new destination to the traveled city list
            all_travelled.append(travelled)

        # now calculate the best one out of all_travelled
        results = []
        for i in range(self.n):
            result = 0
            for j in range(self.n):
                result += self.dists[all_travelled[i][j]][all_travelled[i][(j + 1) % self.n]]
            results.append(result)

        # find the best tour out of all
        best = min(results)
        index_number = results.index(best)
        best_tour = all_travelled[index_number]
        self.perm = best_tour
