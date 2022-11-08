# Simple Corba Python Program
1) Download OmniORB and OmniORBpy: </br>
    * wget http://downloads.sourceforge.net/project/omniorb/omniORB/omniORB-4.1.6/omniORB-4.1.6.tar.bz2 
    * wget http://downloads.sourceforge.net/project/omniorb/omniORBpy/omniORBpy-3.6/omniORBpy-3.6.tar.bz2 

2) Extract OmniORB and OmniORBpy: </br>
    * tar -xjvf omniORB-4.1.6.tar.bz2
    * tar -xjvf omniORBpy-3.6.tar.bz2

3) Install OmniOrb: </br>
    * mkdir omniORB-4.1.6/build
    * cd omniORB-4.1.6/build
    * ../configure
    * make
    * sudo make install

4) Install OmniOrbPY:</br>
    * cd -
    * mkdir omniORBpy-3.6/build
    * cd omniORBpy-3.6/build
    * ../configure
    * make
    * make install


5) Download rep


7) Run server
   * python3 server.py
   * copy IOR (it's needed to connect to the server)


8) Run client 
   * python3 client.py (put IOR)
   * client is a simple calculator 


9) Program idea
   * takes values from the client 
   * pass them to the server
   * do some math and return result
