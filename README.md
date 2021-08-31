*mcd_python* is the web interface of the MCD
it is based (as a submodule) on *mcd-python*
which is the Python interface to the MCD Fortran sources

--- get sources

use
```git clone --recursive```
to get submodule mcd-python

--- instructions

* get MCD sources and data somewhere
* (if needed) compile netCDF in netcdf/
* adapt the header of fmcd_compile.sh in cgi-bin/modules
* compile MCD with fmcd_compile.sh in cgi-bin/modules
* start a server (where index.html is) with one of the script in minimal_cgi_python
* visit localhost:8080 with local browser

