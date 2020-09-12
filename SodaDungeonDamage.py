from numpy import floor
"""
dmg = final damage
b = damage before relics
R = ratio of essence spent on flat Attack to Magic Boost
"""
eCost = 0. #essence cost
CAdd  = 0
FAdd  = 0
PAdd  = 0

b = 50 #int(input("Damage from items: "))
FL = 948 #int(input("Flat damage relic Level: "))
PL = 1079 #int(input("Magic percent relic Level: "))
CL = 956 #int(input("Dark Mage's Level: "))
essence = 958900 #int(input("How much essence do you have? "))

def d(FL, CL, PL):
    return int((b+2*CL+2*FL)*(1+.002*PL))


while eCost < essence:
    dmg = d(FL, CL, PL)

    # f for Flat damage relic (+2)
    fCost = floor(FL**(1.3))
    fDmg = d(FL+1, CL, PL) - dmg
    fEff = fDmg / fCost

    # c for Character relic (+2 to all stats)
    cCost = floor(CL**(1.3))
    cDmg = d(FL, CL+1, PL) - dmg
    cEff = cDmg / cCost

    # p for Percent damage relic (+.2%)
    pCost = floor(PL**(1.3))
    pDmg = d(FL, CL, PL+1) - dmg
    #print (d(FL, CL, PL+1), dmg)
    pEff = pDmg / pCost

    if cEff >= pEff and cEff >= fEff and eCost + floor(CL**(1.3)) < essence:
        eCost += floor(CL**(1.3))
        CL    += 1
        CAdd  += 1
    elif pEff >= fEff and pEff >= cEff and eCost + floor(PL**(1.3)) < essence:
        eCost += floor(PL**(1.3))
        PL    += 1
        PAdd  += 1
    elif eCost + floor(FL**(1.3)) < essence:
        eCost += floor(FL**(1.3))
        FL    += 1
        FAdd  += 1
    else:
        break

    dmg = d(FL, CL, PL)
    print("\t\t", "Character\t Flat\t\t Percentage")
    print("Level:\t\t", int(CL), "\t\t", int(FL), "\t\t", int(PL))
    print("Dmg diff: \t", int(cDmg), "\t\t", int(fDmg), "\t\t", int(pDmg))
    print("Cost: \t\t", int(cCost), "\t\t", int(fCost), "\t\t", int(pCost))
    #print("Efficiency: \t", format(round(cEff, 3), '1.4e'), "\t", \
    #       format(round(fEff, 3), "1.4e"), "\t", format(round(pEff, 3), '1.4e'))
    print("Levels added:\t", CAdd, "\t\t", FAdd, "\t\t", PAdd)
    print("Damage: ", int(dmg))
    print()

"""
for i in range(500):
    newLevel = "f" #input("upgrade which? Flat or Percent? (f/p): ")
    if newLevel == 'f':
        FL += 1
        eCost += floor(FL**(1.3))
    if newLevel == 'p':
        PL += 1
        eCost += floor(PL**(1.3))
    dmg = int(0.55 * (b+2*FL)*(1.002*PL))
    print("######################################################")
    print("TOTAL DAMAGE:\t\t", dmg)
    print("total essence Cost:\t", int(eCost))
    print("Flat Dmg Level:\t\t", int(FL))
    print("Percent dmg Level:\t", int(PL))
    print("Damage per essence:", dmg/eCost)
"""