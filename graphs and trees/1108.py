#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: https://www.e-olymp.com/ru/problems/1108
# Created: 12/8/18

import sys


inf = sys.maxsize


class Graph:
    """
    класс граф
    """
    def __init__(self, n):
        """
        коснтруктор
        :param n: кол-во вершин
        """
        self.size = n
        self.graph = []

    def addEdge(self, vert1, vert2, weight):
        """
        :param vert1: ребро (начало пути)
        :param vert2: ребро (конец пути)
        :param weight: вес
        """
        self.graph.append([vert1, vert2, weight])

    def BellmanFord(self, vert):
        """
        Алгоритм Беллмана-Форда
        :param vert: вершина
        :return: True / False
        """
        success = False
        dist = [inf] * self.size
        dist[vert] = 0
        for i in range(self.size - 1):
            for v1, v2, w in self.graph:
                if dist[v1] != inf and dist[v1] + w < dist[v2]:
                    dist[v2] = dist[v1] + w
        for v1, v2, w in self.graph:
            if dist[v1] != inf and dist[v1] + w < dist[v2]:
                success = True
                break
        return success


if __name__ == '__main__':
    n, m = map(int, input().split())
    G = Graph(n)
    for i in range(m):
        a, b, c = map(int, input().split())
        G.addEdge(a, b, c)
    if G.BellmanFord(0):
        print('possible')
    else:
        print('not possible')
