# 997. Find the town judge

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

def findJudge(n,trust):
    trust_count = [0] * (n + 1)
    for a, b in trust:
        #print(a,b)
        trust_count[a] -= 1
        trust_count[b] += 1
        print(trust_count)
    for i in range(1, n + 1):
        if trust_count[i] == n - 1:
            return i
    return -1
