from random import randint
from Tkinter import *
import tkMessageBox

#
# WCKLIB
# $Id$
#
# tooltips for arbitrary Tkinter widgets
#
# written by Fredrik Lundh, June 1997.  changed to use a global controller
# in September 2007.
#
# Copyright (c) 1997-2007 by Fredrik Lundh.  All rights reserved.
#
# See the README file for license details.
#

from Tkinter import *

class ToolTipManager:

    label = None
    window = None
    active = 0

    def __init__(self):
        self.tag = None

    def getcontroller(self, widget):
        if self.tag is None:

            self.tag = "ui_tooltip_%d" % id(self)
            widget.bind_class(self.tag, "<Enter>", self.enter)
            widget.bind_class(self.tag, "<Leave>", self.leave)

            # pick suitable colors for tooltips
            try:
                self.bg = "systeminfobackground"
                self.fg = "systeminfotext"
                widget.winfo_rgb(self.fg) # make sure system colors exist
                widget.winfo_rgb(self.bg)
            except:
                self.bg = "#ffffe0"
                self.fg = "black"

        return self.tag

    def register(self, widget, text):
        widget.ui_tooltip_text = text
        tags = list(widget.bindtags())
        tags.append(self.getcontroller(widget))
        widget.bindtags(tuple(tags))

    def unregister(self, widget):
        tags = list(widget.bindtags())
        tags.remove(self.getcontroller(widget))
        widget.bindtags(tuple(tags))

    # event handlers

    def enter(self, event):
        widget = event.widget
        if not self.label:
            # create and hide balloon help window
            self.popup = Toplevel(bg=self.fg, bd=1)
            self.popup.overrideredirect(1)
            self.popup.withdraw()
            self.label = Label(
                self.popup, fg=self.fg, bg=self.bg, bd=0, padx=2
                )
            self.label.pack()
            self.active = 0
        self.xy = event.x_root + 16, event.y_root + 10
        self.event_xy = event.x, event.y
        self.after_id = widget.after(200, self.display, widget)

    def display(self, widget):
        if not self.active:
            # display balloon help window
            text = widget.ui_tooltip_text
            if callable(text):
                text = text(widget, self.event_xy)
            self.label.config(text=text)
            self.popup.deiconify()
            self.popup.lift()
            self.popup.geometry("+%d+%d" % self.xy)
            self.active = 1
            self.after_id = None

    def leave(self, event):
        widget = event.widget
        if self.active:
            self.popup.withdraw()
            self.active = 0
        if self.after_id:
            widget.after_cancel(self.after_id)
            self.after_id = None

_manager = ToolTipManager()

##
# Registers a tooltip for a given widget.
#
# @param widget The widget object.
# @param text The tooltip text.  This can be either a string, or a callable
#     object. If callable, it is called as text(widget) when the tooltip is
#     about to be displayed, and the returned text is displayed instead.

def register(widget, text):
    _manager.register(widget, text)

##
# Unregisters a tooltip.  Note that the tooltip information is automatically
# destroyed when the widget is destroyed.

def unregister(widget):
    _manager.unregister(widget)
"""
if __name__ == "__main__":

    root = Tk()

    root.title("ToolTips")

    b1 = Button(root, bg="red", text="red")
    b1.pack()

    register(b1, "A red button")

    b2 = Button(root, bg="green", text="green")
    b2.pack()

    register(b2, "A green button")

    b3 = Button(root, fg="blue", text="blue")
    b3.pack()

    def cb(*args):
        return "A blue text"

    register(b3, cb)
    # unregister(b3)

    mainloop()
"""

"""
global radiant_strike_clicked
global dire_strike_clicked
global radiant_greed_clicked
global dire_greed_clicked
global radiant_freeze_clicked
global dire_freeze_clicked
global radiant_burn_clicked
global dire_burn_clicked
global radiant_basillius_clicked
global dire_basillius_clicked
"""
radiant_turns=0
dire_turns=0

class Hero(object):
	def __init__(self):
		self.hp=10
		self.mana=10
		self.gold=0
		self.hpregen=1
		self.manaregen=1 
		self.goldregen=1 
		self.strike=Strike()
		self.greed=Greed()
		self.freeze=Freeze()
		self.burn=Burn()
		self.basillius=Basillius()
		
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
		self.manacost=self.manacost+1
		

