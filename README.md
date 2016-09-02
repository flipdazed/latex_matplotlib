Easily $\LaTeX$ `matplotlib` plots
===============

**Requirements**
 - `matplotlib`
 - `numpy` just for demos though but who doesn't have `numpy`!?
 - `LaTeX` this is kind of obvious - [get it here](https://www.latex-project.org/get/)
 - May work on `Windows`. If it doesn't get [`Ubuntu`](http://www.ubuntu.com/) like most other programmers!

## Contents
 - [Lazy Start](#ls)
 - [Not So Lazy Start](#nsls)
 - [Usage Examples](#e)

<a name="ls"/>
## Lazy Start
You're lazy and don't care about copying code from unknown sources? Just copy past all of this in a sensible location e.g. `~/Documents/pythonScripts/` and it will sort everything

    git clone https://github.com/flipdazed/latex_matplotlib.git
    LOC=$(pwd)
    echo 'export PYTHONPATH="'$LOC'/latex_matplotlib:$PYTHONPATH"' >> ~/.bash_profile
    source ~/.bash_profile

<a name="nsls"/>
## Not Lazy Start
You should probably read this...

Clone this repository

    git clone https://github.com/flipdazed/latex_matplotlib.git

delete the `.git` bit if you want no `git` history
    
    cd latex_matplotlib
    rm .git*

I'm too busy to properly package it for `pip` so to use it everywhere then in `bash` terminal

    
    export PYTHONPATH="/LOCATION/TO/latex_matplotlib:$PYTHONPATH"

where `/LOCATION/TO/` is the location to `latex_matplotlib` that can be found by typing `pwd` in the terminal.

This may be obvious but if you delete the directory it won't work anymore!

<a name="e"/>
##Usage Examples
The following example is found in `examples/basic.py`

    
    import matplotlib.pyplot as plt
    from latex_matplotlib import Pretty_Plotter
    import numpy as np
    
    pp = Pretty_Plotter()
    
    t = np.linspace(0,np.pi*2,1000)
    f = np.cos(t)+np.sqrt(3.)*np.cos(t)**2
    plt.plot(t,f, label=r'$\cos{\vartheta}+\sqrt{3}\cos^2{\vartheta}$')
    
    plt.title(r"I'm using \LaTeX !")
    plt.ylabel(r'$f(\vartheta)$')
    plt.xlabel(r'$\vartheta$')
    plt.legend(loc='best', shadow=True, fancybox=True)
    plt.show()

to give the following figure

![basic](examples/basic.png)

a more exciting example can be found in `examples/demo.py` which gives

![demo](examples/demo.png)