import re
NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def find_all_occurences(substring, line):
    return [m.start() for m in re.finditer(f'(?={substring})', line)]

def sub_words_for_digits(line):
    # replace first word number and last word number only and then do the first part of the original solution
    l =  sorted([(key,v) for key in NUMBER_MAP.keys() if find_all_occurences(key,line) != [] for v in find_all_occurences(key, line)], key=lambda x: x[1])
    if l == []:
        return line, line
    return line.replace(l[0][0], str(NUMBER_MAP[l[0][0]])), line.replace(l[-1][0], str(NUMBER_MAP[l[-1][0]]))    

def solve(file):
    with open(file) as f:
        s = 0
        
        for l in f:
            s += int("".join([c for c in list(l) if c.isdigit()][0] + [c for c in reversed(list(l)) if c.isdigit()][0]))
    return s

def solve_2(file):
    with open(file) as f:
        s = 0
        for l in f:
            l = sub_words_for_digits(l)
            s += int("".join([c for c in l[0] if c.isdigit()][0] + [c for c in reversed(l[1]) if c.isdigit()][0]))
        return s

print(solve("inp_ex"))
print(solve("inp"))
print(solve_2("inp_ex2"))
print(solve_2("inp2"))