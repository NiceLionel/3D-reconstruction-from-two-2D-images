import numpy as np

def reconstruct3D(transform_candidates, calibrated_1, calibrated_2):
  """This functions selects (T,R) among the 4 candidates transform_candidates
  such that all triangulated points are in front of both cameras.
  """

  best_num_front = -1
  best_candidate = None
  best_lambdas = None
  for candidate in transform_candidates:
    R = candidate['R']
    T = candidate['T']

    lambdas = np.zeros((2, calibrated_1.shape[0]))
    """
    for i in range(len(calibrated_1)):
        x1_coord = calibrated_1[i]
        x2_coord = calibrated_2[i]
        X1 = np.array([[x1_coord[0]],
                        [x1_coord[1]],
                        [x1_coord[2]]])
        X2 = np.array([[x2_coord[0]],
                        [x2_coord[1]],
                        [x2_coord[2]]])
        R1 = -R @ X1
        A = np.concatenate([X2,R1],1)
        Tt = np.array([[T[0]],
                      [T[1]],
                      [T[2]]])
        pinv_A = np.linalg.pinv(A)
        depth = pinv_A @ Tt
        lambdas[0,i], lambdas[1,i] = depth[0], depth[1]
    """
    num_front = np.sum(np.logical_and(lambdas[0]>0, lambdas[1]>0))

    if num_front > best_num_front:
      best_num_front = num_front
      best_candidate = candidate
      best_lambdas = lambdas
      print("best", num_front, best_lambdas[0].shape)
    else:
      print("not best", num_front)


  P1 = best_lambdas[1].reshape(-1, 1) * calibrated_1
  P2 = best_lambdas[0].reshape(-1, 1) * calibrated_2
  T = best_candidate['T']
  R = best_candidate['R']
  return P1, P2, T, R
