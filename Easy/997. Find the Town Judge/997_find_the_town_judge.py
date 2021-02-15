"""
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
1) The town judge trusts nobody.
2) Everybody (except for the town judge) trusts the town judge.
3) There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Constraints:
- 1 <= N <= 1000
- 0 <= trust.length <= 10^4
- trust[i].length == 2
- trust[i] are all different
- trust[i][0] != trust[i][1]
- 1 <= trust[i][0], trust[i][1] <= N
"""

# ATTEMPT 1 THOUGHTS:
# I had a lot of trouble with this problem as first (so much for easy...). I was definitely 
# overthinking it since I was doing too much with list comprehension, etc. 
# 
# I didn't realize this was a directed graph problem and only found out once I came up with 
# the solution below and looked at other's solutions to see where I could improve. 
# I should have realized sooner since the problem was dealing with relationships (which can be modeled 
# with nodes and edges). However, I believe this is the first graph problem I encountered
# on LeetCode, so I know better for next time!  

# --------------- ATTEMPT 1

class Solution:
    def find_judge(self, N: int, trust: List[List[int]]) -> int:
    """
    If there is a town judge, finds them. Otherwise, returns -1. 
    
    This function runs in O(N + M) time, where N is the number of people in the town, and M is the list of elements in the trust list. It has O(N + M) space complexity as well. 
    """
        # Person 1 is the town judge if there is only one person in the list of people
        if N == 1:
            return N
        
        # Generate list of suspects; initially includes every person
        sus = []
        for x in range(1, N + 1):
            sus.append(x)
        
        # Generate list of every person that is trusted, including duplicates
        people_trusted = []
        for x in trust:
            # If a person trusts someone else, they cannot be the town judge
            if x[0] in sus:
                sus.remove(x[0])
            people_trusted.append(x[1])
        
        town_judge = -1
        # Town judge cannot be determined if there are multiple suspects
        if len(sus) != 1:
            return town_judge
        # The town judge must be trusted by N - 1 people (the number of townspeople minus themselves)
        elif people_trusted.count(sus[0]) == (N - 1):
            town_judge = sus[0]
        
        return town_judge