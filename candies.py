candies = [2,3,5,1,3]
extraCandies = 3
m=max(candies)
print([c+extraCandies>=m for c in candies])