class Greed(object):
	def __init__(self):
		self.goldgrab=2
		self.hpcost=2
		self.level=1
		
	def levelup(self):
		self.level=self.level+1
		self.goldgrab=self.goldgrab+2
		
	
class Freeze(object):
	def __init__(self):
		self.damage=3
		self.manacost=7
		self.turns=1
		self.level=1
		
	def levelup(self):
		self.level +=1
		self.manacost+=1
		self.turns+=1

class Burn(object):
	def __init__(self):
		self.level=1
		self.damage=1
		self.manaburn=10
		self.manacost=8
	
	def levelup(self):
		self.level+=1
		self.damage+=1
		self.manaburn+=5
		self.manacost+=1
		
class Basillius(object):
	def __init__(self):
		self.level = 0
		self.manaregen = 0
		self.cost = 5	
		
	def levelup(self):
		self.level += 1
		self.manaregen+=2
		self.cost+=5
		

		
root = Tk()

radiant=Hero()
dire=Hero()

#widgets:

		

radiant_label=Label(root,text="Radiant")
dire_label=Label(root,text="Dire")

radiant_hp_label=Label(root,text="HP:")
radiant_mana_label=Label(root,text="Mana:")
radiant_gold_label=Label(root,text="Gold:")

dire_hp_label=Label(root,text="HP:")
dire_mana_label=Label(root,text="Mana:")
dire_gold_label=Label(root,text="Gold:")

radiant_ability_label=Label(root,text="Abilities")
dire_ability_label=Label(root,text="Abilities")

radiant_strike_label=Label(root,text="Strike")
dire_strike_label=Label(root,text="Strike")

radiant_hp_value_label_text=IntVar()
radiant_hp_value_label_text.set(radiant.hp)
radiant_hp_value_label=Label(root,textvariable=radiant_hp_value_label_text)

radiant_mana_value_label_text=IntVar()
radiant_mana_value_label_text.set(radiant.mana)
radiant_mana_value_label=Label(root,textvariable=radiant_mana_value_label_text)

radiant_gold_value_label_text=IntVar()
radiant_gold_value_label_text.set(radiant.gold)
radiant_gold_value_label=Label(root,textvariable=radiant_gold_value_label_text)

dire_hp_value_label_text=IntVar()
dire_hp_value_label_text.set(dire.hp)
dire_hp_value_label=Label(root,textvariable=dire_hp_value_label_text)

dire_mana_value_label_text=IntVar()
dire_mana_value_label_text.set(dire.mana)
dire_mana_value_label=Label(root,textvariable=dire_mana_value_label_text)

dire_gold_value_label_text=IntVar()
dire_gold_value_label_text.set(dire.gold)
dire_gold_value_label=Label(root,textvariable=dire_gold_value_label_text)

start_button=Button(root,text="Enter Battle",command=lambda:turn(0))
register(start_button,"Start the battle")

radiant_strike_button=Button(root,text="Strike",state="disabled",command=lambda:radiant_strike())
register(radiant_strike_button,"Deals 2 Base Damage + 1 Damage Every 5 Levels.\n Mana Cost = Level of Strike. Every Use Increases Its Level")
dire_strike_button=Button(root,text="Strike",state="disabled",command=lambda:dire_strike())
register(dire_strike_button,"Deals 2 Base Damage + 1 Damage Every 5 Levels.\n Mana Cost = Level of Strike. Every Use Increases Its Level")

radiant_item_label = Label(root,text="Items")
dire_item_label = Label(root,text="Items")

radiant_basillius_button = Button(root,text="Ring of Basillius",state="disabled",command=lambda:radiant_buy_basillius())
register(radiant_basillius_button,"+2 Mana Regen Every Level.\n Cost Increases By 5 For Each Level")
dire_basillius_button = Button(root,text="Ring of Basillius",state="disabled",command=lambda:dire_buy_basillius())
register(dire_basillius_button,"+2 Mana Regen Every Level.\n Cost Increases By 5 For Each Level")

radiant_basillius_level_label_text=IntVar()
radiant_basillius_level_label_text.set(radiant.basillius.level)
radiant_basillius_level_label=Label(root,textvariable=radiant_basillius_level_label_text)

dire_basillius_level_label_text=IntVar()
dire_basillius_level_label_text.set(dire.basillius.level)
dire_basillius_level_label=Label(root,textvariable=dire_basillius_level_label_text)

