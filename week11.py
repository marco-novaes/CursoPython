def tax(bill):
    """ Adds 8% tax to a restairant bill. """
    bill *= 1.08
    print("With Tax: %f " % bill)
    return bill


def tip(bill):
    """ Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("With tip: %f" % bill)
    return bill


meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)

score_math = float(input("Enter the score you received for Math: "))
score_English = float(input("Enter the score you received for English: "))
score_PE = float(input("Enter the score you received for PE: "))
score_Science = float(input("Enter the score you received for Science: "))
score_Art = float(input("Enter the score you received for Art: "))


def score(score_math):
    if score_math >= 90 and score_math <= 100:
        print ("A")
        return score_math
    elif score_math >= 87 and score_math <= 90:
        print ("B+")
        return score_math
    elif score_math >= 83 and score_math <= 87:
        print ("B")
        return score_math
    elif score_math >= 80 and score_math <= 83:
        print ("B-")
        return score_math
    elif score_math >= 77 and score_math <= 80:
        print ("C+")
        return score_math
    elif score_math >= 73 and score_math <= 77:
        print ("C")
        return score_math
    elif score_math >= 70 and score_math <= 73:
        print ("C-")
        return score_math
    elif score_math >= 67 and score_math <= 70:
        print ("D+")
        return score_math
    elif score_math >= 63 and score_math <= 67:
        print ("D")
        return score_math
    elif score_math >= 60 and score_math <= 63:
        print ("D-")
        return score_math
    else:
        print ("F")
        return score_math


print("For a score of " + str(score_math) + " , your grade is " + score(score_math))


def score(score_English):
    if score_English >= 90 and score_English <= 100:
        print ("A")
        return score_English
    elif score_English >= 87 and score_English <= 90:
        print ("B+")
        return score_English
    elif score_English >= 83 and score_English <= 87:
        print ("B")
        return score_English
    elif score_English >= 80 and score_English <= 83:
        print ("B-")
        return score_English
    elif score_English >= 77 and score_English <= 80:
        print ("C+")
        return score_English
    elif score_English >= 73 and score_English <= 77:
        print ("C")
        return score_English
    elif score_English >= 70 and score_English <= 73:
        print("C-")
        return score_English
    elif score_English >= 67 and score_English <= 70:
        print ("D+")
        return score_English
    elif score_English >= 63 and score_English <= 67:
        print ("D")
        return score_English
    elif score_English >= 60 and score_English <= 63:
        print ("D-")
        return score_English
    else:
        print ("F")
        return score_English


print("For a score of " + str(score_English) + " , your grade is " + score(score_English))


def score(score_PE):
    if score_PE >= 90 and score_PE <= 100:
        print ("A")
        return score_PE
    elif score_PE >= 87 and score_PE <= 90:
        print ("B+")
        return score_PE
    elif score_PE >= 83 and score_PE <= 87:
        print ("B")
        return score_PE
    elif score_PE >= 80 and score_PE <= 83:
        print ("B-")
        return score_PE
    elif score_PE >= 77 and score_PE <= 80:
        print ("C+")
        return score_PE
    elif score_PE >= 73 and score_PE <= 77:
        print ("C")
        return score_PE
    elif score_PE >= 70 and score_PE <= 73:
        print ("C-")
        return score_PE
    elif score_PE >= 67 and score_PE <= 70:
        print ("D+")
        return score_PE
    elif score_PE >= 63 and score_PE <= 67:
        print ("D")
        return score_PE
    elif score_PE >= 60 and score_PE <= 63:
        print ("D-")
        return score_PE
    else:
        print ("F")
        return score_PE


print("For a score of " + str(score_PE) + " , your grade is " + score(score_PE))


def score(score_Science):
    if score_Science >= 90 and score_Science <= 100:
        print ("A")
        return score_Science
    elif score_Science >= 87 and score_Science <= 90:
        print ("B+")
        return score_Science
    elif score_Science >= 83 and score_Science <= 87:
        print ("B")
        return score_Science
    elif score_Science >= 80 and score_Science <= 83:
        print ("B-")
        return score_Science
    elif score_Science >= 77 and score_Science <= 80:
        print ("C+")
        return score_Science
    elif score_Science >= 73 and score_Science <= 77:
        print ("C")
        return score_Science
    elif score_Science >= 70 and score_Science <= 73:
        print ("C-")
        return score_Science
    elif score_Science >= 67 and score_Science <= 70:
        print ("D+")
        return score_Science
    elif score_Science >= 63 and score_Science <= 67:
        print ("D")
        return score_Science
    elif score_Science >= 60 and score_Science <= 63:
        print ("D-")
        return score_Science
    else:
        print ("F")
        return score_Science


print("For a score of " + str(score_Science) + " , your grade is " + score(score_Science))


def score(score_Art):
    if score_Art >= 90 and score_Art <= 100:
        print ("A")
        return score_Art
    elif score_Art >= 87 and score_Art <= 90:
        print ("B+")
        return score_Art
    elif score_Art >= 83 and score_Art <= 87:
        print ("B")
        return score_Art
    elif score_Art >= 80 and score_Art <= 83:
        print ("B-")
        return score_Art
    elif score_Art >= 77 and score_Art <= 80:
        print("C+")
        return score_Art
    elif score_Art >= 73 and score_Art <= 77:
        print("C")
        return score_Art
    elif score_Art >= 70 and score_Art <= 73:
        print ("C-")
        return score_Art
    elif score_Art >= 67 and score_Art <= 70:
        print ("D+")
        return score_Art
    elif score_Art >= 63 and score_Art <= 67:
        print ("D")
        return score_Art
    elif score_Art >= 60 and score_Art <= 63:
        print ("D-")
        return score_Art
    else:
        print ("F")
        return score_Art


print("For a score of " + str(score_Art) + " , your grade is " + score(score_Art))