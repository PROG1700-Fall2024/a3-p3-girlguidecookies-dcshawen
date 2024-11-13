"""
    Title: Program 3 - Girl Guide Cookies
    Author: Dan Shaw w0190983  
    Description: The organizers of the annual Girl guide cookie sale event want to raise the stakes on the number of cookies sold and are offering cool prizes to those guides who go above and beyond in their sales efforts. The organizers want a program to print the guide list and their prizes.
"""

import ds_tower1_3_0 as tower

def main():
    # Local variables
    guideCount = getGuideCount()
    print(guideCount)
    title = "Girl Guide Cookie Sell-Off"

    print(tower.Template.titleOut(title))

def getGuideCount():
    """ Returns the number of guides participating in the cookie sell-off """
    instr = "Enter the number of guides selling cookies."
    
    print(instr)

    while (guideCount := tower.Validator.validateInt(input(tower.PROMPT))) == None or guideCount <= 0:
        print("Invalid input. Please enter the number of guides selling cookies.")

    return guideCount

if __name__ == "__main__":
    main()