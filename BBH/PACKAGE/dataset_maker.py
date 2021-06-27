import csv, random

with open('runs_dataset1.data', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'o'])
    for i in range(1000):
        lst = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
        writer.writerow([lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], lst[7], 1 if (lst.count(1) >= 8) or (lst[2] == 1 and lst[5] == 1 and lst[7] == 1) or (lst.count(1) <= 2) else 0])