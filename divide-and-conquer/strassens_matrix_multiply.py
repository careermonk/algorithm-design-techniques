# -*- coding: utf-8 -*-
from numpy import *  # analysis:ignore
import numpy

TEST_S_MATRIX = matrix([[2, 2], [4, 4]])

def square_matrix_multiply(A, B):
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape

    rows = len(A)
    C = zeros((rows, rows), dtype=int)
    for i in range(0, rows):
        for j in range(0, rows):
            C[i][j] = 0
            for k in range(0, rows):
                C[i][j] += A[i][k] * B[k][j]

    return matrix(C)


def strassens_matrix_multiply(A, B):
    A = asarray(A)
    B = asarray(B)
    assert A.shape == B.shape
    assert A.shape == A.T.shape
    assert (len(A) & (len(A) - 1)) == 0, "A is not a power of 2"

    rows = len(A)
    half = len(A) / 2

    if rows < 2:
        return square_matrix_multiply(matrix(A), matrix(B))

    A11 = zeros((half, half), dtype=int)
    A12 = zeros((half, half), dtype=int)
    A21 = zeros((half, half), dtype=int)
    A22 = zeros((half, half), dtype=int)

    B11 = zeros((half, half), dtype=int)
    B12 = zeros((half, half), dtype=int)
    B21 = zeros((half, half), dtype=int)
    B22 = zeros((half, half), dtype=int)

    result_a = zeros((half, half), dtype=int)
    result_b = zeros((half, half), dtype=int)

    for i in range(0, half):
        for j in range(0, half):
            A11[i][j] = A[i][j]
            A12[i][j] = A[i][j + half]
            A21[i][j] = A[i + half][j]
            A22[i][j] = A[i + half][j + half]

            B11[i][j] = B[i][j]
            B12[i][j] = B[i][j + half]
            B21[i][j] = B[i + half][j]
            B22[i][j] = B[i + half][j + half]

    # M0 = (A11+A22) * (B11+B22)
    result_a = add(A11, A22)
    result_b = add(B11, B22)
    M0 = strassens_matrix_multiply(matrix(result_a), matrix(result_b))

    # M1 = (A21+A22) * (B11)
    result_a = add(A21, A22)
    M1 = strassens_matrix_multiply(matrix(result_a), matrix(B11))

    # M2 = (A11) * (B12 - B22)
    result_b = subtract(B12, B22)
    M2 = strassens_matrix_multiply(matrix(A11), matrix(result_b))

    # M3 = (A22) * (B21 - B11)
    result_b = subtract(B21, B11)
    M3 = strassens_matrix_multiply(matrix(A22), matrix(result_b))

    # M4 = (A11+A12) * (B22)
    result_a = add(A11, A12)
    M4 = strassens_matrix_multiply(matrix(result_a), matrix(B22))

    # M5 = (A21-A11) * (B11+B12)
    result_a = subtract(A21, A11)
    result_b = add(B11, B12)
    M5 = strassens_matrix_multiply(matrix(result_a), matrix(result_b))

    # M6 = (A12-A22) * (B21+B22)
    result_a = subtract(A12, A22)
    result_b = add(B21, B22)
    M6 = strassens_matrix_multiply(matrix(result_a), matrix(result_b))

    # C12 = M2 + M4
    C12 = asarray(add(M2, M4))
    # C21 = M1 + M3
    C21 = asarray(add(M1, M3))

    # C11 = M0 + M3 - M4 + M6
    result_a = add(M0, M3)
    result_b = add(result_a, M6)
    C11 = asarray(subtract(result_b, M4))

    # C22 = M0 + M2 - M1 + M5
    result_a = add(M0, M2)
    result_b = add(result_a, M5)
    C22 = asarray(subtract(result_b, M1))

    C = zeros((rows, rows), dtype=int)

    for i in range(0, half):
        for j in range(0, half):
            C[i][j] = C11[i][j]
            C[i][j + half] = C12[i][j]
            C[i + half][j] = C21[i][j]
            C[i + half][j + half] = C22[i][j]
    return C


A = matrix([[1, 2], [3, 4]])
B = matrix([[2, 2], [4, 4]])
print strassens_matrix_multiply(A, B)
