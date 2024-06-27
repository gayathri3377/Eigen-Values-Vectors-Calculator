# Eigenvalues and Eigenvectors Calculator with Tkinter

## Overview

The Eigenvalues and Eigenvectors Calculator with Tkinter is a Python application that provides an interactive interface to calculate the eigenvalues and eigenvectors of a 3x3 matrix using the Jacobi method.The inspiration for this project stemmed from my coursework in Computational Physics.

<div style="display:flex; justify-content:space-around;">
    <img src="https://github.com/gayathri3377/Movies-App/assets/152592583/a77af675-c839-46ab-b1ac-f5afe5588e74" alt="Display" style="width:200px;">
    <img src="https://github.com/gayathri3377/Movies-App/assets/152592583/72b5c17d-4953-4585-9c6a-7de38cd27e00" alt="Result" style="width:200px;">
    <img src="https://github.com/gayathri3377/Movies-App/assets/152592583/c62b3103-a9b7-4309-ad01-8c536ecae3aa" alt="Error" style="width:200px;">
</div>

## Features

- **Graphical User Interface (GUI):** Built using Tkinter to offer a user-friendly environment for matrix input and result display.
- **Matrix Input:** Users can input the elements of a 3x3 matrix using entry boxes provided in the interface.
- **Symmetry Check:** Validates if the entered matrix is symmetric using NumPy's `np.allclose` function.
- **Eigenvalue Calculation:** Computes eigenvalues iteratively until convergence using rotation matrices and the Jacobi method.
- **Eigenvector Calculation:** Calculates corresponding eigenvectors using transformation matrices derived during eigenvalue computation.
- **Result Display:** Displays computed eigenvalues and corresponding eigenvectors in a structured format within the GUI.

## Modules Used

- **Tkinter:** Used for building the GUI and handling user interactions.
- **numpy:** Utilized for matrix operations and checking symmetry.
- **math:** Provides mathematical functions required for calculations.
- **tkinter.font:** Used to define and customize fonts for labels and buttons.
- **tkinter.messagebox:** Enables displaying error messages for invalid input or matrix properties.

### Eigenvalues and Eigenvectors

Eigenvalues are scalar values associated with linear systems, particularly in matrix equations. They represent the values λ for which the equation 
Ax=λx holds true, where A is a matrix and x is a non-zero vector known as an eigenvector.
Eigenvectors are non-zero vectors that, when transformed by a given matrix, retain their direction but are scaled by a scalar factor known as the eigenvalue. They provide insights into the direction of the transformation represented by the matrix. More details can be found in the [Wikipedia article on Eigenvalues and Eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors).

### Jacobi Method

The Jacobi method is an iterative algorithm used to compute eigenvalues and eigenvectors of a real symmetric matrix. It involves a series of rotations (using orthogonal matrices) applied to the original matrix until convergence is achieved. This method is effective for symmetric matrices due to their special properties, including real eigenvalues and orthogonal eigenvectors. Learn more from the [Wikipedia article on the Jacobi eigenvalue algorithm](https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm).

## Input Restrictions

- **Symmetric Matrix:** The application requires the input matrix to be symmetric for accurate eigenvalue and eigenvector computation. A symmetric matrix satisfies \( A = A^T \), where \( A^T \) denotes the transpose of matrix \( A \).
- **Non-singular Matrix:** To ensure the matrix has an inverse, the determinant must be non-zero. A matrix with zero determinant is singular and cannot have an inverse.

## Error Handling

- **Invalid Input:** If non-numeric values are entered into the matrix input fields, the application displays an error message prompting the user to correct the input.
- **Matrix Properties:** Error messages are shown if the matrix fails the symmetry check or has a determinant of zero, indicating it is not suitable for eigenvalue computation.