radiant_strike_level_label_text=IntVar()
radiant_strike_level_label_text.set(radiant.strike.level)
radiant_strike_level_label=Label(root,textvariable=radiant_strike_level_label_text)

dire_strike_level_label_text=IntVar()
dire_strike_level_label_text.set(dire.strike.level)
dire_strike_level_label=Label(root,textvariable=dire_strike_level_label_text)

radiant_greed_button=Button(root,text="Greed",state="disabled",command=lambda:radiant_greed())
register(radiant_greed_button,"Steal LevelX2 Gold At The Cost of 2 HP")
dire_greed_button=Button(root,text="Greed",state="disabled",command=lambda:dire_greed())
register(dire_greed_button,"Steal LevelX2 Gold At The Cost of 2 HP")

radiant_greed_level_label_text=IntVar()
radiant_greed_level_label_text.set(radiant.greed.level)
radiant_greed_level_label=Label(root,textvariable=radiant_greed_level_label_text)

dire_greed_level_label_text=IntVar()
dire_greed_level_label_text.set(dire.greed.level)
dire_greed_level_label=Label(root,textvariable=dire_greed_level_label_text)

radiant_freeze_button=Button(root,text="Freeze",state="disabled",command=lambda:radiant_freeze())
register(radiant_freeze_button,"3 Damage Every Time It Is Used. Grants Additional Turns Equal To The Level Of Freeze.\n Base Mana Cost=7. Mana Cost Increases By 1 Every Level")
dire_freeze_button=Button(root,text="Freeze",state="disabled",command=lambda:dire_freeze())
register(dire_freeze_button,"3 Damage Every Time It Is Used. Grants Additional Turns Equal To The Level Of Freeze. Base Mana Cost=7. Mana Cost Increases By 1 Every Level")

radiant_freeze_level_label_text=IntVar()
radiant_freeze_level_label_text.set(radiant.freeze.level)
radiant_freeze_level_label = Label(root,textvariable=radiant_freeze_level_label_text)

dire_freeze_level_label_text=IntVar()
dire_freeze_level_label_text.set(dire.freeze.level)
dire_freeze_level_label = Label(root, textvariable=dire_freeze_level_label_text)

radiant_burn_button = Button(root,text="Burn",state="disabled",command=lambda:radiant_burn())
register(radiant_burn_button,"Deals 1 Base Damage and Level X 5 Mana Burn. Base Mana Cost is 10. Levels up Every Time it is Used.\n +1 Damage and +5 Mana Burn Every Level. Mana Cost Increases by 1 Every Level" )
dire_burn_button = Button(root,text="Burn",state="disabled",command=lambda:dire_burn())
register(dire_burn_button,"Deals 1 Base Damage and Level X 5 Mana Burn. Base Mana Cost is 10. Levels up Every Time it is Used.\n +1 Damage and +5 Mana Burn Every Level. Mana Cost Increases by 1 Every Level" )

radiant_burn_level_label_text=IntVar()
radiant_burn_level_label_text.set(radiant.burn.level)
radiant_burn_level_label=Label(root,textvariable=radiant_burn_level_label_text)

dire_burn_level_label_text=IntVar()
dire_burn_level_label_text.set(dire.burn.level)
dire_burn_level_label=Label(root,textvariable=dire_burn_level_label_text)

#button functions:

