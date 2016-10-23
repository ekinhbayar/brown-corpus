#!/usr/bin/env python2
import datetime
from collections import defaultdict
import sys

input_file_name = sys.argv[1]

with open(input_file_name, "rb") as input_file:
    raw_data = input_file.read().split("\n")

parsed_data = defaultdict(list)

for line in raw_data:
    word, tag = line.split(" ")
    if not word.isdigit():
        if not tag in parsed_data[word]:
            parsed_data[word].append(tag)

now = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
output_file_name = "output-%s.txt" % now

with open(output_file_name, "a") as output_file:
    for word in parsed_data.keys():
        output_file.write("%s %s\n" % (word, " ".join(parsed_data[word])))

print("%s is ready. %d lines cleaned." % (output_file_name, len(raw_data) - len(parsed_data)))