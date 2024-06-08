from Test import evaluate
try:
    k = 0
    while True:
        print("data:")
        a = str(input())
        res = evaluate(a, k)
        k += 1
        pass
except SystemExit:
    print("Program Stopped!")