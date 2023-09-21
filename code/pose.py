import numpy as np

def pose_candidates_from_E(E):
  transform_candidates = []
  ##Note: each candidate in the above list should be a dictionary with keys "T", "R"
  """ YOUR CODE HERE
  """
  Rz1 = np.array([[0, -1, 0],
                  [1, 0, 0],
                  [0, 0, 1]])
  Rz2 = np.array([[0, 1, 0],
                  [-1, 0, 0],
                  [0, 0, 1]])
  U, S, VT = np.linalg.svd(E)
  T1 = U[:,-1]
  T2 = -T1
  R1 = U @ Rz1.T @ VT
  R2 = U @ Rz2.T @ VT
  transform_candidates.append({"T":T1, "R":R1})
  transform_candidates.append({"T":T1, "R":R2})
  transform_candidates.append({"T":T2, "R":R1})
  transform_candidates.append({"T":T2, "R":R2})
  """ END YOUR CODE
  """
  return transform_candidates