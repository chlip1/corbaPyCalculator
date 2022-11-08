# Simple Corba Python Program
1) Download OmniORB and OmniORBpy extension:
    $> wget http://downloads.sourceforge.net/project/omniorb/omniORB/omniORB-4.1.6/omniORB-4.1.6.tar.bz2
    $> wget http://downloads.sourceforge.net/project/omniorb/omniORBpy/omniORBpy-3.6/omniORBpy-3.6.tar.bz2

2) Extract OmniORB and OmniORBpy:
    $> tar -xjvf omniORB-4.1.6.tar.bz2
    $> tar -xjvf omniORBpy-3.6.tar.bz2

3) Install OmniOrb (installs to /usr/local by default):
    $> mkdir omniORB-4.1.6/build
    $> cd omniORB-4.1.6/build
    $> ../configure
    $> make
    $> sudo make install

4) Install OmniOrbPY (with path to your virtualenv, which you really should use):
    $> cd -
    $> mkdir omniORBpy-3.6/build
    $> cd omniORBpy-3.6/build
    $> ../configure --prefix=<path-to-your-virtualenv> --with-omniorb=/usr/local (or wherever you put it in step 3)
    $> make
    $> make install
