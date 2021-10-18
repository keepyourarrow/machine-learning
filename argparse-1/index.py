# import the necessary packages
import argparse
# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser(description="This program greets you") # description = optional
parser.add_argument("-n", "--name", required=True, help="name of the user")
parser.add_argument("-fn", "--first-name", required=True, help="name of the user")
args = parser.parse_args()

print(args)
# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args.name))