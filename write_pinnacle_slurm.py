#! usr/bin/env python3

# print bash header 
print('#!/bin/bash')

print()

# print bash commands
print('#SBATCH --job-name=jdt')
print('#SBATCH --partition comp72')
print('#SBATCH --nodes=1')
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=32')
print('#SBATCH --time=72:00:00')
print('#SBATCH -o jdt_%j.out')
print('#SBATCH -e jdt_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=jdtalley@uark.edu')

print()

# purge all the modules
print('module purge')

print()

# cd into the submit directory