def turn(arg):
	start_button.configure(state="disabled")
	if radiant.hp <= 0:
		tkMessageBox.showinfo("Dire Victory", "Dire Victory")
		
	if dire.hp <= 0:
		tkMessageBox.showinfo("Radiant Victory", "Radiant Victory")
	radiant_strike_clicked=0
	if arg == 0:	
		t = randint(0,99)
	if arg == 1:
		t = 2
	if arg == 2:
		t =1
	if t%2==0: #radiant's turn
		dire_strike_button.configure(state="disabled")
		dire_greed_button.configure(state="disabled")
		dire_freeze_button.configure(state="disabled")
		dire_burn_button.configure(state="disabled")
		dire_basillius_button.configure(state="disabled")
		radiant_strike_button.configure(state="normal")
		radiant_greed_button.configure(state="normal")
		radiant_freeze_button.configure(state="normal")
		radiant_burn_button.configure(state="normal")
		radiant_basillius_button.configure(state="normal")
		radiant.hp += radiant.hpregen
		radiant.mana += radiant.manaregen
	if t%2==1: #dire's turn
		radiant_strike_button.configure(state="disabled")
		radiant_greed_button.configure(state="disabled")
		radiant_freeze_button.configure(state="disabled")
		radiant_burn_button.configure(state="disabled")
		radiant_basillius_button.configure(state="disabled")
		dire_strike_button.configure(state="normal")
		dire_greed_button.configure(state="normal")
		dire_freeze_button.configure(state="normal")
		dire_burn_button.configure(state="normal")
		dire_basillius_button.configure(state="normal")
		dire.hp += dire.hpregen
		dire.mana += dire.manaregen
	if radiant.strike.manacost > radiant.mana: #strike
		radiant_strike_button.configure(state="disabled")
	if dire.strike.manacost > dire.mana:
		dire_strike_button.configure(state="disabled")
	#if radiant.hp <= 2: #greed. Not neccessary anymore. Can commit suicide
	#	radiant_greed_button.configure(state="disabled")
	#if dire.hp <= 2:
	#	dire_greed_button.configure(state="disabled")
	if radiant.mana < radiant.freeze.manacost: #freeze
		radiant_freeze_button.configure(state="disabled")
	if dire.mana < dire.freeze.manacost:
		dire_freeze_button.configure(state="disabled")
	if radiant.mana < radiant.burn.manacost:#burn
		radiant_burn_button.configure(state="disabled")
	if dire.mana < dire.burn.manacost:
		dire_burn_button.configure(state="disabled")
	if radiant.gold + 1 < radiant.basillius.cost: #Ring of Basillius, + 1 because we're only updating the value later
		radiant_basillius_button.configure(state="disabled")
	if dire.gold + 1 < dire.basillius.cost:
		dire_basillius_button.configure(state="disabled")
	radiant.gold += radiant.goldregen
	dire.gold += dire.goldregen
	radiant_hp_value_label_text.set(radiant.hp)
	radiant_mana_value_label_text.set(radiant.mana)
	radiant_gold_value_label_text.set(radiant.gold)
	dire_hp_value_label_text.set(dire.hp)
	dire_mana_value_label_text.set(dire.mana)
	dire_gold_value_label_text.set(dire.gold)
	
	
def radiant_strike():
	#radiant_strike_clicked=1
	radiant.mana -= radiant.strike.manacost
	dire.hp -= radiant.strike.damage
	radiant.strike.levelup()
	radiant_strike_level_label_text.set(radiant.strike.level)
	global radiant_turns
	if radiant_turns > 0:
		radiant_turns -= 1
		turn(1)
	else:
		turn(0)
	
def dire_strike():
	#dire_strike_clicked=1
	dire.mana -= dire.strike.manacost
	radiant.hp -= dire.strike.damage
	dire.strike.levelup()
	dire_strike_level_label_text.set(dire.strike.level)
	global dire_turns
	if dire_turns > 0:
		dire_turns -= 1
		turn(2)
	else:
		turn(0)
	
def radiant_buy_basillius():
	#radiant_buy_basillius_clicked=1
	radiant.gold -= radiant.basillius.cost
	radiant.manaregen -= radiant.basillius.manaregen
	radiant.basillius.levelup()
	radiant.manaregen += radiant.basillius.manaregen
	radiant_basillius_level_label_text.set(radiant.basillius.level)
	global radiant_turns
	if radiant_turns > 0:
		radiant_turns -= 1
		turn(1)
	else:
		turn(0)
			
def dire_buy_basillius():
	#dire_buy_basillius_clicked=1
	dire.gold -= dire.basillius.cost
	dire.manaregen -= dire.basillius.manaregen
	dire.basillius.levelup()
	dire.manaregen += dire.basillius.manaregen
	dire_basillius_level_label_text.set(dire.basillius.level)
	#dire_gold_value_label_text.set(dire.gold)
	global dire_turns
	if dire_turns > 0:
		dire_turns -= 1
		turn(2)
	else:
		turn(0)
		
def radiant_greed():
	#radiant_greed_clicked=1
	radiant.hp -= 2
	radiant.gold +=radiant.greed.goldgrab
	dire.gold -= radiant.greed.goldgrab
	radiant.greed.levelup()
	radiant_greed_level_label_text.set(radiant.greed.level)
	#radiant_hp_value_label_text.set(radiant.hp)
	#dire_gold_value_label_text.set(dire.gold)
	global radiant_turns
	if radiant_turns > 0:
		radiant_turns -= 1
		turn(1)
	else:
		turn(0)
	
