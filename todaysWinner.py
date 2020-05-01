#Mike Norrito 
""" Program: todaysWinner.py
a program that will pick a name from a list and display them as the winner of the day! 
"""
"""DELETE IF U PUT ON GITHUB!!! Afternoon Exercise 4/30/2020:
Create a GUI based python app that will display some text as a title like ("Today's winner is:"). And a command button. When the button is clicked, a random name from the students in our class should be chosen. That chosen name should then be displayed in the GUI.
BONUS: Don't allow the app to select the same student twice in a row OR don't allow a selected student to be EVER chosen again."""

#Import Statements 
from breezypythongui import EasyFrame

import random 


names = ["Spongebob Squarepants", "Patrick Star","Sandy Cheeks", "Eugene Krabs", "Squidward Tenticles", "Sheldon J. Plankton", "Karen Plankton's Computer Wife", "Gary the Snail", "Pearl Krabs", "Squilliam Fancyson", "Old Man Jenkins", "Mama Krabs", ]

class TodaysWinner(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self, title= "Honorary Town Rookie of the Day!", background = "hotpink", height = 300, width = 456)
		self.addLabel(text = "And Today Our Honorary Town Rookie of the day is...", row = 0, column = 1, columnspan = 2, background = "magenta", foreground = "white")
		self.outputArea = self.addTextArea(text = "", row = 1, column = 1, columnspan = 2)
		self.pickme = self.addButton(text = "Pick", row = 3, column = 0, columnspan = 2, command = self.pickme)
		self.prevWinner = ""


		self.outputArea["state"] = "disabled"

		#self.rookieSong = self.addLabel(text = "For he's a jolly good rookie, for he's a jolly good rookie, for he's a jolly good rookie...", row = 2, column = 2)
	def pickme(self):
		"""Picks a name and displays it as well"""
		
		#Little easter egg for only spongebob
		rookieMSong = "For he's a jolly good rookie,\nfor he's a jolly good rookie,\nfor he's a jolly good rookie..."
		#rookieWSong = "For she's a jolly good rookie,\nfor she's a jolly good rookie,\nfor she's a jolly good rookie..."


		result = random.choice(names)

		while result == self.prevWinner:
			print("We have a dupe: " + result)
			result = random.choice(names)



		if result == "Spongebob Squarepants":
			self.outputArea["state"] = "normal"
			self.outputArea.setText(result + "\n\n"+ rookieMSong)
			self.prevWinner = result
			self.outputArea["state"] = "disabled"
		elif result == "Gary the Snail":
			self.outputArea["state"] = "normal"
			self.outputArea.setText(result + "\n\nWait... this is a Snail. how did he get in the mix?")
			self.prevWinner = result
			self.outputArea["state"] = "disabled"

		else:
			self.outputArea["state"] = "normal"
			self.outputArea.setText(result)
			self.prevWinner = result
			self.outputArea["state"] = "disabled"


		





def main():
	TodaysWinner().mainloop()

main()




