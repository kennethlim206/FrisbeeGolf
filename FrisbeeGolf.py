# Frisbee Golf World Championship
# By Justin Lim

from graphics import *
from random import randrange

# Class for buttons that ask for difficulty at the beginning of the game
class MapButton:
	def __init__(self, center, width, height, text):
		w, h = width/2.0, height/2.0
		self.xmin, self.xmax = center.getX() - w, center.getX() + w
		self.ymin, self.ymax = center.getY() - h, center.getY() + h
		self.rect = Rectangle(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))
		self.rect.setFill("white")
		self.text = Text(center, text)

	def draw(self, window):
		self.rect.draw(window)
		self.text.draw(window)
	
	def undraw(self, window):
		self.rect.undraw()
		self.text.undraw()
		
	# This method makes buttons flash red when they are clicked
	def clrclick(self):
		self.rect.setFill("red")
		self.rect.setFill("white")

	def clicked(self, p):
		return self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax

# Class for arrow key buttons
class DirectionButton:
	def __init__(self, center, width, height, text):
		w, h = width/2.0, height/2.0
		self.xmin, self.xmax = center.getX() - w, center.getX() + w
		self.ymin, self.ymax = center.getY() - h, center.getY() + h
		self.rect = Rectangle(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))
		self.rect.setFill("white")
		self.text = Text(center, text)

	def draw(self, window):
		self.rect.draw(window)
		self.text.draw(window)
	
	def undraw(self, window):
		self.rect.undraw()
		self.text.undraw()

	def clrclick(self):
		self.rect.setFill("red")
		self.rect.setFill("white")

	def clicked(self, p):
		return self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax
		
# Class for power buttons
class PowerButton:
	def __init__(self, center, width, height, text, power):
		w, h = width/2.0, height/2.0
		self.xmin, self.xmax = center.getX() - w, center.getX() + w
		self.ymin, self.ymax = center.getY() - h, center.getY() + h
		self.rect = Rectangle(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))
		self.rect.setFill("white")
		self.text = Text(center, text)
		self.power = power

	def draw(self, window):
		self.rect.draw(window)
		self.text.draw(window)

	def clicked(self, p):
		return self.xmin <= p.getX() <= self.xmax and self.ymin <= p.getY() <= self.ymax
		
	def getPower(self):
		return self.power
		
	def setFill(self, clr):
		self.rect.setFill(clr)
		
# Class for notes if players win/lose
class EndNote:
	def __init__(self, center, width, height, text, clr):
		w, h = width/2.0, height/2.0
		self.xmin, self.xmax = center.getX() - w, center.getX() + w
		self.ymin, self.ymax = center.getY() - h, center.getY() + h
		self.rect = Rectangle(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))
		self.rect.setFill(clr)
		self.text = Text(center, text)

	def draw(self, window):
		self.rect.draw(window)
		self.text.draw(window)

# Class for mountains, bunkers and lakes
class Obstacle:
	def __init__(self, center, width, height, clr):
		w, h = width/2.0, height/2.0
		self.xmin, self.xmax = center.getX() - w, center.getX() + w
		self.ymin, self.ymax = center.getY() - h, center.getY() + h
		self.rect = Rectangle(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))
		self.rect.setFill(clr)

	def draw(self, window):
		self.rect.draw(window)
	
	def undraw(self, window):
		self.rect.undraw()

	# Returns the boundary of an obstacle
	def stuck(self):
		return [self.xmin, self.xmax, self.ymin, self.ymax]
		
# Class for goal
class Hole:
	def __init__(self, centerx, centery, width, height):
		w, h = width/2.0, height/2.0
		self.xmin, self.xmax = centerx - w, centerx + w
		self.ymin, self.ymax = centery - h, centery + h
		self.ov = Oval(Point(self.xmin, self.ymin), Point(self.xmax, self.ymax))
		self.ov.setFill("yellow")

	def draw(self, window):
		self.ov.draw(window)
		
	def undraw(self, window):
		self.ov.undraw()
		
	def changeclr(self):
		self.pink = color_rgb(255, 105, 180)
		self.ov.setFill(self.pink)
		
	# Returns the boundary of the goal
	def ingoal(self):
		return [self.xmin, self.xmax, self.ymin, self.ymax]
	
