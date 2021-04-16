import argparse

parser = argparse.ArgumentParser(description="Edit frame counts to be correctly formatted.")
parser.add_argument('input', metavar='I', type=str, help="Your input path.")
args = parser.parse_args()

f = open(args.input, "r")
flist = f.read().splitlines()
x = "1"
for index, i in enumerate(flist):
    inum = i.split(' ')
    inum[0] = str(x)
    flist[index] = ' '.join(inum)
    x = int(x) + 1
fstr = '\n'.join(flist)
g = open(args.input, "w")
g.seek(0)
g.write(fstr)
g.truncate()