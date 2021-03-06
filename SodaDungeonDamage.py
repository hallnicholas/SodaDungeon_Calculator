#from numpy import floor
"""
dmg = final damage
b = damage before relics
R = ratio of essence spent on flat Attack to Magic Boost
"""
eCost = 0. #essence cost
CAdd  = 0
FAdd  = 0
PAdd  = 0

try:
    f = open("prevLvls.txt", 'r')
    b = int(f.readline().rstrip('\n'))
    FL = int(f.readline().rstrip('\n'))
    PL = int(f.readline().rstrip('\n'))
    CL = int(f.readline().rstrip('\n'))
    essence = f.readline()
    print("\nYour previously input levels are:")
    print("Damage from Items:\t", b)
    print("Relic of Attack:\t", FL)
    print("Relic of Magic Boost:\t", PL)
    print("Relic of [Character]:\t", CL)
    f.close()
    if input("\nDo you want to use these values? \
type 'no' to input new values, or just hit enter to  \
continue.\n>").lower() == 'no':
        raise Exception("Clean slate, here we go..\n")
    essence = float(input("\nHow much essence do you have? "))
except Exception:
    b = int(input("Damage from items: "))
    FL = int(input("Flat damage relic Level: "))
    PL = int(input("Magic percent relic Level: "))
    CL = int(input("Dark Mage's Level: "))
    essence = int(input("How much essence do you have? "))

def d(FL, CL, PL):
    return int((b+2*CL+2*FL)*(1+.002*PL))


while eCost < essence:
    dmg = d(FL, CL, PL)

    # f for Flat damage relic (+2)
    fCost = round(FL**(1.3)-.5)
    fDmg = d(FL+1, CL, PL) - dmg
    fEff = fDmg / fCost

    # c for Character relic (+2 to all stats)
    cCost = round(CL**(1.3)-.5)
    cDmg = d(FL, CL+1, PL) - dmg
    cEff = cDmg / cCost

    # p for Percent damage relic (+.2%)
    pCost = round(PL**(1.3)-.5)
    pDmg = d(FL, CL, PL+1) - dmg
    #print (d(FL, CL, PL+1), dmg)
    pEff = pDmg / pCost

    if cEff >= pEff and cEff >= fEff and eCost + round(CL**(1.3)) < essence:
        eCost += round(CL**(1.3)-.5)
        CL    += 1
        CAdd  += 1
    elif pEff >= fEff and pEff >= cEff and eCost + round(PL**(1.3)) < essence:
        eCost += round(PL**(1.3)-.5)
        PL    += 1
        PAdd  += 1
    elif eCost + round(FL**(1.3)-.5) < essence:
        eCost += round(FL**(1.3)-.5)
        FL    += 1
        FAdd  += 1
    else:
        break

    dmg = d(FL, CL, PL)
    """
    print("___________________________________________________________")
    print("\t\t", "Character\t Flat\t\t Percentage")
    print("Final Level:\t", int(CL), "\t\t", int(FL), "\t\t", int(PL))
    print("Dmg diff: \t", int(cDmg), "\t\t", int(fDmg), "\t\t", int(pDmg))
    print("Cost: \t\t", int(cCost), "\t\t", int(fCost), "\t\t", int(pCost))
    print("Efficiency: \t", format(round(cEff, 3), '1.4e'), "\t", \
           format(round(fEff, 3), "1.4e"), "\t", format(round(pEff, 3), '1.4e'))
    print("Levels added:\t", CAdd, "\t\t", FAdd, "\t\t", PAdd)
    print("Damage before boosts: ", int(dmg))
    """


print("___________________________________________________________")
print("\t\t", "Character\t Flat\t\t Percentage")
print("Final Level:\t", int(CL), "\t\t", int(FL), "\t\t", int(PL))
print("Levels added:\t", CAdd, "\t\t", FAdd, "\t\t", PAdd)

if input("\nBefore the program exits, \
do you want to save these levels? for next time?\n>") == 'no':
    exit()
else:
    pass

f = open("prevLvls.txt", 'w')

print(b, "\n", FL, "\n", PL, "\n", CL, sep = '', file=f)

close = input("Hit enter to close.\n")