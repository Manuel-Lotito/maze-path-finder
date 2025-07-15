import tkinter as tk

def change_cell(matrix, i, j):
    if matrix[i][j] == "#":
        matrix[i][j] = " "
    else:
        matrix[i][j] = "#"

def clear_matrix(matrix, start, end):
    start_pos = matrix[start[1]][start[0]]
    end_pos = matrix[end[1]][end[0]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] not in [start_pos, end_pos]:
                matrix[i][j] = " "


    