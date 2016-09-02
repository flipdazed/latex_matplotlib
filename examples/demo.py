import matplotlib.pyplot as plt
import numpy as np

plt.ion()
plt.show()
x = np.linspace(-10,10,1000)
y = lambda x, m, s: np.exp(-(x-m)**2/s**2)/np.sqrt(2.*np.pi*s**2)
fig,ax = plt.subplots(1)
ax.plot(x,y(x,0,1), color='red', linewidth=2.0, alpha=0.7)
ax.plot(x,y(x,0,2.), color='green', linewidth=2.0, alpha=0.7, label='Im a legend')
ax.legend(loc=(0.2,0.5), shadow=True, fancybox=True) # make exact location of legend
ax.legend(loc='best', shadow=True, fancybox=True) # auto place
ax.set_xlabel("x")
ax.set_ylabel("y")

# this is my super uber LaTeXifying script
# you need latex installed for this to work
from latex_matplotlib import Pretty_Plotter
pp = Pretty_Plotter()
pp._teXify()
plt.draw()
# with latex must use r"" the 'r' infront makes python treat it as a literal
# string otherwise {} and \ are treated specially in Python

# now delete the last two lines
del ax.lines[-2:]
# and replot with LaTeX labels
ax.plot(x,y(x,0,1), color='red', linewidth=2.0, alpha=0.7, 
    label=r'$\mathbb{M}=0; \mathscr{S}=1$)')
ax.plot(x,y(x,0,2.), color='green', linewidth=2.0, alpha=0.7,
    label=r'$\mathbb{M}=0; \mathscr{S}=2$)')
    
# get new legend handle
ax.legend(loc='best', shadow=True, fancybox=True)

# redo the labels with LaTeX
ax.set_xlabel(r"I'm a $\vartheta$-axis")
ax.set_ylabel(r"$y(\vartheta, \mathscr{S}, \mathbb{M}) = \frac{1}{\sqrt{2\pi\mathscr{S}^2}} e^{-\frac{(\vartheta-\mathbb{M})^2}{\mathscr{S}^2}}$")

# add a title
ax.set_title(r"I use \LaTeX\ with fancy equations like $\iint dx d^{d-2}l \frac{-i}{(l^2-x)^2} \mathscr{G}(\vartheta)$")

# fig.suptitle('text') will also add a higher title

if __name__ == '__main__':
    # save if run directly
    import os,sys
    
    # get current directory location
    root = ''.join(os.path.split(sys.argv[0])[:-1])
    save_loc = os.path.join(root,'demo.png')
    
    # save the plot
    fig.savefig(save_loc)