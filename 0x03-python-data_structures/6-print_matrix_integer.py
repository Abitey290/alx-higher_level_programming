#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        a = 0
        for b in row:
            len_matrix = len(row)
            a += 1
            print("{:d}".format(b), end="")
            if a != len_matrix:
                print(" ", end="")
        print("")
