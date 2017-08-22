Worldmap
========

Expert Analytics playtoy for creating world maps using Bokeh.

Installation
------------

`worldmap` requires that GDAL is installed in the system before installation.

On Ubuntu/Debian version before 17.04, the APT repository needs to be updated::

    $ sudo add-apt-repository ppa:ubuntugis/ppa

To install system requirements::

    $ sudo apt update
    $ sudo apt install gdal-bin libgdal-dev

To install python requirements and install package::

    $ pip install -r requirements.txt
    $ python setup.py install

To verify that everything works as expeced, run the following::

    $ python -c "from worldmap import DTM; DTM()"

If no errors is thrown, the package is installed successfully.

