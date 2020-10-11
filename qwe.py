
import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import rand
from pylab import figure
import helper


def random_point_ellipsoid(a, b, c):
    u = np.random.rand()
    v = np.random.rand()
    theta = u * 2.0 * np.pi
    phi = np.arccos(2.0 * v - 1.0)
    sinTheta = np.sin(theta);
    cosTheta = np.cos(theta);
    sinPhi = np.sin(phi);
    cosPhi = np.cos(phi);
    rx = a * sinPhi * cosTheta;
    ry = b * sinPhi * sinTheta;
    rz = c * cosPhi;
    return rx, ry, rz


def qwe(matrix):

    m = np.asarray(matrix)
    fig = figure()
    ax = Axes3D(fig)

    for i in range(len(m)):  # plot each point + it's index as text above
        ax.scatter(m[i, 0], m[i, 1], m[i, 2], color='b')
        z = [m[i, 0], m[i, 1], m[i, 2]]
        # ax.text(m[i, 0], m[i, 1], m[i, 2], '%s' % (str(m[i, 2])), size=20, zorder=1,
        #         color='k')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    pyplot.show()



if __name__ == '__main__':
    qwe()