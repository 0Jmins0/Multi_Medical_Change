from Test import evaluate
try:
    k = 0
    while True:
        # a = input()
        res = evaluate(0, k)
        k += 1
        pass
except SystemExit:
    print("Program Stopped!")