import random

def getGaussListValues(mean, stddev, sample):
    values=[random.gauss(mean,stddev) for i in range(sample)]
    return values

def getRandomNumFromRange(range):
    value = random.randrange(0,range)
    return value

def getSexo():
    value = random.choice(["M", "F"])
    return value
