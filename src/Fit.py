from Test import evaluate
import Global_Parameter as GP
if __name__ == '__main__':
    try:
        k = GP.RANDOM_SEED
        while True:
            print("choose data source(1 or 2)\n 1: data from cola \n 2: data from random")
            p = eval(input())
            if p == 2:
                print("choose a number between 0 - 49")
            else:
                print("choose a number from[6,30,121,165]")
            a = str(input())
            res = evaluate(a, k, p)
    except SystemExit:
        print("Program Stopped!")