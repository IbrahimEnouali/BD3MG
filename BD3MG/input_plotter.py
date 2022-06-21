import os
from mat_plotter import plot_mat

mat_file_name = os.getcwd() + "/Images/FlyBrain.mat"
mat_file_key = "I"
output_file_name =  "input_image.png"
layer = 16

plot_mat(mat_file_name, mat_file_key, output_file_name, layer)