#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    le = len(sys.argv)
    sum = 0
    for i in range(1, le):
        sum += int(sys.argv[i])
    print(f"{sum}")
