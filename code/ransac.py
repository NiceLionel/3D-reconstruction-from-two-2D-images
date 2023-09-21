from lse import least_squares_estimation
import numpy as np

def ransac_estimator(X1, X2, num_iterations=60000):
    sample_size = 8

    eps = 10**-4

    best_num_inliers = -1
    best_inliers = None
    best_E = None

    for i in range(num_iterations):
        # permuted_indices = np.random.permutation(np.arange(X1.shape[0]))
        permuted_indices = np.random.RandomState(seed=(i*10)).permutation(np.arange(X1.shape[0]))
        sample_indices = permuted_indices[:sample_size]
        test_indices = permuted_indices[sample_size:]

        """
        X1_sample = X1[sample_indices]
        X1_test = X1[test_indices]
        X2_sample = X2[sample_indices]
        X2_test = X2[test_indices]

        E = least_squares_estimation(X1_sample,X2_sample)
        E1 = least_squares_estimation(X2_sample,X1_sample)

        inliers = sample_indices
        error = 10**(-4)

        for indice in range(test_indices.shape[0]):
            index = test_indices[indice]
            cur_residual = residual(X1[index],X2[index],E,E1)
            if (cur_residual<error):
                inliers = np.append(inliers,index).astype(int)
        """
        if inliers.shape[0] > best_num_inliers:
            best_num_inliers = inliers.shape[0]
            best_E = E
            best_inliers = inliers

    return best_E, best_inliers

def residual(X1,X2,E1,E2):
    e3 = [0,0,1]
    e3_hat = np.array([[0, -e3[2], e3[1]],
                       [e3[2], 0, -e3[0]],
                       [-e3[1], e3[0], 0]])
    deno_1 = (X2 @ E1 @ X1)**2
    num_1 = (np.linalg.norm(e3_hat@E1@X1))**2
    dist_1 = deno_1/num_1

    deno_2 = (X1 @ E2 @ X2)**2
    num_2 = (np.linalg.norm(e3_hat@E2@X2))**2
    dist_2 = deno_2/num_2

    dist = dist_1 + dist_2
    return dist
