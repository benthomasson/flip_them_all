===============================
Flip Them All
===============================

A small program that uses ffmpeg to flip all the videos in one directory with output files in another directory.
This utility will not process files that have already been processed and exist in the output directory.


Installation
------------

::

    virtualenv env
    source env/bin/activate
    pip install .

Usage
-------

::

    source env/bin/activate
    flip_them_all to_be_flipped already_flipped


