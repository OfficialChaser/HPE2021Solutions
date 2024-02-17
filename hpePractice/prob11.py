f = str(input().strip("F "))
k = str(input().strip("K "))
x = str(input().strip("X "))

if (f == "?"):
    k = float(k)
    x = float(x)
    result = round((-k * x), 2)
    print(f"F {result}")
elif (k == "?"):
    f = float(f)
    x = float(x)
    if (x != 0):
        result = round((-f / x), 2)
        print(f"K {result}")
    else:
        print("K 0")
else:
    f = float(f)
    k = float(k)
    if (k != 0):
        result = round((-f / k), 2)
        print(f"X {result}")
    else:
        print("X 0")