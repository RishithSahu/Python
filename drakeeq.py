# A program to find the no of Civilisations in the universe.

n = int(input("Average no. of planets that could support life "))
i = int(input("Percentage that devlop intelligent life "))
c = int(input("Percentage of those that would be willing to communicate "))
L = int(input("Expected lifetime of civilisations "))

N = 7 * (0.4) * (0.13) * n/100.0 * (i/100) * (c/100) * L
print("The estimated no. of civilisations detectable are ", N)