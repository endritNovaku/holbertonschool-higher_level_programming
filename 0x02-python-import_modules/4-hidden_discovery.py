#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hidden4 = dir(hidden_4)
    filtered = []
    for i in hidden4:
        if i.startswith("_"):
            continue
        else:
            filtered.append(i)

    length = len(filtered)
    for i in range(length):
        print(filtered[i])
