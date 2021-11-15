*mcd_python* (git branch *vcd*) is the web interface of the VCD.
It is based (as a submodule) on *mcd-python* (git branch [vcd_py2.7](https://github.com/aymeric-spiga/mcd-python/tree/vcd_py2.7))
which is the Python interface to the VCD Fortran sources

Based on the MCD version (git branch [master](https://github.com/aymeric-spiga/mcd_python/tree/master)).
***WARNING:***
To keep track of changes between the git branches,
we keep the file names `index5.html`, `martian_time.js` and `cgi-bin/mcdcgi.py` as such, at least for now.
Every instance of `"mcd"` other than in these 3 file names is replaced by its `"vcd"` counterpart.

--- get sources

use
```git clone --recursive```
to get submodule mcd-python

--- instructions

* get VCD sources and data somewhere
* (if needed) compile netCDF in netcdf/
* adapt the header of fmcd_compile.sh in cgi-bin/modules
* compile VCD with fmcd_compile.sh in cgi-bin/modules
* start a server (where index.html is) with one of the script in minimal_cgi_python
* visit localhost:8080 with local browser

