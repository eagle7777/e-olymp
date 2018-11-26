#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: https://www.e-olymp.com/ru/problems/3329
# Created: 11/26/18


#  Создадим граф с вершинами (домами) и преобразуем его в дерево


class Vertex:
    """
    Вспомогательный класс
    Вершина графа
    """
    def __init__(self, key, data=0):
        """
        конструктор
        :param key: ключ (номер дома)
        :param data: энергия дома
        """
        self.key = key
        self.data = data
        self.neighbors = []  # список всех соседей

    def addNeighbour(self, neighbour):
        """
        Добавить соседа
        :param neighbour: сосед
        :return:
        """
        self.neighbors.append(neighbour)
        neighbour.neighbors.append(self)

    #  вспомогательные методы для вывода
    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class Graph:
    """
    класс граф
    """
    def __init__(self):
        self.vertexNumber = 0
        self.vertices = {}  # словарь всех вершин графа (содержит пары key: Vertex)

    def addVertex(self, v: Vertex):
        """
        добавить вершину в граф
        :param v: вершина
        :return:
        """
        self.vertexNumber += 1
        self.vertices[v.key] = v

    def getVertex(self, key):
        """
        получить вершину (объект) по ключу
        :param key: ключ
        :return: вершина # type: Vertex
        """
        return self.vertices[key]

    def addEdge(self, v1, v2):
        """
        Добавить ребро между двумя вершинами, которые задаются ключами
        :param v1: ключ 1-й вершины
        :param v2: ключ 2-1 вершины
        :return:
        """
        self.vertices[v1].addNeighbour(self.vertices[v2])


class TreeNode:
    """
    Вспомогательный класс
    Узел дерева
    """
    def __init__(self, key=None, father=None, data=0):
        """
        Конструктор
        :param key: ключ
        :param father: ссылка на родителя (корень дерева ссылается на None)
        :param data: энергия (сначала = 0)
        """
        self.key = key
        self.data = data
        self.father = father
        self.deep = 0  # глубина вершины (кол-во вершин от заданной до корня)

    def setFather(self, father):
        """
        выбрать родителя
        :param father:
        :return:
        """
        self.father = father

    # вспомогательный метод для вывода
    def __repr__(self):
        return str('key: {}, data: {};'.format(self.key, self.data))


class Tree:
    """
    Класс Дерево
    """
    def __init__(self, root=None):
        """
        коструктор
        дерево задается корнем
        все остальные вершины можно получить рекурсивно
        :param root: корень # type: TreeNode
        """
        self.root = root

    def findWayToRoot(self, v: TreeNode) -> list:
        """
        нахождения пути от вершины до корня
        :param v: вершина
        :return: список всех вершин на пути из текущей до корня
        """
        way = []
        while v is not None:
            way.append(v)
            v = v.father
        return way

    def findWay(self, vertA: TreeNode, vertB: TreeNode) -> list:
        """
        нахождения пути между двумя вершинами в дереве
        :param vertA: вершина A
        :param vertB: вершина B
        :return: список всех вершин на пути из вершины A в вершину B
        """
        if vertA == self.root:  # если какая-то из вершин является корнем то ищем путь от другой до корня
            return self.findWayToRoot(vertB)
        if vertB == self.root:
            return self.findWayToRoot(vertA)
        way = []
        #  "стабилизируем" до одинаковой глубины
        if vertA.deep > vertB.deep:
            while vertA.deep != vertB.deep:
                way.append(vertA)
                vertA = vertA.father
        elif vertB.deep > vertA.deep:
            while vertA.deep != vertB.deep:
                way.append(vertB)
                vertB = vertB.father
        while vertA != vertB:  # пока вершины не совпадают идем вверх и сравниваем отцов
            way.append(vertA)
            way.append(vertB)
            vertA = vertA.father
            vertB = vertB.father
        way.append(vertA)
        return way


def _buildHelper(graph: Graph, visited: set, start: Vertex, nodeList: list):
    """
    Вспомогательная рекурсивная функция для преобразования графа в дерево
    :param graph: граф
    :param visited: список вершин, в которых мы уже побывали
    :param start: текущая стартовая вершина
    :param nodeList: список всех вершин
    :return:
    """
    visited.add(start)
    for neighbour in start.neighbors:
        if neighbour not in visited:
            nodeList[neighbour.key].setFather(nodeList[start.key])
            nodeList[neighbour.key].deep = nodeList[start.key].deep + 1
            _buildHelper(graph, visited, neighbour, nodeList)


def BuildTree(graph: Graph, start: Vertex, nodeList: list) -> Tree:
    """
    Преобразование графа в дерево
    :param graph: граф
    :param start: вершина, с которой начинается обход
    :param nodeList: список всех узлов дерева
    :return: дерево
    """
    T = Tree(nodeList[start.key])  # создаем дерево с корнем в вершине старт
    visited = set()  # создаем множество чтоб отмечать посещенные вершины
    _buildHelper(graph, visited, start, nodeList)
    return T


if __name__ == '__main__':
    T = int(input())  # кол-во тестов
    for test in range(T):
        N = int(input())  # кол-во вершин
        vert = [Vertex(i) for i in range(N)]
        treeNodes = [TreeNode(i) for i in range(N)]
        G = Graph()
        for v in vert:
            G.addVertex(v)  # добавляем вершины в граф
        for i in range(N-1):  # добавляем N-1 ребро
            s, e = map(int, input().split())
            G.addEdge(s, e)
        T = BuildTree(G, vert[0], treeNodes)  # преобразовываем граф в дерево
        del G, vert
        Q = int(input())  # кол-во ударов молнии
        for i in range(Q):
            A, B, C = map(int, input().split())
            verticesOnWay = T.findWay(treeNodes[A], treeNodes[B])  # находим все вершины на пути
            for v in verticesOnWay:
                v.data += C  # и каждой прибавляем энергию C
        # вывод
        print('Case #{}:'.format(test + 1))
        for i in range(N):
            print(treeNodes[i].data)
