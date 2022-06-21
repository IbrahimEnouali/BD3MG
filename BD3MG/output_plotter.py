import os
from mat_plotter import plot_mat

mat_file_name = os.getcwd() + "/outputs/y_restaured.mat"
mat_file_key = "y"
output_file_name =  "y_restaured_image.png"

plot_mat(mat_file_name, mat_file_key, output_file_name)