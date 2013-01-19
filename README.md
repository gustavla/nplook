nplook
======

Command-line tool that peeks into a numpy `npy` or `npz` file and summarizes its contents.

quick install
-------------

    [sudo] pip install nplook

If you don't want pip to try to upgrade your numpy, you might want to do

    [sudo] pip install --no-deps nplook

install from github
-------------------

    git clone git://github.com/gustavla/nplook.git 
    cd nplook
    [sudo] python setup.py install

usage
-----

    $ nplook output.npz
    -> output.npz
       templates : ndarray (9, 64, 64) [float64]
         weights : ndarray (9,) [float64]
