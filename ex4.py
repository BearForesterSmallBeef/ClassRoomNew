import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, required=True)
parser.add_argument("-up", "--up_case", action="store_true",
                    help="convert name to upper register")
parser.add_argument(
    "--number", choices=[i for i in range(10, 100)], type=int, default=0,
    help="select number", required=True)
parser.add_argument("--no-name", action="store_const", const="no",
                    dest="name")
args = parser.parse_args()

name = args.name
if (args.up_case):
    name = name.upper()

print(f"The name is {name}. And the number = {args.number}")


