#!/usr/bin/env python
# coding: utf-8
# Author: Valentyn Kofanov (knu)
# source: https://www.e-olymp.com/ru/contests/11455/problems/2166
# Created: 11/27/18


from itertools import permutations


def main(s1: str, s2: str) -> str:
    """
    :param s1:
    :param s2:
    :return: YES / NO
    """
    #  находим список всех перестановок для s1
    #  возвращем YES если s2 входит в этот список / NO если нет
    return 'YES' if s2 in [''.join(i) for i in permutations(s1)] else 'NO'


if __name__ == '__main__':
    print(main(input(), input()))
