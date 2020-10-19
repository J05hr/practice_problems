import math

def differentTeams(skills):
    # check empty
    if skills == "":
        return 0

    # get the skills set and make sure there are exactly 5
    skillsset = set(skills)
    if len(skillsset) != 5:
        return 0

    # check for min skill count and check for any other chars
    minskill = math.inf
    for item in skillsset:
        if item not in "bcmpz":
            return 0
        if skills.count(item) < minskill:
            minskill = skills.count(item)

    return minskill


if __name__ == '__main__':
    skills = 'ccccccmmmmmmpppppzzzzzzzzzzzzzzzzzzzz'

    print(differentTeams(skills))