def dire_greed():
	#dire_greed_clicked=1
	dire.hp -= 2
	dire.gold += dire.greed.goldgrab
	radiant.gold -= dire.greed.goldgrab
	dire.greed.levelup()
	dire_greed_level_label_text.set(dire.greed.level)
	#dire_hp_value_label_text.set(dire.hp)
	#radiant_gold_value_label_text.set(radiant.gold)
	global dire_turns
	if dire_turns > 0:
		dire_turns -= 1
		turn(2)
	else:
		turn(0)
	

def radiant_freeze():
	#radiant_freeze_clicked=1
	global radiant_turns
	radiant_turns = radiant.freeze.turns
	radiant.mana -= radiant.freeze.manacost
	dire.hp -= radiant.freeze.damage
	radiant.freeze.levelup()
	radiant_freeze_level_label_text.set(radiant.freeze.level)
	turn(1)
	
def dire_freeze():
	#dire_freeze_clicked=1
	global dire_turns
	dire_turns = dire.freeze.turns
	dire.mana -= dire.freeze.manacost
	radiant.hp -= dire.freeze.damage
	dire.freeze.levelup()
	dire_freeze_level_label_text.set(dire.freeze.level)
	turn(2)
	
def radiant_burn():
	#radiant_burn_clicked=1
	radiant.mana -= radiant.burn.manacost
	dire.hp -= radiant.burn.damage
	dire.mana -= radiant.burn.manaburn
	radiant.burn.levelup()
	radiant_burn_level_label_text.set(radiant.burn.level)
	global radiant_turns
	if radiant_turns > 0:
		radiant_turns -= 1
		turn(1)
	else:
		turn(0)
	
def dire_burn():
	dire.mana -= dire.burn.manacost
	radiant.hp -= dire.burn.damage
	radiant.mana -= dire.burn.manaburn
	dire.burn.levelup()
	dire_burn_level_label_text.set(dire.burn.level)
	global dire_turns
	if dire_turns > 0:
		dire_turns -= 1
		turn(2)
	else:
		turn(0)
	
#layout:

radiant_label.grid(row=1,column=1)
radiant_hp_label.grid(row=2,column=1)
radiant_mana_label.grid(row=3,column=1)
radiant_gold_label.grid(row=4,column=1)
radiant_hp_value_label.grid(row=2,column=2)
radiant_mana_value_label.grid(row=3,column=2)
radiant_gold_value_label.grid(row=4,column=2)
radiant_ability_label.grid(row=5,column=1)
	
radiant_strike_button.grid(row=6,column=1)
radiant_strike_level_label.grid(row=7,column=1)

radiant_greed_button.grid(row=6,column=2)
radiant_greed_level_label.grid(row=7,column=2)

radiant_freeze_button.grid(row=8,column=1)
radiant_freeze_level_label.grid(row=9,column=1)

radiant_burn_button.grid(row=8,column=2)
radiant_burn_level_label.grid(row=9,column=2)

	
radiant_item_label.grid(row=10,column=1)
radiant_basillius_button.grid(row=11,column=1)
radiant_basillius_level_label.grid(row=12,column=1)	

start_button.grid(row=1,column=3)

dire_label.grid(row=1,column=4)
dire_hp_label.grid(row=2,column=4)
dire_mana_label.grid(row=3,column=4)
dire_gold_label.grid(row=4,column=4)
dire_hp_value_label.grid(row=2,column=5)
dire_mana_value_label.grid(row=3,column=5)
dire_gold_value_label.grid(row=4,column=5)
dire_ability_label.grid(row=5,column=4)

dire_strike_button.grid(row=6,column=4)
dire_strike_level_label.grid(row=7,column=4)

dire_greed_button.grid(row=6,column=5)
dire_greed_level_label.grid(row=7,column=5)	

dire_freeze_button.grid(row=8,column=4)
dire_freeze_level_label.grid(row=9,column=4)

dire_burn_button.grid(row=8,column=5)
dire_burn_level_label.grid(row=9,column=5)

dire_item_label.grid(row=10,column=4)
dire_basillius_button.grid(row=11,column=4)
dire_basillius_level_label.grid(row=12,column=4)

root.mainloop()





