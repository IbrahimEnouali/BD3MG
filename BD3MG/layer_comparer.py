import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy.io import loadmat

input_file_name = "FlyBrain"
input_file_key = "I"
output_file_name = "y_restaured"
output_file_key = "y"

input_mat = loadmat(input_file_name)[input_file_key]
output_mat = loadmat(output_file_name)[output_file_key]

def get_plot_data(mat, layer):
    return mat[:,:,layer]

init_layer = 12
max_layer = min(input_mat.shape[2], output_mat.shape[2])

# Make a horizontal slider (taken from https://matplotlib.org/3.5.0/gallery/widgets/slider_demo.html)
fig, ax = plt.subplots()

plt.subplot(1, 2, 1)
ax_img_input = plt.imshow(get_plot_data(input_mat, init_layer), cmap="gray")

plt.subplot(1, 2, 2)
ax_img_output = plt.imshow(get_plot_data(output_mat, init_layer), cmap="gray")

plt.subplots_adjust(bottom=0.25)

axhor = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(
    ax=axhor,
    label='Layer (z)',
    valmin=0,
    valmax=max_layer,
    valstep=1,
    valinit=init_layer,
)

def update(val):
    ax_img_input.set_data(get_plot_data(input_mat, val))
    ax_img_output.set_data(get_plot_data(output_mat, val))

slider.on_changed(update)

plt.show()
