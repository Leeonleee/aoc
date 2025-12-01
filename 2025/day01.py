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

        # number of full rotations
        res += rotation // 100
        rotation %= 100
        
        if direction == "L":
            if dial_val == 0:
                dial_val += 100
            dial_val -= rotation
        else:
            dial_val += rotation

        # leftover rotations
        if dial_val <= 0 or dial_val >= 100:
            res += 1
        
        dial_val %= 100
            

    print(res)

if __name__ == "__main__":
    part2()