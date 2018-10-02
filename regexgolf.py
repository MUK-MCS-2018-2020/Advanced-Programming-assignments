
import re
import regexgolf

def verify(regex, winners, losers):
    "Return true iff the regex matches all winners but no losers."
    missed_winners = {W for W in winners if not re.search(regex, W)}
    matched_losers = {L for L in losers if re.search(regex, L)}
    if missed_winners:
      print ("Error: should match but did not:", ', '.join(missed_winners))
    if matched_losers:
        print ("Error: should not match but did:", ', '.join(matched_losers))
        return not (missed_winners or matched_losers)

def puzzlewords(puzzle):
    "Returns a dictionary containing the words to match and the words to reject"
    matchwords = []
    rejectwords = []
    result = {}
    try:
        if (puzzle<1) | (puzzle>30):
            print ("Need puzzle between 1 and 30")
            return []
        
        content = open('wordlist%d.txt' % puzzle,'r').read()
        
        matchlist = True
        for line in content.splitlines():        
            if (line == ''):
                matchlist = False
            else:
                if matchlist:
                    matchwords.append(line)
                else:
                    rejectwords.append(line)
        
        result['matchwords'] = matchwords
        result['rejectwords'] = rejectwords   
        return result
    except (TypeError, ValueError):
        print ("Need puzzle to be a number")
        return []
    except (IOError) as e:
        print ("Puzzle files not found, please use a puzzle value between 1 and 11")
        return []

def verifypuzzle(regex,puzzle):
    "Verifies if the regular expression solves the puzzle"
    words = puzzlewords(puzzle)
    if (len(words)>0):
        return verify(regex,words['matchwords'],words['rejectwords'])
    else:
        print ("Invalid puzzle!")


print (regexgolf.puzzlewords(2)['matchwords'])
print (regexgolf.puzzlewords(2)['rejectwords'])