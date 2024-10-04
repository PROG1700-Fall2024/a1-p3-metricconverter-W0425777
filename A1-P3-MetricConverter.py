#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    print("\nImperial to Metric Conversion\n")
    #pritn title

    tons = float(input("Enter the number of tons: "))
    #input tones,stones,pounds ounces(make sure to convert to float or int)

    stones = float(input("Enter the number of stones: "))

    pounds = float(input("Enter the of pounds: "))

    ounces = float(input("Enter the number of Ounces: "))

    tOunces = 35840*tons+224*stones+16*pounds+ounces
    #equation for Total Ounces

    tKilos = (tOunces/35.274)
    #equation for Total Kilos

    mTons = int(tKilos/1000)
    #equation for Total Tons

    mKilos = int(tOunces/35.274)-(mTons*1000)
    #Make new value to - tons form kilos

    grams = (tKilos-(int(tOunces/35.274)))*1000
    #equation for grams???

    print("\nThe metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.\n".format(mTons,mKilos,grams))
    #Pray that it works

    # YOUR CODE ENDS HERE

main()