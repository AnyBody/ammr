import matplotlib.pyplot as plt
import matplotlib.image as mimg
import numpy as np

def plot(image_name, dpi=200):
    image = mimg.imread(image_name)
    #px,py,  = image.shape # depending of your matplotlib.rc you may have to use py,px instead
    px,py = image[:,:,0].shape # if image has a (x,y,z) shape 
    size = (py/np.float(dpi), px/np.float(dpi)) # note the np.float()

    fig = plt.figure(figsize=size, dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    # Customize the axis
    # remove top and right spines
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    # turn off ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])

    ax.imshow(image)
    
def show():
    plt.show()