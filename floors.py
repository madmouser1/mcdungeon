import materials
import random
from mymath import * 

class Blank(object):
	_name = 'Blank'
	def __init__ (self, parent):
		self.parent = parent
	def render (self):
		pass
		
class Cobble(Blank):
	_name = 'Cobble'
	def render (self):
		if (sum_points_inside_flat_poly(*self.parent.canvas) > 0):
			for x in iterate_points_inside_flat_poly(*self.parent.canvas):
				self.parent.parent.setblock(x+self.parent.loc, materials.Cobblestone)

class DoubleSlab(Blank):
	_name = 'DoubleSlab'
	def render (self):
		if (sum_points_inside_flat_poly(*self.parent.canvas) > 0):
			for x in iterate_points_inside_flat_poly(*self.parent.canvas):
				self.parent.parent.setblock(x+self.parent.loc, materials.DoubleSlab)

class WoodTile(Blank):
	_name = 'WoodTile'
	def render (self):
		if (sum_points_inside_flat_poly(*self.parent.canvas) > 0):
			for x in iterate_points_inside_flat_poly(*self.parent.canvas):
				if ((x.x+x.z)&1 == 1):
					self.parent.parent.setblock(x+self.parent.loc, materials.Wood)
				else:
					self.parent.parent.setblock(x+self.parent.loc, materials.WoodPlanks)
					
class CheckerRug(Blank):
	_name = 'CheckerRug'
	colors = (
		(7,8),   # dark grey / light grey
		(9,3),   # cyan / light blue
		#(14,10), # red / purple
		(11,9),  # dark blue / cyan
		(1,14),  # red / orange
		(7,15),  # dark grey / black
		(3,4),   # light blue  / yellow
		(11,10), # dark blue  / purple
		(12,13), # brown  / dark green
		(15,13), # black  / dark green
		(1,14)   # red / orange
		)
	def render (self):
		if (sum_points_inside_flat_poly(*self.parent.canvas) > 0):
			color = random.choice(self.colors)
			for x in iterate_points_inside_flat_poly(*self.parent.canvas):
				self.parent.parent.setblock(x+self.parent.loc, materials.Wool)
				if ((x.x+x.z)&1 == 1):
					self.parent.parent.blocks[x+self.parent.loc].data = color[0]
				else:
					self.parent.parent.blocks[x+self.parent.loc].data = color[1]

def new (name, parent):
        if (name == 'Cobble'):
                return Cobble(parent)
        if (name == 'DoubleSlab'):
                return DoubleSlab(parent)
        if (name == 'WoodTile'):
                return WoodTile(parent)
        if (name == 'CheckerRug'):
                return CheckerRug(parent)
        return Blank(parent)