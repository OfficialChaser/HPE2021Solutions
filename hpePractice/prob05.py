dates = []
dups = []
numOfDates = int(input())

for _ in range(numOfDates):
    date = str(input())
    dates.append(date[:5])

for date in dates:
    if (dates.count(date) > 1):
        if (date not in dups):
            dups.append(date)

print(len(dups)) 
if (len(dups) > 0):
    for dup in dups:
        print(dup, end=" ")
else:
    print("duplicates: None", end="")

print()
