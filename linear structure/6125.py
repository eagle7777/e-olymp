#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: https://www.e-olymp.com/ru/problems/6125
# Created: 11/26/18


class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None


class Queue:
    def __init__(self):
        self.m_front = None
        self.m_back = None
        self.size = 0

    def empty(self):
        return self.m_front is None and self.m_back is None

    def push(self, item):
        self.size += 1
        new_node = Node(item)
        if self.empty():
            self.m_front = new_node
        else:
            self.m_back.next = new_node
        self.m_back = new_node

    def pop(self):
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
        assert not self.empty(), 'Queue is empty!'
        return self.m_front.item

    def __len__(self):
        return self.size
