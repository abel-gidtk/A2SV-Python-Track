# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
countries = set()

for i in range(num):
    country = str(input())
    countries.add(country)

print(len(countries))
