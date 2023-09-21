import numpy as np

def least_squares_estimation(X1, X2):
  """
  A = np.zeros((len(X1),9))
  for i in range(len(X1)):
    x1 = X1[i][0]
    x2 = X2[i][0]
    y1 = X1[i][1]
    y2 = X2[i][1]
    z1 = X1[i][2]
    z2 = X2[i][2]
    A_row = np.array([x1*x2, x1*y2, x1*z2, y1*x2, y1*y2, y1*z2, z1*x2, z1*y2, z1*z2])
    A[i] = A_row
  U, S, VT = np.linalg.svd(A)
  E_prime = VT.T[:,8].reshape(3,3).T
  U, S, VT = np.linalg.svd(E_prime)
  E = U @ np.diag([1,1,0]) @ VT
  """
  return E
