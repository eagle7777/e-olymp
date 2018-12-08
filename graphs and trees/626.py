#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: https://www.e-olymp.com/ru/problems/626
# Created: 12/5/18


def main(n, m):
    vert = []
    for i in range(2, n+1):
        vert.append((i-1, i, 0))
        m -= 1
    for i in range(n, 1, -1):
        if m == 0:
            break
        for j in range(i-2, 0, -1):
            if m == 0:
                break
            vert.append((i, j, i-j))
            m -= 1
            if m == 0:
                break
        if m == 0:
            break
    for i in range(0, len(vert)):
        if vert[i][0] > vert[i][1]:
            vert[i] = (vert[i][1], vert[i][0], vert[i][2])
        print(*vert[i])


if __name__ == '__main__':
    main(*map(int, input().split()))
