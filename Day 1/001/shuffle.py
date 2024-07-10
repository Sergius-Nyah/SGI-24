# shuffle the columns of A to the right by one, such that the
# new ith column is the old i-1th column, and the new 1st column is the old
# last column.

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # Example array
A = np.roll(A, shift=1, axis=1)
print(A)
