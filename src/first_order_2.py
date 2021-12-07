# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:04:25 2021

@author: workstation
"""

# Import libraries
import aima.utils
import aima.logic
# The main entry point for this module
def main():
    # Create an array to hold clauses
    clauses = []
    # Add first-order logic clauses (rules and fact)
    clauses.append(aima.utils.expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))
    clauses.append(aima.utils.expr("Enemy(Nono, America)"))
    clauses.append(aima.utils.expr("Owns(Nono, M1)"))
    clauses.append(aima.utils.expr("Missile(M1)"))
    clauses.append(aima.utils.expr("(Missile(x) & Owns(Nono, x)) ==> Sells(West, x, Nono)"))
    clauses.append(aima.utils.expr("American(West)"))
    clauses.append(aima.utils.expr("Missile(x) ==> Weapon(x)"))
    # Create a first-order logic knowledge base (KB) with clauses
    KB = aima.logic.FolKB(clauses)
    # Add rules and facts with tell
    KB.tell(aima.utils.expr('Enemy(Coco, America)'))
    KB.tell(aima.utils.expr('Enemy(Jojo, America)'))
    KB.tell(aima.utils.expr("Enemy(x, America) ==> Hostile(x)"))
    # Get information from the knowledge base with ask
    hostile = aima.logic.fol_fc_ask(KB, aima.utils.expr('Hostile(x)'))
    criminal = aima.logic.fol_fc_ask(KB, aima.utils.expr('Criminal(x)'))
    # Print answers
    print('Hostile?')
    print(list(hostile))
    print('\nCriminal?')
    print(list(criminal))
    print()
# Tell python to run main method
if __name__ == "__main__": main()