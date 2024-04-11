#

#A population can be modeled by the following:
#future population = (current population)*(1+r)^(time in years) 
#Have the user enter the current population, the rate of growth as a decimal and the number of DAYS.
#Calculate the expected future population

#Enter the population: 25000000
#Enter the rate of growth in percent: 2.1
#Enter the number of days: 12
#There will be 25017087 people after 12 days

input("Wellcome to lord beelzebub's population calculator!!!")
input("This calculator takes a population, its growth rate, and a peroid of time, and calculates what the population will be later in time.")
nPopulation = int(input("Please enter the current populace count: "))
Irate = float(input(f"please enter the rate of growth in percentage: "))
nT = float(input(f"finally, please enter the number of days: "))
Trate = Irate * 0.01
nTy = nT / 365
fPopu = ( nPopulation * ( 1 + Trate ) ** nTy )
DeltaP = fPopu - nPopulation
fPopu = int(round(fPopu, 0))
DeltaP = int(round(DeltaP, 0))
print(f"The populace will be become {fPopu}, growing by {DeltaP} people.")