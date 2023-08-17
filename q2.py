"""
Q2
The number of goals achieved by two football teams in matches in a league is given in the
form of two lists. For each match of team B, compute the total number of matches of team A
where team A has scored less than or equal to the number of goals scored by team B in that
match.
Example:
teamA = [1, 2, 3]
teamB = [2, 4]
Team A has played three matches and has scored teamA = [1, 2, 3] goals in each match
respectively. Team B has played two matches and has scored teamB = [2, 4] goals in each
match respectively. For 2 goals scored by team B in its first match, team A has 2 matches
with scores 1 and 2. For 4 goals scored by team B in its second match, team A has 3
matches with scores 1, 2 and 3. Hence, the answer is [2, 3].
"""


def count_matches(teamA: list, teamB: list) -> list:
    result = []
    for goalsB in teamB:
        count = 0
        for goalsA in teamA:
            if goalsA <= goalsB:
                count += 1
        result.append(count)
    return result
