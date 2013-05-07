conways
=======

A command-line implementation of Conway's Game of Life. Tested on Python 2.7.3
and Python 3.2.3.

Examples
--------
* [Screenshot](http://i.imgur.com/8G53a1o.jpg)
* [Video](http://www.youtube.com/watch?v=MK-_l4czzuU)

Setup
-----

    git clone git://github.com/hph/conways.git
    cd conways
    sudo cp conways.py /usr/local/bin/conways

Usage
-----
Simply run `conways` to execute the program with the default options. For full
list of options run `conways -h`:

    usage: conway [-h] [--width WIDTH] [--height HEIGHT] [--chance CHANCE]
                  [--fps FPS] [--no-clear]

    Visualize Conway's Game of Life with a command-line interface.

    optional arguments:
      -h, --help       show this help message and exit
      --width WIDTH    Number of columns in the grid. The default is 40.
      --height HEIGHT  Number of rows in the grid. The default is 21.
      --chance CHANCE  Denotes the chance for a living cell in each grid
                       coordinate. The default is 0.5.
      --fps FPS        The number of generations per second. The default is 4.0.
      --no-clear       Do not clear previous generations.
