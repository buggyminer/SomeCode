import random
import time
import unittest
import networkx as nx
import matplotlib.pyplot as plt


def generate_graph(n):
    vector = [[0] * n for i in range(n)]


def check_if_color_satisfied(adjacent, colors, color):
    for i, adj in zip(range(len(adjacent)), adjacent):
        if (adj == 1 and colors[i] == color): return False
    return True


def color_decode(color):
    color_dict = {0: "black", 1: "red", 2: "blue", 3: "green"}
    return color_dict[color]


def plot_graph(vector, colors=None):
    if (colors == None):
        colors = [1 for i in range(len(vector))]
    edges = []
    G = nx.Graph()
    for row, i in zip(vector, range(len(vector))):
        for col, j in zip(row, range(len(row))):
            if (col != 0):
                G.add_edge(i, j)
    nodes = list(zip(list(G.nodes), colors))
    sorted_list = sorted(nodes, key=lambda x: x[0])
    colors = [x[1] for x in sorted_list]
    nx.draw(G, node_color=[color_decode(color) for color in colors], with_labels=True)
    plt.show()


# 可能找不到可行解
def graph_coloring_greedy(vector, color_num):
    colors = [0 for i in range(len(vector[0]))]
    for i in range(len(vector[0])):
        color = colors[i]
        adjacents = vector[i]
        if (color == 0):
            while True:
                color = color + 1
                if (color > color_num):
                    return None
                if (check_if_color_satisfied(adjacents, colors, color)):
                    colors[i] = color
                    break
    return colors


# 回溯法
def graph_coloring_recall(vector, color_num):
    stack = []
    visit = [0 for i in range(len(vector))]
    colors = [0 for i in range(len(vector))]

    stack.append(0)
    visit[0] = 1
    while (len(stack) > 0):
        node_now = stack.pop()
        visit[node_now] = 1
        while colors[node_now] < color_num:
            colors[node_now] = colors[node_now] + 1
            if check_if_color_satisfied(vector[node_now], colors, colors[node_now]):
                break
        else:
            if 0 in visit:
                colors[node_now] = 0
                visit[node_now] = 0
                continue
        if 0 not in visit:
            return colors
        for i in range(len(vector[node_now])):
            if vector[node_now][i] == 1 and visit[i] == 0 and i not in stack:
                stack.append(i)


if __name__ == '__main__':
    test_graph_list = [
        {
            "vector":
                [
                    [0, 1, 1],
                    [1, 0, 0],
                    [1, 0, 0],
                ],
            "color_num": 2
        },
        {
            "vector":
                [
                    [0, 1, 1, 0, 1],
                    [1, 0, 0, 1, 0],
                    [1, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0],
                ],
            "color_num": 2
        },
        {
            "vector":
                [
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 0, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 1, 0, 1],
                    [0, 0, 1, 1, 0],
                ],
            "color_num": 3
        }
    ]

    for graph in test_graph_list:
        vector = graph["vector"]
        plot_graph(vector)
        color_num = graph["color_num"]
        colors = graph_coloring_recall(vector, color_num)
        if colors:
            plot_graph(vector, colors)

    time1=time.time()
    for i in range(1000):
        for graph in test_graph_list:
            vector = graph["vector"]
            color_num = graph["color_num"]
            colors = graph_coloring_recall(vector, color_num)
    time1=time.time()-time1
    print("time of recall is ",time1)

    time2=time.time()
    for i in range(1000):
        for graph in test_graph_list:
            vector = graph["vector"]
            color_num = graph["color_num"]
            colors = graph_coloring_greedy(vector, color_num)
    time2=time.time()-time2
    print("time of recall is ",time2)