import math
import graph
import random

g = graph.Graph(-1, "cities50")
g.tourValue()

g = graph.Graph(12, "twelvenodes")
g.tourValue()
g.swapHeuristic(12)
g.tourValue()
g = graph.Graph(-1, "cities50")
g.swapHeuristic(50)
g.TwoOptHeuristic(50)
g.tourValue()
g = graph.Graph(-1, "cities50")
print(g.Improved_Greedy())


def Euclidean_Graph(n, lb, ub):
    file = open("Euclidean_Graph_" + str(n) + ".txt", "w")
    for i in range(n):
        x, y = random.randint(lb, ub), random.randint(lb, ub)
        if x < 10:
            space1 = "   "
        elif x < 100:
            space1 = "  "
        elif x < 1000:
            space1 = " "
        if y < 10:
            space2 = "    "
        elif y < 100:
            space2 = "   "
        elif y < 1000:
            space2 = "  "

        file.write(space1 + str(x) + space2 + str(y) + "\n")
    file.close()


Euclidean_Graph(20, 2, 20)
Euclidean_Graph(40, 2, 20)
Euclidean_Graph(60, 2, 20)
Euclidean_Graph(80, 2, 20)
g20 = graph.Graph(-1, "Euclidean_Graph_20.txt")
g40 = graph.Graph(-1, "Euclidean_Graph_40.txt")
g60 = graph.Graph(-1, "Euclidean_Graph_60.txt")
g80 = graph.Graph(-1, "Euclidean_Graph_80.txt")


print(20)
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
for i in range(10):

    t1 += g20.tourValue()

    g20.swapHeuristic(20)
    t2 += g20.tourValue()

    g20.TwoOptHeuristic(20)
    t3 += g20.tourValue()

    g20.Greedy()
    t4 += g20.tourValue()

    g20.Improved_Greedy()
    t5 += g20.tourValue()

t1, t2, t3, t4, t5 = t1 / 25, t2 / 25, t3 / 25, t4 / 25, t5 / 25
print(t1, t2, t3, t4, t5)

print(40)
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
for i in range(10):


    t1 += g40.tourValue()

    g40.swapHeuristic(40)
    t2 += g40.tourValue()

    g40.TwoOptHeuristic(40)
    t3 += g40.tourValue()

    g40.Greedy()
    t4 += g40.tourValue()

    g40.Improved_Greedy()
    t5 += g40.tourValue()

t1, t2, t3, t4, t5 = t1 / 25, t2 / 25, t3 / 25, t4 / 25, t5 / 25
print(t1, t2, t3, t4, t5)

print(60)
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
for i in range(10):


    t1 += g60.tourValue()

    g60.swapHeuristic(60)
    t2 += g60.tourValue()

    g60.TwoOptHeuristic(60)
    t3 += g60.tourValue()

    g60.Greedy()
    t4 += g60.tourValue()

    g60.Improved_Greedy()
    t5 += g60.tourValue()

t1, t2, t3, t4, t5 = t1 / 25, t2 / 25, t3 / 25, t4 / 25, t5 / 25
print(t1, t2, t3, t4, t5)

print(80)
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
for i in range(10):


    t1 += g80.tourValue()

    g80.swapHeuristic(80)
    t2 += g80.tourValue()

    g80.TwoOptHeuristic(80)
    t3 += g80.tourValue()

    g80.Greedy()
    t4 += g80.tourValue()

    g80.Improved_Greedy()
    t5 += g80.tourValue()

t1, t2, t3, t4, t5 = t1 / 25, t2 / 25, t3 / 25, t4 / 25, t5 / 25
print(t1, t2, t3, t4, t5)


def General_Graph(n, lb, ub):
    file = open("General_Graph_" + str(n) + ".txt", "w")
    for i in range(n):
        for j in range(n):
            if i < j:
                file.write(str(i) + " " + str(j) + " " + str(random.randint(lb, ub)) + "\n")
    file.close()


General_Graph(4, 2, 20)
General_Graph(6, 2, 20)
General_Graph(8, 2, 20)
General_Graph(10, 2, 20)
g20_ = graph.Graph(-1, "General_Graph_4.txt")
g40_ = graph.Graph(-1, "General_Graph_6.txt")
g60_ = graph.Graph(-1, "General_Graph_8.txt")
g80_ = graph.Graph(-1, "General_Graph_10.txt")

print(4)
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
for i in range(25):

    t1 += g20_.tourValue()

    g20_.swapHeuristic(20)
    t2 += g20_.tourValue()

    g20_.TwoOptHeuristic(20)
    t3 += g20_.tourValue()

    g20_.Greedy()
    t4 += g20_.tourValue()

    g20_.Improved_Greedy()
    t5 += g20_.tourValue()

t1, t2, t3, t4, t5 = t1 / 25, t2 / 25, t3 / 25, t4 / 25, t5 / 25
print(t1, t2, t3, t4, t5)

print(6)
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
for i in range(25):


    t1 += g40_.tourValue()

    g40_.swapHeuristic(40)
    t2 += g40_.tourValue()

    g40_.TwoOptHeuristic(40)
    t3 += g40_.tourValue()

    g40_.Greedy()
    t4 += g40_.tourValue()

    g40_.Improved_Greedy()
    t5 += g40_.tourValue()

t1, t2, t3, t4, t5 = t1 / 25, t2 / 25, t3 / 25, t4 / 25, t5 / 25
print(t1, t2, t3, t4, t5)

print(8)
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
for i in range(25):


    t1 += g60_.tourValue()

    g60_.swapHeuristic(60)
    t2 += g60_.tourValue()

    g60_.TwoOptHeuristic(60)
    t3 += g60_.tourValue()

    g60_.Greedy()
    t4 += g60_.tourValue()

    g60_.Improved_Greedy()
    t5 += g60_.tourValue()

t1, t2, t3, t4, t5 = t1 / 25, t2 / 25, t3 / 25, t4 / 25, t5 / 25
print(t1, t2, t3, t4, t5)

print(10)
t1, t2, t3, t4, t5 = 0, 0, 0, 0, 0
for i in range(25):


    t1 += g80_.tourValue()

    g80_.swapHeuristic(80)
    t2 += g80_.tourValue()

    g80_.TwoOptHeuristic(80)
    t3 += g80_.tourValue()

    g80_.Greedy()
    t4 += g80_.tourValue()

    g80_.Improved_Greedy()
    t5 += g80_.tourValue()

t1, t2, t3, t4, t5 = t1 / 25, t2 / 25, t3 / 25, t4 / 25, t5 / 25
print(t1, t2, t3, t4, t5)