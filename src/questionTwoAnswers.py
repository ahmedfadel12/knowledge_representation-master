from utils import *
from logic2 import *

# question 2.1
#  read(maria, logic programming book) ==> by(peter lucas)
maria = Symbol("maria")
peter_lucas = Symbol("peter lucas")
read = Symbol(f" read ({maria}, logic programming book)")
by = Symbol(f"by ({peter_lucas})")
knowledge_for_question1 = And(Implication(read, by))
# print(knowledge_for_question1.formula())

#-----------------------------------------------------------

# question 2.2
# is_girl(x) ==> like(x, shopping)
is_girl = Symbol("is_girl(x)")
shopping = Symbol("shopping")
like = Symbol(f"like(x, {shopping} )")
knowledge_for_question2 = And(Implication(is_girl, like))
# print(knowledge_for_question2.formula())

#-----------------------------------------------------------
# question 2.3
# ? likes( x , shopping)
who = Symbol("?")
knowledge_for_question3  = And(who ,like)
# print(knowledge_for_question3.formula())
#-----------------------------------------------------------
# question 2.4
# city( x ,big , crowdy) ==> hates(kirke, x)
city = Symbol("city(x, big, crowdy)")
hates = Symbol("kirke, x")
knowledge_for_question4 = And(Implication(city, hates))
# print(knowledge_for_question4.formula())


