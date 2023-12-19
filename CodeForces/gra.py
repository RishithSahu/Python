#nitially, all of its cities are in economic collapse. The government can choose to rebuild certain cities. Additionally, any collapsed city which has at least one vertically neighboring rebuilt city and at least one horizontally neighboring rebuilt city can ask for aid from them and become rebuilt without help from the government. More formally, collapsed city positioned in (i,j)
#  can become rebuilt if both of the following conditions are satisfied:

# At least one of cities with positions (i+1,j)
#  and (i−1,j)
#  is rebuilt;
# At least one of cities with positions (i,j+1)
#  and (i,j−1)
#  is rebuilt.
# If the city is located on the border of the matrix and has only one horizontally or vertically neighbouring city, then we consider only that city.

no_of_test_cases = int(input())

for i in range(no_of_test_cases):
    