# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:26:14 2021

@author: workstation
"""

from logic2 import *
Rain = Atom('Rain') # Shortcut
Wet = Atom('Wet') # Shortcut
kb = createResolutionKB() # Create the knowledge base
kb.ask(Wet) # Prints "I don't know."
kb.ask(Not(Wet)) # Prints "I don't know."
kb.tell(Implies(Rain, Wet)) # Prints "I learned something."
kb.ask(Wet) # Prints "I don't know."
kb.tell(Rain) # Prints "I learned something."
kb.tell(Wet) # Prints "I already knew that."
kb.ask(Wet) # Prints "Yes."
kb.ask(Not(Wet)) # Prints "No."
kb.tell(Not(Wet)) # Prints "I don't buy that."