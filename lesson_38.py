import numpy as np

# Our image processing tools
import skimage.filters
import skimage.io
import skimage.morphology
import skimage.exposure

import matplotlib.pyplot as plt
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

# Load the phase contrast image.
im_phase = skimage.io.imread('data/bsub_100x_phase.tif')
cfp_im = skimage.io.imread('data/bsub_100x_cfp.tif')


# Display the image, set Seaborn style 'dark' to avoid grid lines
with sns.axes_style('dark'):
    skimage.io.imshow(im_phase)

# Display the image
with sns.axes_style('dark'):
    skimage.io.imshow(im_phase / im_phase.max())

# Show the phase image.
plt.imshow(im_phase, cmap=plt.cm.Greys_r)
plt.close()

# Plot the histogram of the phase image.
# Get the histogram data
hist_phase, bins_phase = skimage.exposure.histogram(im_phase)
plt.plot(bins_phase, hist_phase)

# Use matplotlib to make a pretty plot of histogram data
plt.fill_between(bins_phase, hist_phase, alpha=0.5)

# Label axes
plt.xlabel('pixel value')
plt.ylabel('count')

# Threshold value, as obtained by eye
thresh_phase = 280

# Generate thresholded image
im_phase_bw = im_phase < thresh_phase

with sns.axes_style('dark'):
    plt.imshow(im_phase_bw, cmap=plt.cm.Greys_r)

# Show the fluorescence image.
with sns.axes_style('dark'):
    plt.imshow(cfp_im, cmap=plt.cm.viridis)

# Slice out region with hot pixel
plt.close()
with sns.axes_style('dark'):
    plt.imshow(cfp_im[150:250, 450:550]/cfp_im.max(), cmap=plt.cm.viridis)


# Make the structuring element
selem = skimage.morphology.square(3)

# Perform the median filter
im_cfp_filt = skimage.filters.median(cfp_im, selem)

# Show filtered image with the viridis LUT.
with sns.axes_style('dark'):
    plt.imshow(im_cfp_filt, cmap=plt.cm.viridis)
    plt.colorbar()

# Same as before, but zoomed in.
with sns.axes_style('dark'):
    plt.imshow(im_cfp_filt[150:250, 450:550], cmap=plt.cm.viridis)
    plt.colorbar()

# Look at the histogram of the median filtered image.
# Get the histogram data
hist_cfp, bins_cfp = skimage.exposure.histogram(im_cfp_filt)
plt.close()

# Use matplotlib to make a pretty plot of histogram data
plt.fill_between(bins_cfp, hist_cfp, alpha=0.5)
plt.plot([115, 115], [0, 500000], 'r-')

# Label axes
plt.xlabel('pixel value')
plt.ylabel('count')

# Threshold value, as obtained by eye
thresh_cfp = im_cfp_filt > 120
plt.close()
with sns.axes_style('dark'):
    plt.imshow(thresh_cfp, cmap=plt.cm.Greys_r)

# Aplly an otsu threshold.
phase_thresh = skimage.filters.threshold_otsu(im_phase)
cfp_thresh = skimage.filters.threshold_otsu(im_cfp_filt)
phase_otsu = im_phase < phase_thresh
cfp_otsu = im_cfp_filt > cfp_thresh

with sns.axes_style('dark'):
    plt.figure()
    plt.imshow(phase_otsu, cmap=plt.cm.Greys_r)
    plt.title('phase otsu')

    plt.figure()
    plt.imshow(cfp_otsu, cmap=plt.cm.Greys_r)
    plt.title('cfp otsu')
