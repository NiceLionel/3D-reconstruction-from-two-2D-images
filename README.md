**3D Reconstruction from 2D Images**

## Introduction

In this project, I ventured into the realm of 3D reconstruction using two 2D images. Leveraging computer vision techniques and tools, I transformed a pair of 2D images of a castle into a 3D miniature model. The key challenge was to determine the relative camera positions when the images were taken and subsequently construct the 3D scene.

The main tasks and highlights of this project include:

1. **3D Transformation Recovery**: I aimed to find the 3D transformation (R, T) between two views such that for two points \(P1, P2 in R^3) describing the same scene in frames 1 and 2, we have \(P2 = RP1 + T\).

2. **Estimation of the Essential Matrix**:
   - **Least-squares Estimation**: Implemented the 8-point algorithm to estimate the essential matrix \(E\) using the SVD decomposition method.
   - **RANSAC Estimation**: Enhanced the robustness of \(E\) estimation by implementing a basic RANSAC algorithm to counteract outliers from spurious matchings.
   - **Epipolar Line Drawing**: Using the essential matrix, I plotted the epipolar lines in both images to visualize the relationship between matched points.

3. **Pose Recovery & 3D Reconstruction**:
   - **Twisted Pair Ambiguity**: Explored the twisted pair ambiguity solutions for \(E\), resulting in four possible solutions for the transformation (R, T).
   - **Triangulation**: I triangulated points to find the intersection of rays from both cameras. Based on the four transformation candidates, I optimized the reconstruction by selecting the transformation where most of the 3D points were in front of both cameras.

4. **Reprojections**: A crucial part of validation, I compared original image points in one camera to the reprojections of image points from the other camera. This involved applying the camera projection model and understanding the transformation's expression between the two views.

**Tools & Packages**: This project was carried out in a Python environment, utilizing packages such as numpy, matplotlib, opencv-python, opencv-contrib-python, and jupyterlab.
