from sys import stdin

def main():
    dial_val = 50
    res = 0

    for line in stdin:
        direction = line[0]
        rotation = int(line[1:])

        if direction == "L":
            dial_val = (dial_val - rotation) % 100
        else:
            dial_val = (dial_val + rotation) % 100
        if dial_val == 0:
            res += 1
    print(res)

if __name__ == "__main__":
    main()