# Class that keeps updates of frisbee position, crashes and scores
class Rules:
	def __init__(self, xval, yval, compx, compy):
		
		self.xval = xval    # User position
		self.yval = yval
		self.compx = compx  # Computer player position
		self.compy = compy
		self.movnum = 0     # User number of moves
		self.compmov = 0    # Computer number of moves
		
		self.scored = 0     # Becomes 1 if user scores
		self.cscored = 0    # Becomes 1 if computer scores
		self.crash = 0      # Becomes 1 if user crashes
		self.ccrash = 0
		self.bunked1 = 0    # Becomes value that frisbees are inhibited in bunkers
		self.bunked2 = 0
		self.bunked3 = 0
		self.cbunked1 = 0
		self.cbunked2 = 0
		self.offmap = 0     # Becomes 1 if user throws out of bounds
		self.coffmap = 0
		self.par = 0        # Keeps track of par for a particular map
	
	def getMovnum(self):
		return self.movnum
	
	# Keeps track of frisbee position
	def update(self, fwd, updown):
		self.fwd = fwd
		self.updown = updown
		self.xval = self.xval + self.fwd
		self.yval = self.yval + self.updown
		self.movnum = self.movnum + 1
	
	# Keeps track of computer player position
	def cupdate(self, cfwd, cupdown):
		self.cfwd = cfwd
		self.cupdown = cupdown
		self.compx = self.compx + self.cfwd
		self.compy = self.compy + self.cupdown
		self.compmov = self.compmov + 1
        
