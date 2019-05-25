# coding: UTF-8
import csv
from multiprocessing import Pool, cpu_count
import random

count= 0
random.seed(1)
input_data = [[random.randint(0,100) for i in range(100)] for j in range(4)]
output_data = []

input_file = ["input_1.txt", "input_2.txt", "input_3.txt", "input_4.txt"]
output_file = ["output_1.txt", "output_2.txt", "output_3.txt", "output_4.txt"]

print(input_data)

def create_files(index, input_file, output_file) :
    print(index, input_data[index])
    with open(input_file, "r") as input, open(output_file, "w") as file:
            while (True):
                line = input.readline()
                if not line:
                    break
                file.write(line + "\n")

c = cpu_count()
pool = Pool(c)
l = [p.get() for p in [pool.apply_async(create_files, args=(i, input_file[i], output_file[i]))
                       for i in range(len(input_file))]]
pool.close()
print(len(l))

