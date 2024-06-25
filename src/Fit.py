from Test import evaluate
try:
    k = 1
    while True:
        print("data:")
        a = str(input())
        res = evaluate(a, k)

        pass
except SystemExit:
    print("Program Stopped!")