class Game:
	def __init__(self):
		# Draw window
		self.window = GraphWin("Frisbee Golf", 1000, 500)
		self.window.setCoords(0, 0, 500, 250)
		self.hole = Hole(475,125,30,30)
		self.grasscolor = color_rgb(0,150,0)
		self.mountaincolor = color_rgb(192, 192, 150)
		self.bunkercolor = color_rgb(243, 181, 0)
		self.lakecolor = color_rgb(101, 153, 255)
		self.pink = color_rgb(255, 105, 180)
		self.window.setBackground(self.grasscolor)
		
		# Draw main menu buttons
		self.easy = MapButton(Point(250,185), 100, 50, "Easy")
		self.easy.draw(self.window)
		self.medium = MapButton(Point(250,125), 100, 50, "Medium")
		self.medium.draw(self.window)
		self.hard = MapButton(Point(250,65), 100, 50, "Hard")
		self.hard.draw(self.window)
		
		# Assign function to main menu buttons
		p = self.window.getMouse()
		if self.easy.clicked(p):
			self.easy.clrclick()
			self.easy.undraw(self.window)
			self.medium.undraw(self.window)
			self.hard.undraw(self.window)
			self.getEasy()
			self.getButtons()
			self.play()
			
		if self.medium.clicked(p):
			self.medium.clrclick()
			self.easy.undraw(self.window)
			self.medium.undraw(self.window)
			self.hard.undraw(self.window)
			self.getMedium()
			self.getButtons()
			self.play()
		
		if self.hard.clicked(p):
			self.hard.clrclick()
			self.easy.undraw(self.window)
			self.medium.undraw(self.window)
			self.hard.undraw(self.window)
			self.getHard()
			self.getButtons()
			self.play()

	# Creates easy golf course
	def getEasy(self):
		# Set obstacles and goal
		self.ob1 = Obstacle(Point(100,40),60,40, self.mountaincolor)
		self.ob2 = Obstacle(Point(200,190),110,200, self.mountaincolor)
		self.bunker1 = Obstacle(Point(370,50),150,200, self.bunkercolor)

		# Draw obstacles and hole
		self.ob1.draw(self.window)
		self.ob2.draw(self.window)
		self.bunker1.draw(self.window)
		self.hole.draw(self.window)
		
		# Draw par textbox
		self.par = EndNote(Point(480, 240), 30, 10, "Par 7", self.pink)
		self.par.draw(self.window)

		# Draw frisbees
		self.rules = Rules(10, 140, 10, 110)
		self.frisbee = self.makeFrisbee()
		self.frisbee.draw(self.window)
		self.cplayer = self.makeCplayer()
		self.cplayer.draw(self.window)
		
		self.rules.par = 7
		
	# Creates medium golf course
	def getMedium(self):
		# Set obstacles and goal
		self.ob1 = Obstacle(Point(185,280),150,240, self.lakecolor)
		self.ob2 = Obstacle(Point(355,115),160,200, self.mountaincolor)
		self.bunker1 = Obstacle(Point(175,40),130,200, self.bunkercolor)

		# Draw obstacles and hole
		self.ob1.draw(self.window)
		self.ob2.draw(self.window)
		self.bunker1.draw(self.window)
		self.hole.draw(self.window)
		
		# Draw par textbox
		self.par = EndNote(Point(480, 240), 30, 10, "Par 8", self.pink)
		self.par.draw(self.window)

		# Draw frisbee
		self.rules = Rules(10, 140, 10, 110)
		self.frisbee = self.makeFrisbee()
		self.frisbee.draw(self.window)
		self.cplayer = self.makeCplayer()
		self.cplayer.draw(self.window)
		
		self.rules.par = 8
		
	# Creates hard golf course
	def getHard(self):
		# Set obstacles and goal
		self.ob1 = Obstacle(Point(220,130),80,300, self.lakecolor)
		self.ob2 = Obstacle(Point(330,170),116,280, self.lakecolor)
		self.bunker1 = Obstacle(Point(60,104),210,182, self.bunkercolor)

		# Draw obstacles and hole
		self.ob1.draw(self.window)
		self.ob2.draw(self.window)
		self.bunker1.draw(self.window)
		self.hole.draw(self.window)
		
		# Draw par textbox
		self.par = EndNote(Point(480, 240), 30, 10, "Par 8", self.pink)
		self.par.draw(self.window)

		# Draw frisbee
		self.rules = Rules(10, 170, 10, 150)
		self.frisbee = self.makeFrisbee()
		self.frisbee.draw(self.window)
		self.cplayer = self.makeCplayer()
		self.cplayer.draw(self.window)
		
		self.rules.par = 8

	def getButtons(self):	
		
		# Draw arrow key buttons
		self.nbutton = DirectionButton(Point(10,80), 15, 10, "N")
		self.nbutton.draw(self.window)
		self.nebutton = DirectionButton(Point(22,65), 15, 10, "N / E")
		self.nebutton.draw(self.window)
		self.ebutton = DirectionButton(Point(34,50), 15, 10, "E")
		self.ebutton.draw(self.window)
		self.sebutton = DirectionButton(Point(22,35), 15, 10, "S / E")
		self.sebutton.draw(self.window)
		self.sbutton = DirectionButton(Point(10,20), 15, 10, "S")
		self.sbutton.draw(self.window)

		# Draw power buttons
		self.power3 = PowerButton(Point(25, 240), 40, 10, "Driver", 6)
		self.power3.draw(self.window)
		self.power2 = PowerButton(Point(70, 240), 40, 10, "Mid-Range", 3)
		self.power2.draw(self.window)
		self.power1 = PowerButton(Point(115, 240), 40, 10, "Putter", 1)
		self.power1.draw(self.window)
		
		# Make new game button
		self.newgame = DirectionButton(Point(445, 235), 30, 20, "Reset")
		self.newgame.draw(self.window)
		
		# Draw quit button
		self.quitbutton = DirectionButton(Point(410, 235), 30, 20, "Quit")
		self.quitbutton.draw(self.window)
	
	def makeFrisbee(self):			
		friz = Circle(Point(self.rules.xval, self.rules.yval), 6)
		friz.setFill("white")
		return friz
	
	def makeCplayer(self):
		friz = Circle(Point(self.rules.compx, self.rules.compy), 6)
		friz.setFill("black")
		friz.setOutline("white")
		return friz
		
	# Checks if user frisbee has hit an obstacle or goes out of bounds
	def crashCheck(self):
		# Checks if frisbee hits an obstacle
		crashl1 = self.ob1.stuck()
		if crashl1[0] <= self.rules.xval <= crashl1[1] and crashl1[2] <= self.rules.yval <= crashl1[3]:
			self.rules.crash = 1
		crashl2 = self.ob2.stuck()
		if crashl2[0] <= self.rules.xval <= crashl2[1] and crashl2[2] <= self.rules.yval <= crashl2[3]:
			self.rules.crash = 1
			
		# Checks if frisbee is in a bunker	
		bunkl = self.bunker1.stuck()
		if bunkl[0] <= self.rules.xval <= bunkl[1] and bunkl[2] <= self.rules.yval <= bunkl[3]:
			self.rules.bunked1 = 17
			self.rules.bunked2 = 9
			self.rules.bunked3 = 11
		if self.rules.xval > bunkl[1] or self.rules.yval > bunkl[3] or self.rules.yval < bunkl[2]:
			self.rules.bunked1 = 0
			self.rules.bunked2 = 0
			self.rules.bunked3 = 0
		
		# Checks if frisbee has gone out of bounds
		if 500 < self.rules.xval or 250 < self.rules.yval:
			self.rules.offmap = 1
		if self.rules.yval < 0:
			self.rules.offmap = 1
	
	# Checks if user frisbee is in the goal
	def winCheck(self):
		winl = self.hole.ingoal()
		if winl[0] <= self.rules.xval <= winl[1] and winl[2] <= self.rules.yval <= winl[3]:
			self.rules.scored = 1
			
	# Gets rid of direction buttons at end of game
	def deactivate(self):
		self.nbutton.undraw(self.window)
		self.nebutton.undraw(self.window)
		self.ebutton.undraw(self.window)
		self.sebutton.undraw(self.window)
		self.sbutton.undraw(self.window)
   
	def play(self):
		multi = self.power3.getPower()
		self.power3.setFill(self.pink)
		while self.rules.getMovnum() <= 25:
		
			# Draw display that keeps track of your moves
			self.scorekeeper = EndNote(Point(480, 230), 30, 10, ("Moves: " + `self.rules.getMovnum()`), self.pink)
			self.scorekeeper.draw(self.window)
			
			self.crashCheck()
			p = self.window.getMouse()
		
			# User input for power buttons
			if self.power1.clicked(p):
				multi = self.power1.getPower()
				self.power2.setFill("white")
				self.power3.setFill("white")
				self.power1.setFill(self.pink)
			if self.power2.clicked(p):
				multi = self.power2.getPower()
				self.power3.setFill("white")
				self.power1.setFill("white")
				self.power2.setFill(self.pink)
			if self.power3.clicked(p):
				multi = self.power3.getPower()
				self.power1.setFill("white")
				self.power2.setFill("white")
				self.power3.setFill(self.pink)
		
			# User input for direction buttons
			if self.nbutton.clicked(p):
				tot1 = (15 - self.rules.bunked3) * multi   # Moves frisbee based on
				self.nbutton.clrclick()                    # power button input and
				self.frisbee.move(0, tot1)                 # if frisbee is in a bunker
				self.rules.update(0, tot1)
				self.crashCheck()
				self.winCheck()
				self.compPlay()
			if self.nebutton.clicked(p):
				tot2 = (12 - self.rules.bunked2) * multi
				self.nebutton.clrclick()
				self.frisbee.move(tot2, tot2)
				self.rules.update(tot2, tot2)
				self.crashCheck()
				self.winCheck()
				self.compPlay()
			if self.ebutton.clicked(p):
				tot3 = (20 - self.rules.bunked1) * multi
				self.ebutton.clrclick()
				self.frisbee.move(tot3, 0)
				self.rules.update(tot3, 0)
				self.crashCheck()
				self.winCheck()
				self.compPlay()
			if self.sebutton.clicked(p):
				tot4 = (12 - self.rules.bunked2) * multi
				self.sebutton.clrclick()
				self.frisbee.move(tot4, -tot4)
				self.rules.update(tot4, -tot4)
				self.crashCheck()
				self.winCheck()
				self.compPlay()
			if self.sbutton.clicked(p):
				tot5 = (15 - self.rules.bunked3) * multi
				self.sbutton.clrclick()
				self.frisbee.move(0, -tot5)
				self.rules.update(0, -tot5)
				self.crashCheck()
				self.winCheck()
				self.compPlay()
			
			# Resets game
			if self.newgame.clicked(p):
				self.newgame.clrclick()
				self.window.close()
				self.rules.movnum = 0
				game = Game()
			
			# Quits game
			if self.quitbutton.clicked(p):
				self.quitbutton.clrclick()
				self.rules.movnum = 100
			
			# Draws display if computer wins
			if self.rules.cscored == 1:
				self.deactivate()
				self.hole.changeclr()
				if self.rules.compmov <= self.rules.par:
					self.winner = EndNote(Point(250, 125), 200, 100,("Beau wins. His score is " + `self.rules.getMovnum()`), "grey")
					self.winner.draw(self.window)
				else:
					self.loser = EndNote(Point(250, 125), 200, 100,("Beau was not under par. His score is " + `self.rules.getMovnum()`), "grey")
					self.loser.draw(self.window)
			
			# Draws display if user wins
			if self.rules.scored == 1:
				self.deactivate()
				self.hole.changeclr()
				if self.rules.movnum <= self.rules.par:
					self.winner = EndNote(Point(250, 125), 200, 100,("YOU WIN! Your score is " + `self.rules.getMovnum()`), self.pink)
					self.winner.draw(self.window)
				else:
					self.loser = EndNote(Point(250, 125), 200, 100,("You were not under par. Your score is " + `self.rules.getMovnum()`), "grey")
					self.loser.draw(self.window)
				
			# Draws display if user hits an obstacle
			if self.rules.crash == 1:
				self.deactivate()
				self.crashnote = EndNote(Point(250, 125), 200, 100, "You lost your frisbee. Please quit or reset", "grey")
				self.crashnote.draw(self.window)
				self.hole.undraw(self.window)
				
			# Draws display if user throws out of bounds
			if self.rules.offmap == 1:
				self.deactivate()
				self.offnote = EndNote(Point(250, 125), 200, 100, "You are off the map. Please quit or reset", "grey")
				self.offnote.draw(self.window)
				self.hole.undraw(self.window)
			
			# Draws display if computer player throws out of bounds
			if self.rules.coffmap == 1:
				self.offnote = EndNote(Point(180, 240), 80, 10, "Beau threw out of bounds", "white")
				self.offnote.draw(self.window)
				self.cplayer.undraw()
			
			# Draws display if computer player hits an obstacle
			if self.rules.ccrash == 1:
				self.offnote = EndNote(Point(180, 240), 80, 10, "Beau lost his frisbee", "white")
				self.offnote.draw(self.window)
		
		# Losing tests
		if self.rules.getMovnum > 25:
			self.xval = 1000
			self.yval = 1000
			print "Game Quit"
		
	# Method that computer uses to navigate around obstacles
	def compPlay(self):
		ob1chk = self.ob1.stuck()
		ob2chk = self.ob2.stuck()
		bunkerchk = self.bunker1.stuck()
		winchk = self.hole.ingoal()
		self.compCheck()
		if 0 <= self.rules.compx <= 500 and 0 <= self.rules.compy <= 250:
			if self.rules.ccrash == 0:
				if ob1chk[2] < ob2chk[2]:
					lowest = ob1chk[2]
				else:
					lowest = ob2chk[2]
				if ob1chk[2] < 0 and ob1chk[3] > 250:
					lowest = ob2chk[2]
				if self.rules.compmov < self.rules.movnum:
					if ob1chk[0] > self.rules.compx:
						if self.rules.compy > lowest:
							self.compChoose(2)
							self.compCheck()
				if self.rules.compmov < self.rules.movnum:
					if ob2chk[1] > self.rules.compx:
						self.compChoose(3)
						self.compCheck()
				if self.rules.compmov < self.rules.movnum:
					if winchk[0] > self.rules.compx:
						shotx = (((winchk[0] + winchk[1]) / 2) - self.rules.compx)
						self.cplayer.move(shotx, 0)
						self.rules.cupdate(shotx,0)
						self.compCheck()
				if self.rules.compmov < self.rules.movnum:
					if ob2chk[1] < self.rules.compx:
						if winchk[3] > self.rules.compy:
							shoty = (((winchk[2] + winchk[3]) / 2) - self.rules.compy)
							self.rules.oneshotx = 1
							self.cplayer.move(0, shoty)
							self.rules.cupdate(0, shoty)
							self.compCheck()
		
	# Moves computer player
	def compChoose(self, m):
		recoil = [1, 1, 1, 2]
		r = randrange(0, 4)
		if m == 1:
			self.cplayer.move(0, (25 * recoil[r]) - self.rules.cbunked1)
			self.rules.cupdate(0, (25 * recoil[r]) - self.rules.cbunked1)
		if m == 2:
			self.cplayer.move(0, (-25 * recoil[r]) - self.rules.cbunked1)
			self.rules.cupdate(0, (-25 * recoil[r]) - self.rules.cbunked1)
		if m == 3:
			self.cplayer.move(((120 * recoil[r]) - self.rules.cbunked2), 0)
			self.rules.cupdate(((120 * recoil[r]) - self.rules.cbunked2), 0)
	
	# Checks computer player status
	def compCheck(self):
	
		# Checks if computer player is in bounds
		if 500 < self.rules.compx or 250 < self.rules.compy:
			self.rules.coffmap = 1
		if self.rules.compy < 0:
			self.rules.coffmap = 1
		
		# Checks if computer player has hit an obstacle
		crashl1 = self.ob1.stuck()
		if crashl1[0] <= self.rules.compx <= crashl1[1] and crashl1[2] <= self.rules.compy <= crashl1[3]:
			self.rules.ccrash = 1
			
		# Checks if computer player in stuck in a bunker
		bunkl = self.bunker1.stuck()
		if bunkl[0] <= self.rules.compx <= bunkl[1] and bunkl[2] <= self.rules.compy <= bunkl[3]:
			self.rules.cbunked1 = 10
			self.rules.cbunked2 = 90
		if self.rules.compx > bunkl[1] or self.rules.compy > bunkl[3] or self.rules.compy < bunkl[2]:
			self.rules.cbunked1 = 0
			self.rules.cbunked2 = 0
		
		# Checks if computer player has won
		winl = self.hole.ingoal()
		if winl[0] <= self.rules.compx <= winl[1] and winl[2] <= self.rules.compy <= winl[3]:
			self.rules.cscored = 1

def main():
	game = Game()

if __name__ == "__main__":
	main()
