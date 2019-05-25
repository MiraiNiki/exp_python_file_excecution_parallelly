# coding: UTF-8
import csv
from multiprocessing import Pool, cpu_count
import random

random.seed(1)
input_data = [[] for i in range(4)]#[[random.randint(0,100) for i in range(100)] for j in range(4)]
output_data = []

with open("test_input.csv", "r") as input:
    count = 0
    reader = csv.reader(input)
    header = next(reader)
    for row in reader:
        input_data[count % 4].append({"fuga":row[0]})
        count = count + 1

input_file = ["input_1.csv", "input_2.csv", "input_3.csv", "input_4.csv"]
print(input_data[0][0].keys())


def create_input_f(fname, index):
    with open(fname, "w") as file:
        writer = csv.DictWriter(file, input_data[index][0].keys())
        writer.writeheader()
        writer.writerows(input_data[index])  # list（1次元配列）の場合

for i in range(len(input_file)):
    create_input_f(input_file[i], i)


output_file = ["output_rw1.csv", "output_rw2.csv", "output_rw3.csv", "output_rw4.csv"]

print(len(input_data))

def create_files(index, input_file, output_file) :
    print(index)
    with open(input_file,"r") as input, open(output_file, "w") as file:
        cf_reader = csv.reader(input)
        next(cf_reader)
        output_d = []
        for row in cf_reader:
            output_d.append({"hoge":row})

        writer = csv.DictWriter(file, output_d[0].keys())
        writer.writeheader()
        writer.writerows(output_d)  # list（1次元配列）の場合


c = cpu_count()
pool = Pool(c)
l = [p.get() for p in [pool.apply_async(create_files, args=(i, input_file[i], output_file[i]))
                       for i in range(len(input_data))]]
pool.close()
print(len(l))

