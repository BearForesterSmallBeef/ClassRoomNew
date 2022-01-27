import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--count", action="store_true")
parser.add_argument("--num", action="store_true")
parser.add_argument("--sort", action="store_true")
parser.add_argument("file", type=str)

args = parser.parse_args()

file, count, num, sort = args.file, args.count, args.num, args.sort

try:
    with open(file, "r") as f:
        fi = f.readlines()
        if sort:
            sorted(fi)
        for i in range(len(fi)):
            if num:
                print(f"{i + 1} " + fi[i])
            else:
                print(fi[i])
        if count:
            print(len(fi))
        f.close()
except Exception:
    print(-8)