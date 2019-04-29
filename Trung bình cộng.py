import matplotlib.pyplot as plt
import os
import numpy as np
import gzip

def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path, '%s-labels-idx1-ubyte.gz' % kind)
    images_path = os.path.join(path, '%s-images-idx3-ubyte.gz' % kind)
    
    with gzip.open(labels_path, 'rb') as lbpath:
        lbpath.read(8)
        buffer = lbpath.read()
        labels = np.frombuffer(buffer, dtype=np.uint8)
    with gzip.open(images_path, 'rb') as imgpath:
        imgpath.read(16)
        buffer = imgpath.read()
        images = np.frombuffer(buffer, dtype=np.uint8).reshape(len(labels), 28, 28).astype(np.float64)
    
    return images, labels

X_train, y_train = load_mnist('data/', kind='train')

u=0
for q in range(0,60000):
    for w in range(0,7):
        w*=4
        for e in range(0,7):
            e*=4
            for r in range(w,w+4):
                for t in range(e,e+4):
                    u += X_train[q][r][t]
            X_train[q][w][e]=u/16
            u=0
for q in range(0,60000):
    for w in range(0,7):
        for e in range(0,7):
            X_train[q][w][e]=X_train[q][w*4][e*4]

A=[]
for i in range(0,60000):
    A.append([])
    for j in range(0,7):
        A[i].append([])
        for k in range(0,7):
            A[i][j].insert(k,X_train[i][j][k])
            
B=np.array(A)


print('Rows: %d, columns: %d' % (B.shape[0], B.shape[1]))

fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True,)
ax = ax.flatten()
for i in range(10):
    img = B[y_train == i][0]
    ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    
ax[0].set_xticks([])
ax[0].set_yticks([])
plt.tight_layout()
plt.show()
B=B.reshape(60000,-1)

            
            
