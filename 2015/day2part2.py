
with open('inputday2part1.txt', 'r') as i:
    c = i.read()

if __name__ == '__main__':
    # print(c[0:16])
    s = c.split('\n')
    length = 0
    for r in s[:-1]:
        # print(r)
        try:
            l, b, h = r.split('x')
        except Exception as e:
            print(e)
        length = length + 2 * min(int(l) + int(b), int(l) + int(h), int(b) + int(h)) + (int(l) * int(b) * int(h))
        # print(r.split('x'), area)
    print(length)