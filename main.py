import tkinter as tk
from tkinter import font, messagebox
import math
import numpy as np

# Initialize the main window
root = tk.Tk()
root.title("Eigenvalues and Eigenvectors Calculator")
root.geometry("600x400")
root.configure(bg="grey6")

# Set predefined fonts
f = font.Font(family='Century Gothic', size=15, weight="bold")
f2 = font.Font(family='Cambria', size=12, weight="bold")
f3 = font.Font(size=10, weight="bold")
f4 = font.Font(size=12, weight="bold")
f5 = font.Font(size=11)

# Labels and entry boxes for matrix input
tk.Label(root, text="  Enter the elements of the 3x3 matrix:", fg='white', bg='grey6', font=f2).grid(row=0, column=0, columnspan=3, pady=10)

entries = []
for i in range(3):
    row_entries = []
    for j in range(3):
        entry = tk.Entry(root, width=5, font=f2)
        entry.grid(row=i+1, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entries.append(row_entries)

# Function to fetch matrix values from entry boxes
def get_matrix_from_entries():
    matrix = []
    for row_entries in entries:
        row = []
        for entry in row_entries:
            try:
                row.append(float(entry.get()))
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter valid numbers.")
                return None
        matrix.append(row)
    return matrix

# Check if matrix is symmetric
def is_symmetric(matrix):
    return np.allclose(matrix, np.transpose(matrix))

# Calculate the determinant of a matrix
def calculate_determinant(matrix):
    return np.linalg.det(matrix)

# Eigenvalues and eigenvectors calculation
def maxOffDig(m):
    n = len(m)
    a = m[0][0]
    mr = 0
    mc = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a < m[i][j]:
                a = m[i][j]
                mr = i
                mc = j
    return mr, mc

def inrotm(r):
    ir = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            ir[j][i] = r[i][j]
    return ir

def multy(m, r):
    ans = [[0]*3 for _ in range(3)]
    for i in range(0, 3):
        for j in range(0, 3):
            v = 0.0
            for k in range(0, 3):
                v += m[i][k] * r[k][j]
            ans[i][j] = v
    return ans

def sc(t2):
    r = 1 / t2
    r1 = -r + math.sqrt(r*r + 1)
    c = 1 / (math.sqrt(1 + r1*r1))
    s = r1 * c
    return s, c

def rotm(mr, mc, s, c):
    r = [[0]*3 for _ in range(3)]
    r[mr][mc] = s
    r[mc][mr] = -s
    r[mr][mr] = c
    r[mc][mc] = c
    r[3-mc-mr][3-mr-mc] = 1
    return r

def calculate_eigenvalues_eigenvectors(matrix):
    m = matrix
    q = [[0]*3 for _ in range(3)]
    f = 0
    mr, mc = maxOffDig(m)

    while m[mr][mc] > 0.001 or m[mr][mc] < -0.001:
        if m[mc][mc] - m[mr][mr] == 0:
            s = 1 / math.sqrt(2)
            c = 1 / math.sqrt(2)
        else:
            t2 = (2 * m[mr][mc]) / (m[mc][mc] - m[mr][mr])
            s, c = sc(t2)

        r = rotm(mr, mc, s, c)
        if f == 0:
            for i in range(3):
                for j in range(3):
                    q[i][j] = r[i][j]
        else:
            q = multy(q, r)

        ir = inrotm(r)
        p = multy(ir, m)
        n = multy(p, r)
        for i in range(3):
            for j in range(3):
                m[i][j] = n[i][j]
        mr, mc = maxOffDig(m)
        f += 1

    eigenvalues = [m[i][i] for i in range(3)]
    eigenvectors = q
    return eigenvalues, eigenvectors

def display_results(eigenvalues, eigenvectors):
    results_frame = tk.Frame(root, bg='grey6')
    results_frame.grid(row=6, column=0, columnspan=3, pady=10)

    # Eigenvalues heading
    tk.Label(results_frame, text="Eigenvalues:", fg='red', bg='grey6', font=f).grid(row=0, column=0, columnspan=3)
    for i, val in enumerate(eigenvalues):
        tk.Label(results_frame, text=f"{val:.2f}", fg='white', bg='grey6', font=f4).grid(row=1, column=i, padx=10)

    # Eigenvectors heading
    tk.Label(results_frame, text="Eigenvectors:", fg='red', bg='grey6', font=f).grid(row=2, column=0, columnspan=3)
    for i in range(3):
        for j in range(3):
            tk.Label(results_frame, text=f"{eigenvectors[j][i]:.2f}", fg='white', bg='grey6', font=f4).grid(row=3+i, column=j, padx=10)

# Button to trigger calculation
def calculate():
    matrix = get_matrix_from_entries()
    if matrix:
        if not is_symmetric(matrix):
            messagebox.showerror("Matrix Error", "The matrix is not symmetric.")
            return
        if calculate_determinant(matrix) == 0:
            messagebox.showerror("Matrix Error", "The matrix is not orthogonal.")
            return

        eigenvalues, eigenvectors = calculate_eigenvalues_eigenvectors(matrix)
        display_results(eigenvalues, eigenvectors)

calculate_button = tk.Button(root, text="CALCULATE", fg="red", bg="white", command=calculate)
calculate_button['font'] = f
calculate_button.grid(row=5, column=0, columnspan=3, pady=20)

# Run the main event loop
root.mainloop()
