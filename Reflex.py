from pygame import display , image , time , event , font
import time as TM
import random

class Main:
	def __init__(self):
		self.StartGame()
		self.GameLoop()

	def StartGame(self):
		display.init()
		font.init()
		
		self.GameState = "Not started"
		self.TimerStart = False

		self.ScreenSize = (600 , 600)
		self.Gray = (51,51,51)
		self.Lime = (94 , 227 , 10)
		self.Orange = (255,165,0)
		self.Red = (251,46,1)
		
		self.Clock = time.Clock()
		#self.Time = 0.0

		self.InfoFont = font.SysFont("consolas" , 24)
		self.BigTextFont = font.SysFont("calibri" , 56)
		self.screen = display.set_mode(self.ScreenSize)

	def GameLoop(self):
		while 1:
			for e in event.get():
				if e.type == 2:
					if e.key == 13 and self.GameState == "Not started":
						self.Time = 0.0
						self.GameState = "Wait timer"
						self.ToStart = TM.time() + random.randint(8 , 35) / 10
					if self.GameState == "Wait timer" and not self.TimerStart:
						self.ToStart += 0.2
					if self.GameState == "Wait press":
						self.GameState = "End"
					if self.GameState == "End" and e.key == 114:
						self.GameState = "Not started"
				if e.type == 12:
					display.quit()
					exit()	
			
			self.screen.fill(self.Gray)

			if self.GameState != "Not started":
				Time = self.InfoFont.render(str(self.Time) , 1 , self.Lime)
				if self.ToStart - TM.time() >= 0:
					Text = self.BigTextFont.render("Wait" , 1 , self.Orange)
					self.screen.blit(Text , (240 , 273))
				elif self.GameState == "End":
					Text = self.BigTextFont.render("You record: " + str(round(self.Time , 6)) , 1 , self.Orange)
					self.screen.blit(Text , (70 , 273))
				else:
					self.GameState = "Wait press"
					Text = self.BigTextFont.render("Press !!!" , 1 , self.Red)
					self.screen.blit(Text , (190 , 273))
					self.Time = TM.time() - self.ToStart
				self.screen.blit(Time , (0 , 574))
			else:
				Text = self.BigTextFont.render("Press enter to go" , 1 , self.Orange)
				self.screen.blit(Text , (100 , 273))
			self.Clock.tick(1000)
			display.update()

Main()