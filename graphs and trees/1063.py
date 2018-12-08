#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: https://www.e-olymp.com/ru/problems/1063
# Created: 12/8/18


class NodeForQueue:
    """
    Вспомогательный класс
    узел очереди
    """
    def __init__(self, item=None):
        self.item = item  # нагрузка (значение) элемента
        self.next = None  # ссылка на следующий в очереди


class Queue:
    """
    Очередь
    """
    def __init__(self):
        """
        конструктор
        """
        self.m_front = None  # первый элемент
        self.m_back = None  # послдений элемент
        self.size = 0  # длина очереди

    def empty(self):
        """
        :return: True - если очередь пуста / False - в противном случае
        """
        return self.m_front is None and self.m_back is None

    def push(self, item):
        """
        добавляет элемент в очередь
        :param item: элемент
        :return:
        """
        self.size += 1
        new_node = NodeForQueue(item)
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
        возвращает первый элемент, но не удаляет его
        :return: первый элемент
        """
        assert not self.empty(), 'Queue is empty!'
        return self.m_front.item

    def __len__(self):
        return self.size


def main(n, m, char):
    paper = [[False for _ in range(m+2)] for _ in range(n+2)]
    mark = [[0 for _ in range(m+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(m):
            if char[i][j] == '#':
                paper[i+1][j+1] = True
    count = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if mark[i][j] == 0 and paper[i][j]:
                Q = Queue()
                Q.push((i, j))
                mark[i][j] = count
                while not Q.empty():
                    cur_i, cur_j = Q.pop()
                    for t in range(-1, 2):
                        tmp = -1 if t == 0 else 0
                        for k in range(tmp, 2, 2):
                            if paper[cur_i + t][cur_j + k] and mark[cur_i + t][cur_j + k] == 0:
                                Q.push((cur_i + t, cur_j + k))
                                mark[cur_i + t][cur_j + k] = count
                count += 1
    return count - 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    char = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        tmp = input()
        for j in range(m):
            char[i][j] = tmp[j]
    print(main(n, m, char))

