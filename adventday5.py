
myfile = open("adventday5input.txt", mode='r')

jumps = [int(x) for x in myfile.readlines()]

cursor = 0
count = 0
steps = 0
#print(jumps)

while cursor < len(jumps):
    #print("Cursor position {} has the value {}.".format(cursor,jumps[cursor]))
    old_cursor = cursor
    cursor += jumps[cursor]
    jumps[old_cursor] += 1
    steps += abs(jumps[old_cursor])
    count += 1

#print(jumps)
print(len(jumps))
print("It took {} iterations and {} steps to leave the maze.".format(count, steps))
