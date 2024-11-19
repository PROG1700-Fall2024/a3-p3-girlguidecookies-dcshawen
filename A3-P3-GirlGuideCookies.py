"""
    Title: Program 3 - Girl Guide Cookies
    Author: Dan Shaw w0190983  
    Description: The organizers of the annual Girl guide cookie sale event want to raise the stakes on the number of cookies sold and are offering cool prizes to those guides who go above and beyond in their sales efforts. The organizers want a program to print the guide list and their prizes.
"""

import ds_tower1_3_0 as tower

class Guide:
    def __init__(self, name:str, sales:int):
        self.name = name
        self.sales = sales
        self.prize = ""

def main():
    # Local variables
    title = "Girl Guide Cookie Sell-Off"
    avgOut = "The average number of boxes sold by {0} girl scouts is: {1}"

    print(tower.Template.titleOut(title))
    guideCount = getGuideCount()
    guides = getNamesAndSales(guideCount)

    averageSales = getAverage(getSum(guides), len(guides))
    prizes = getPrizes()
    guides = assignPrizes(guides, prizes, averageSales)

    print(avgOut.format(guideCount, averageSales))
    outputResults(guides)

def outputResults(guides):
    """ Outputs the results of the cookie sell-off """

    print(f"\n{'Guide':<20}{'Sales':<20}{'Prize':<20}") # NOTE These fun little print formatting rules are cool. 
    print(tower.Template.getLine("-"))

    for g in guides:
        print(f"{g.name:<20}{g.sales:<20}{g.prize:<20}")

def assignPrizes(guides, prizes, average):
    """ Assigns prizes to guides based on sales """
    max = 0

    # NOTE I don't like these loops. It feels clunky. I don't know if I'll get a chance to rewrite it, but just know I do not like this logic structure. 
    # Assign all prizes except the first place prize first, then loop again and overwrite the highest sales number with the first place prize
    for g in guides:
        if g.sales > max: # Figure out what the highest sales number is 
            max = g.sales

        if g.sales > average: # Assign second and third place prizes 
            g.prize = prizes[1]
        elif g.sales >= 1:
            g.prize = prizes[2]

    for g in guides: # Assign first place prize
        if g.sales == max:
            g.prize = prizes[0]
        
    return guides

def getPrizes():
    """ Returns the list of prizes in descending order """

    return [ "Girl Guide Jamboree", 
            "Super Seller Badge", 
            "Leftover Cookies" ]

def getSum(guides):
    """ Returns the sum of all sales """
    sum = 0
    for g in guides:
        sum += g.sales

    return sum

def getAverage(sum, len):
    """ Returns the average """
    return sum / len

def getGuideCount():
    """ Returns the number of guides participating in the cookie sell-off """
    instr = "Enter the number of guides selling cookies."
    
    print(instr)

    while (guideCount := tower.Validator.validateInt(input(tower.PROMPT))) == None or guideCount <= 0:
        if guideCount == 0:
            print("Then why are you even here?")
            exit() # End the program if no guides participated

        print("Invalid input. Please enter the number of guides selling cookies.")

    return guideCount

def getNamesAndSales(guideCount:int):
    guides = []
    for i in range(guideCount):
        name = getName(i)
        sales = getSales(name)
        guides.append(Guide(name, sales))

    return guides

def getName(currentGuide:int):
    """ Returns the name of a guide """
    instr = "Enter the name of the guide #{0}"

    print(instr.format(currentGuide + 1))
    name = input(tower.PROMPT) # No validation on this string because we do not live in a world where we can assume all names are only letters
    
    return name

def getSales(name:str):
    """ Returns the number of boxes sold by a guide """
    instr = "Enter the number of boxes sold by {0}"

    print(instr.format(name))

    while (sales := tower.Validator.validateInt(input(tower.PROMPT))) == None or sales < 0:
        print("Invalid input. Please enter a number equal to, or greater than, 0.")

    return sales

if __name__ == "__main__":
    main()