from sys import stdin

def part1():
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

def part2():
    dial_val = 50
    res = 0

    for line in stdin:
        direction = line[0]
        rotation = int(line[1:])
        
        if direction == "L":
            for _ in range(rotation):
                dial_val -= 1
                if dial_val < 0:
                    dial_val = 99
                if dial_val == 0:
                    res += 1
        else:
            for _ in range(rotation):
                dial_val += 1
                if dial_val > 99:
                    dial_val = 0
                if dial_val == 0:
                    res += 1

    print(res)

if __name__ == "__main__":
    part2()