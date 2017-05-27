import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat-bungy.jpg')
img = cv2.resize(img, (256, 256))
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

chans = cv2.split(hsv_image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
features = []
bins = [180, 256, 256]
ranges = [[0, 179], [0, 255], [0, 255]]

# loop over the image channels
for (chan, color, bin, range) in zip(chans, colors, bins, ranges):

    hist = cv2.calcHist([chan], [0], None, [bin], range)
    features.extend(hist)

    # plot the histogram
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
plt.show()
#
# fig = plt.figure()
# ax = p3.Axes3D(fig)
h_ = cv2.calcHist(hsv_image, [0], None, [180], [0, 179])
v_ = cv2.calcHist(hsv_image, [1], None, [256], [0, 255])
i_ = cv2.calcHist(hsv_image, [2], None, [256], [0, 255])
ax.scatter(h_, v_, i_, s=5, c=[r, g, b], lw=0)

plot_surface(h_, v_, i_, cmap=cm.coolwarm, linewidth=0, antialiased=False)
plt.show()
