from Tkinter import *
from random import randint


class Hero(object):
	def __init__(self):
		self.hp=10
		self.mana=10
		self.gold=0
		self.hpregen=1
		self.manaregen=1 
		self.goldregen=1 
		self.strike=Strike()
		
	def gainhp(self,hpgain):
		self.hp=self.hp + hpgain 
	
	def gainmana(self,managain):
		self.mana=self.mana + managain
	
	def gaingold(self,goldgain):
		self.gold=self.gold + goldgain
		
	def losehp(self,hploss):
		self.hp=self.hp - hploss
		
	def losemana(self,manaloss):
		self.mana=self.mana - manaloss 


class Strike(object):
	def __init__(self):
		self.damage=2
		self.manacost=1
		self.level=1 
		
	def levelup(self):
		self.level=self.level+1
		if self.level%5==0:
			self.damage=self.damage+1
		self.manacost=self.manacost+0.25
		

class gui:
	def __init__(self,master):
		self.master=master
		
		self.lich = Hero()
		self.huskar = Hero()
		
		
		self.lichlabel=Label(master,text="Lich")
		self.huskarlabel=Label(master,text="Huskar")
		
		self.lich_hp_label_text=IntVar()
		self.lich_hp_label_text.set(self.lich.hp)
		self.lich_hp_label=Label(master,textvariable=self.lich_hp_label_text)
		
		self.huskar_hp_label_text=IntVar()
		self.huskar_hp_label_text.set(self.huskar.hp)
		self.huskar_hp_label=Label(master,textvariable=self.huskar_hp_label_text)
		self.lichbutton=Button(master,text="Strike!",state="disabled",command=lambda:self.changehp("huskar"))
		self.huskarbutton=Button(master,text="Strike!",state="disabled",command=lambda:self.changehp("lich"))
		
		self.turnbutton=Button(master,text="Enter Battle",command=self.nextturn)
		
		self.turnbutton.grid(row=1,column=10)
		
		self.lichlabel.grid(row=1,column=1)
		self.huskarlabel.grid(row=1,column=15)
		
		self.lich_hp_label.grid(row=2,column=1)
		self.huskar_hp_label.grid(row=2,column=15)
		
		self.lichbutton.grid(row=3,column=1)
		self.huskarbutton.grid(row=3,column=15)
		
					
		
	def nextturn(self):
		self.turnbutton.config(state="disabled")
		turn = randint(0,99)
		if turn % 2 == 0:
			self.huskarbutton.config(state="disabled")
			self.lichbutton.config(state="normal")
		elif turn % 2 ==1:
			self.lichbutton.config(state="disabled")
			self.huskarbutton.config(state="normal")
	
	def changehp(self,method):
		if method=="lich":
			self.lich.losehp(2)
		elif method=="huskar":
			self.huskar.losehp(2)
		
		self.huskarbutton.config(state="disabled")
		self.lichbutton.config(state="disabled")
		self.lich_hp_label_text.set(self.lich.hp)
		self.huskar_hp_label_text.set(self.huskar.hp)
		self.nextturn()
		
root = Tk()
root.state('zoomed')
my_gui=gui(root)
root.mainloop()

		
		
		
		
		
