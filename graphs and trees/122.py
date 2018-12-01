#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: https://www.e-olymp.com/ru/problems/122
# Created: 11/26/18


import random


class Matrix:
    """
    класс для матриц
    """
    def __init__(self, l=list()):
        """
        коснтруктор
        матрица задается списком (вектор) или списком списков (матрица)
        :param l:
        """
        if not isinstance(l[0], list):
            for i in range(len(l)):
                l[i] = [l[i]]
        self.m = l

    def __getitem__(self, item):
        """
        возвращает элемент по индексу
        :param item: индекс
        :return:
        """
        return self.m[item]

    def __setitem__(self, key, value):
        """
        устанавливает элемент по индексу
        :param key: индекс
        :param value: новое значение
        :return:
        """
        self.m[key] = value

    def __contains__(self, item):
        """
        переопределение метода 'in'
        :param item:
        :return:
        """
        return item in self.m

    def __str__(self):
        """
        метод ля вывода
        :return:
        """
        res = ''
        for row in self:
            res += '{}\n'.format(row)
        res.rstrip('\n')
        return res

    def __repr__(self):
        """
        метод для вывода
        :return:
        """
        res = ''
        for row in self:
            res += '{}\n'.format(row)
        res.rstrip('\n')
        return res

    def shape(self):
        """
        возвращает размер матрицы
        :return: кортеж (n, k) матрицы nxk
        """
        n = len(self.m)
        k = 1
        if isinstance(self.m[0], list):
            k = len(self.m[0])
        return n, k

    @staticmethod
    def eye(n):
        """
        возвращает единичную матрицу nxn
        :param n: размер матрицы
        :return:
        """
        new = Matrix([[0 for _ in range(n)] for _ in range(n)])
        for i in range(n):
            for j in range(n):
                if i == j:
                    new[i][j] = 1
        return new

    @staticmethod
    def zeros(n, k):
        """
        возвращает матрицу nxk заполненную нулями
        :param n:
        :param k:
        :return:
        """
        return Matrix([[0 for _ in range(k)] for _ in range(n)])

    def __add__(self, other):
        """
        сложение матриц
        :param other:
        :return: результат матричного сложения
        """
        n, k = self.shape()
        n2, k2 = other.shape()
        assert n == n2 and k == k2, 'INVALID matrix size'
        new = Matrix.zeros(n, k)
        for i in range(n):
            for j in range(k):
                new[i][j] = self[i][j] + other[i][j]
        return new

    def __sub__(self, other):
        """
        вычитание матриц
        :param other:
        :return:
        """
        n, k = self.shape()
        n2, k2 = other.shape()
        assert n == n2 and k == k2, 'INVALID matrix size'
        new = Matrix.zeros(n, k)
        for i in range(n):
            for j in range(k):
                new[i][j] = self[i][j] - other[i][j]
        return new

    def transpose(self):
        """
        возвращает транспонированную матрицу
        :return:
        """
        n, k = self.shape()
        new = Matrix.zeros(k, n)
        for i in range(n):
            for j in range(k):
                new[j][i] = self[i][j]
        return new

    def __eq__(self, other):
        """
        переопределение метода '=='
        :param other:
        :return: True, если две матрицы равны (поэлементно) / False, в противном случае
        """
        n, k = self.shape()
        n2, k2 = other.shape()
        assert n == n2 and k == k2, 'INVALID matrix size'
        success = True
        for i in range(n):
            for j in range(k):
                if self[i][j] != other[i][j]:
                    success = False
                    break
        return success

    def __mul__(self, other):
        """
        умножение матриц
        :param other:
        :return:
        """
        n1, k1 = self.shape()
        k2, m2 = other.shape()
        assert k1 == k2, 'INVALID matrix size'
        new = Matrix.zeros(n1, m2)
        for i in range(n1):
            for j in range(k1):
                for k in range(m2):
                    new[i][k] += self[i][j] * other[j][k]
        return new

    def __pow__(self, power):
        """
        возведение матрицы в степень
        :param power: степень
        :return:
        """
        new = Matrix(self.m)
        n = self.shape()[0]
        for i in range(power-1):
            new *= self
            for k in range(n):
                for j in range(n):
                    if k == j:
                        new[k][j] = 1
        return new

    def __hash__(self):
        return str.__hash__(str(self.m))

    @staticmethod
    def getRandomMatrix(n=None, m=None):
        """
        возвращает рандомную матрицу
        n и m размеры
        :param n: если не задано, то случайное
        :param m: если не задано, то случайное
        :return:
        """
        if not n or not m:
            n = random.randint(1, 30)
            m = random.randint(1, 30)
        new = Matrix.zeros(n, m)
        for i in range(n):
            for j in range(m):
                new[i][j] = random.randint(-100, 100)
        return new


class Graph:
    def __init__(self, n):
        """
        конструктор
        граф задается матрицей смежности
        :param n: кол-во вершин графа
        """
        self.adjacencyMatrix = Matrix.zeros(n, n)  # создаем нулевую матрицу nxn

    def __getitem__(self, item):
        return self.adjacencyMatrix.__getitem__(item)

    def __setitem__(self, key, value):
        return self.adjacencyMatrix.__setitem__(key, value)

    def addEdge(self, key1, key2):
        self[key1][key2] += 1

    def __str__(self):
        return self.adjacencyMatrix.__str__()

    def __repr__(self):
        return self.adjacencyMatrix.__repr__()

    def findFixedLengthPath(self, key1, key2, d):
        md = self.adjacencyMatrix ** d
        return md[key1][key2]


if __name__ == '__main__':
    n, k, a, b, d = map(int, input().split())
    G = Graph(n)
    for _ in range(k):
        v1, v2 = map(int, input().split())
        G.addEdge(v1-1, v2-1)
    print(G.findFixedLengthPath(a-1, b-1, d))
