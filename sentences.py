import random
def main():
    requirements = [["single","past"],\
                    ["single","present"],\
                    ["single","future"],\
                    ["plural","past"],\
                    ["plural","present"],\
                    ["plural","future"]]
    
    for i in range(len(requirements)):
       quantity = requirements[i][0]
       tense = requirements[i][1]

       if quantity == "single":
          quantity = 1
          make_sentence(quantity, tense)
       else:
          quantity = 2
          make_sentence(quantity, tense)
   

def get_determiner(quantity):

  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]

  word = random.choice(words)
  return word

def get_noun(quantity):
  
  if quantity == 1:
     noun = ["bird", "boy", "car", "cat", "child",\
              "dog", "girl", "man", "rabbit", "woman"]
     noun_select = random.choice(noun)
     return noun_select
  else:
     nouns = ["birds", "boys", "cars", "cats", "children",\
             "dogs", "girls", "men", "rabbits", "women"]
     nouns_select = random.choice(nouns)
     return nouns_select

def get_verb(quantity, tense):
  if tense == "past":
     verb = ["drank", "ate", "grew", "laughed", "thought",\
             "ran", "slept", "talked", "walked", "wrote"]
     verb = random.choice(verb)
     return verb
  
  elif tense == "present" and quantity == 1:
     verb = ["drinks", "eats", "grows", "laughs", "thinks",\
             "runs", "sleeps", "talks", "walks", "writes"]
     verb = random.choice(verb)
     return verb
  
  elif tense == "present" and quantity != 1:
     verb = ["drink", "eat", "grow", "laugh", "think",\
             "run", "sleep", "talk", "walk", "write"]
     verb = random.choice(verb)
     return verb
  
  elif tense == "future":
     verb = ["will drink", "will eat", "will grow", "will laugh",\
             "will think", "will run", "will sleep", "will talk",\
                "will walk", "will write"]
     verb = random.choice(verb)
     return verb
  
     
def make_sentence(quantity, tense):
   print(f"{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_verb(quantity, tense)}.")

def get_preposition():
  preposition = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
  
  prepition_select = random.choice(preposition)

main()