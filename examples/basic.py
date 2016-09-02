import matplotlib.pyplot as plt
from latex_matplotlib import Pretty_Plotter
import numpy as np

# super uber latexifying
pp = Pretty_Plotter()

# plot
t = np.linspace(0,np.pi*2,1000)
f = np.cos(t)+np.sqrt(3.)*np.cos(t)**2
plt.plot(t,f, label=r'$\cos{\vartheta}+\sqrt{3}\cos^2{\vartheta}$')

# add niceities
plt.title(r"I'm using \LaTeX !")
plt.ylabel(r'$f(\vartheta)$')
plt.xlabel(r'$\vartheta$')
plt.legend(loc='best', shadow=True, fancybox=True)
plt.show()

if __name__ == '__main__':
    # save if run directly
    import os,sys

    # get current directory location
    root = ''.join(os.path.split(sys.argv[0])[:-1])
    save_loc = os.path.join(root,'basic.png')
    
    # save the plot
    plt.savefig(save_loc)