# Simple Corba Python Program
1) Download OmniORB and OmniORBpy extension: </br>
    $> wget http://downloads.sourceforge.net/project/omniorb/omniORB/omniORB-4.1.6/omniORB-4.1.6.tar.bz2 </br>
    $> wget http://downloads.sourceforge.net/project/omniorb/omniORBpy/omniORBpy-3.6/omniORBpy-3.6.tar.bz2 </br>

2) Extract OmniORB and OmniORBpy:</br>
    $> tar -xjvf omniORB-4.1.6.tar.bz2</br>
    $> tar -xjvf omniORBpy-3.6.tar.bz2</br>

3) Install OmniOrb (installs to /usr/local by default):</br>
    $> mkdir omniORB-4.1.6/build</br>
    $> cd omniORB-4.1.6/build</br>
    $> ../configure</br>
    $> make</br>
    $> sudo make install</br>

4) Install OmniOrbPY (with path to your virtualenv, which you really should use):</br>
    $> cd -</br>
    $> mkdir omniORBpy-3.6/build</br>
    $> cd omniORBpy-3.6/build</br>
    $> ../configure --prefix=<path-to-your-virtualenv> --with-omniorb=/usr/local (or wherever you put it in step 3)</br>
    $> make</br>
    $> make install</br>
