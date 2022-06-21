import matplotlib.pyplot as plt
from scipy.io import loadmat

def plot_mat(mat_file_name, mat_file_key, output_file_name, layer=-1):
    """
        plot a .mat file to a .png file
        Use layer = -1 to keep the entire mat file
    """
    y = loadmat(mat_file_name)[mat_file_key]
    if layer != -1: y = y[:,:,layer]
    else: y = y.sum(axis=2)

    plt.imshow(y, cmap="gray")
    plt.savefig(output_file_name)