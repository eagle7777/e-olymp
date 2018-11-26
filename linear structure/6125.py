#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: https://www.e-olymp.com/ru/problems/6125
# Created: 11/26/18

# реализация очереди


class Node:
    """
    вспомогательный класс
    описывает узел (элемент) очереди
    """
    def __init__(self, item=None):
        """
        конструктор
        :param item:
        """
        self.item = item  # значение
        self.next = None  # ссылка на следующий узел очереди


class Queue:
    """
    класс очередь
    """
    def __init__(self):
        """
        конструктор
        """
        self.m_front = None  # будем запоминать первый узел,
        self.m_back = None  # последний
        self.size = 0  # и длину очереди (кол-во элементов в ней0

    def empty(self):
        """
        :return: True - елси очередь пустая / False - в противном случае
        """
        return self.m_front is None and self.m_back is None

    def push(self, item):
        """
        Добавить элемент в очередь
        :param item: элемент
        :return:
        """
        self.size += 1  # увеличиваем длину на 1
        new_node = Node(item)
        if self.empty():
            self.m_front = new_node
        else:
            self.m_back.next = new_node
        self.m_back = new_node

    def pop(self):
        """
        Извлечь элемент из очереди
        :return: первый элемент в очереди
        """
        assert not self.empty(), 'Queue is empty!'
        current_front = self.m_front
        item = current_front.item
        self.m_front = self.m_front.next
        del current_front
        self.size -= 1
        if self.m_front is None:
            self.m_back = None
        return item

    def front(self):
        """
        посмотреть первый элемент, не удаляя его из очереди
        :return:
        """
        assert not self.empty(), 'Queue is empty!'
        return self.m_front.item

    def __len__(self):
        """
        переопределение (для длины len(Queue()))
        :return:
        """
        return self.size


if __name__ == '__main__':
    Q = Queue()
    while True:
        s = input()
        if s == 'exit':
            print('bye')
            break
        elif s == 'pop':
            print(Q.pop())
        elif s == 'front':
            print(Q.front())
        elif s == 'size':
            print(len(Q))
        elif s == 'clear':
            while len(Q):
                Q.pop()
            print('ok')
        else:
            s = s.split()
            Q.push(s[1])
            print('ok')
