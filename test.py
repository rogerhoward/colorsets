#!/usr/bin/env python
import click
from module import ColorSet
from pprint import pprint

#------------------------------------------------#
#  Command line options                          #
#------------------------------------------------#
@click.command()
@click.option('--colors', default=3, help='Number of colors to generate.')
def main(colors):
    this_set = ColorSet(colors)
    pprint(this_set.in_rgb)



if __name__ == '__main__':
    main()