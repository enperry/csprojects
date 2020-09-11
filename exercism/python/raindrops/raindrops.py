def convert(number):
    resultString = ""

    if(number % 3 == 0):
        resultString = resultString + "Pling"
    if(number % 5 == 0):
        resultString = resultString + "Plang"
    if(number % 7 == 0):
        resultString = resultString + "Plong"
    
    if(resultString == ""):
        return str(number)

    return resultString