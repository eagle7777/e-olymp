#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# Created: 11/28/18


class Matrix:
    """
    класс для матриц
    """
    def __init__(self, l=list()):
        """
        коснтруктор
        матрица задается списком или списком списков
        :param l:
        """
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

    def getMatrixSize(self):
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
        n, k = self.getMatrixSize()
        n2, k2 = other.getMatrixSize()
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
        n, k = self.getMatrixSize()
        n2, k2 = other.getMatrixSize()
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
        n, k = self.getMatrixSize()
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
        n, k = self.getMatrixSize()
        n2, k2 = other.getMatrixSize()
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
        n1, k1 = self.getMatrixSize()
        k2, m2 = other.getMatrixSize()
        assert k1 == k2, 'INVALID matrix size'
        new = Matrix.zeros(n1, m2)
        other_tran = other.transpose()
        for i in range(n1):
            new[i] = [self[i][j] * other_tran[i][j] for j in range(m2)]
        return new


if __name__ == '__main__':
    m1 = [[2, 0, 4, -1], [1, -1, 1, 0]]
    m2 = [[2], [1], [0], [-2]]
    a = Matrix(m1)
    b = Matrix(m2)