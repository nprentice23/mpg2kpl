'''
A unit converter that can convert MPG to KPL
'''
# do the simplest thing that can work
# ask the user to input a mpg value
mpg = input("what is the mpg? ")
# convert the input into a numerical (float) value 
mpg = float(mpg)
print (mpg * 1.609344 * 0.2641720524)
