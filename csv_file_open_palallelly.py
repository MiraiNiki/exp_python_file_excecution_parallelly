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
        input_data[count % 4].append(row[0])
        count = count + 1

print(input_data[3])

# input_file = ["input_1.csv", "input_2.csv", "input_3.csv", "input_4.csv"]
output_file = ["output_1.csv", "output_2.csv", "output_3.csv", "output_4.csv"]

print(len(input_data))

def create_files(index, input_data, output_file) :
    print(index)
    with open(output_file, "w") as file:
        writer = csv.writer(file, lineterminator='\n')  # 改行コード（\n）を指定しておく
        writer.writerow(input_data)  # list（1次元配列）の場合


c = cpu_count()
pool = Pool(c)
l = [p.get() for p in [pool.apply_async(create_files, args=(i, input_data[i], output_file[i]))
                       for i in range(len(input_data))]]
pool.close()
print(len(l))

