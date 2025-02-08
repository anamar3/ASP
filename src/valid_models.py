"""Module for checking whether a model satisfies all rules and constraints."""

from src.exceptions import WrongFact, ContradictingConstraints, InvalidSyntax

def checkFactExists(facts, fact) -> bool:
    """Checks if a fact exists in the list of facts."""
    for el in facts:
        if(el.startswith(fact)):
          return True
    return False

def checkIfAllConditionsApply(model,theRest,flag):
    accFlag = True

    for rest in theRest:
        if(rest[len(rest)-1] == "."): 
            rest = rest[:-4]
        else:   
            rest = rest[:-3]
        if(rest.startswith("not cannot_")):
            rest = rest[4:]
            if(not flag):
                if(model.get(rest)):
                    return False
            else:
                if(not model.get(rest)):
                    return False
        elif(rest.startswith("not ")):
            rest = rest[4:]
            if(not flag):
                if(not model.get(rest)):
                     return False
            else:
                if(model.get(rest)):
                     return False
            if(not flag):
                if(not model.get(rest)):
                     return False
            else:
                if(model.get(rest)):
                     return False
    return accFlag

def checkValidModel(model,second,constraints,first,TheRest) -> bool | None:
    """Checks if a model is valid given constraints and rules."""

    if (model.get(second)):
            if constraints:
                for constraint in constraints:
                    head = constraint[2:].split(", ")[0][1:-3]
                    body = constraint[2:].split(", ")[1][:-4]
                    try:
                        if (head == second): 
                            flag = True
                            if(body.startswith("not")):
                                body = body[4:]
                                flag = False
                            
                            if(body == first):
                                if(not checkIfAllConditionsApply(model,TheRest,flag)):
                                    return False
                                else:
                                    return True
                            else:
                                continue
                        else:
                            raise WrongFact
                    except WrongFact as s:
                        print(s)
                        return False
            else:
             return True
    else:
      return True
          
def findRuleFacts(rules: list, body: str) -> list[str] | None:
    """ Finds all facts in a rule."""
    if(body.startswith("not")):
        body = body[4:]
    
    for rule in rules:
        r = rule.split("(X) :- ")[0]
        if(r == body):
          temp = rule.split(" :- ")[1].split(", ")[1:]
          u = temp[len(temp)-1][:-1]
          temp[len(temp) - 1] = u
          return temp

def checkContradictingBodies(factOfFirs,factsofSec):
    
    for f1 in factOfFirs:
        flag = True
        if(f1.startswith("not")):
            if(f1[len(f1)-1] == "."):
             f1 = f1[4:-4]
            else:  
             f1 = f1[4:-3]
            flag = False
        for f2 in factsofSec:
            if(f2[len(f2)-1] == "."):
              f2 = f2[:-4]
            else:   
              f2 = f2[:-3]
            if(f1 == f2 and not flag):
                return False
            elif(f1 == f2 and flag):
                continue
            elif(f2.startswith("not") and not flag and f2[4:] == f1):
                continue
            elif(f2.startswith("not") and flag and f2[4:] == f1):
                return False

    return True

def checkRulesAndConstraintsValid(rules,constraints) -> bool:
    """ Checks if rules and constraints are valid (no contradictions). """

    for firs in constraints:
     
     headF = firs[2:].split(", ")[0][1:-3]
     bodyF = firs[2:].split(", ")[1][:-4]

     for sec in constraints[1:]:
      
      headS = sec[2:].split(", ")[0][1:-3]
      bodyS = sec[2:].split(", ")[1][:-4]

      if((bodyF.startswith('not') and bodyF[4:] == bodyS) or (bodyS.startswith("not") and bodyS[4:] == bodyF)): 
        return False
      
      if(headS == headF):
         
            factsOfFirs = findRuleFacts(rules,bodyF)
            factsOfSec = findRuleFacts(rules,bodyS)
            return checkContradictingBodies(factsOfFirs,factsOfSec)      
    return True

def evaluate_model(model,rules,constraints,facts) ->  bool:
    """Evaluates whether a model satisfies all rules and constraints."""

    toReturn = True
    try:
      if( not checkRulesAndConstraintsValid(rules,constraints)): raise ContradictingConstraints
    except ContradictingConstraints as s:
        print(s)
        return False
    else:
        for rule in rules:
            first = rule.split("(X) :- ")[0]
            second = rule.split(" :- ")[1].split("(X)")[0]
            theRest = rule.split(" :- ")[1].split(", ")[1:]
            try:
                for rest in theRest:

                    if(rest[len(rest)-1] == "."):
                      rest = rest[:-4]
                    else:
                      rest = rest[:-3]

                    if((rest.startswith("not cannot_"))):
                        rest = rest[4:]
                        flag = False
                    elif((rest.startswith("cannot_")) and first == rest[7:]):
                        raise InvalidSyntax
                
                    if(not checkFactExists(facts,rest)):
                        raise InvalidSyntax
            except InvalidSyntax as s:
                  print(s)
                  return False
            try:
                if not (second == facts[0].split('(')[0]):
                  raise WrongFact
            except WrongFact as s:
                print(s)
                return False
            
            if(not checkValidModel(model,second,constraints,first,theRest)):
                return False         
        return True
