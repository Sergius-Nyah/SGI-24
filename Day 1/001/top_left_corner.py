# Select the top-left corner of a matrix
import numpy as np

def top_left_corner(A, r, c):
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Example array
    C = A[1:r, 1:c]
