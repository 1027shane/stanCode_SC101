"""
File: hole_puncher.py
Name: Shane Liu
-------------------------
This file shows how to use campy mouse event to punch holes(GOval)
on GWindow.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 30

# Global variable
window = GWindow()


def main():
	onmouseclicked(create_hole)


def create_hole(mouse):
	hole = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
	hole.filled = True
	hole.fill_color = 'Green'
	window.add(hole)


if __name__ == '__main__':
	main()
