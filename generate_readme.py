import os
import sys
from collections import defaultdict

#dictionary to store paths in format: directoryPath -> allFilesInDirectory
paths = defaultdict(list)

#populate the paths dictionary
for dirname, dirnames, filenames in os.walk('.'):
    if 'algorithms' not in dirname:
        continue
    if 'pycache' in dirname:
        continue

    for filename in filenames:
        if '__init__' in filename:
            continue
        paths[dirname[1:]].append(os.path.join(dirname[1:], filename))

#generate count of ds and algo for readme
count_ds, count_algo = 0, 0
for values in paths.values():
    count_algo += len(values)
    for file in values:
        if 'implementation' in file:
            count_ds += 1
count_algo -= count_ds

#generate list of files in tree format for markdown
markdown = list()
for key, values in sorted(paths.items()):
    string = '*'
    directory_name = ''
    
    for i in reversed(range(len(key))):
        if key[i] == '/':
            break
        directory_name = key[i] + directory_name
    
    if directory_name == 'dp':
        directory_name = 'Dynamic Programming'
    elif directory_name == 'twopointers':
        directory_name = 'Two Pointers'
    elif directory_name == 'hashtables':
        directory_name = 'Hash Tables'
    elif directory_name == 'linkedlist':
        directory_name = 'Linked List'
    elif directory_name == 'bst':
        directory_name = 'Binary Search Tree'

    directory_name = '* [**' + directory_name.title() + '**]' + '(' + key + ')  '
    markdown.append(directory_name)

    files = []
    for file in values:
        file_name = ''
        for i in reversed(range(len(file))):
            if file[i] == '/':
                    break
            file_name = file[i] + file_name
        file_name = file_name[:len(file_name)-3]
        file_name = file_name.replace("_", " ")
        if 'implementation' in file_name:
            file_name = '    - [*' + file_name.title() + '*](' + file + ')  '
        else:
            file_name = '    - [' + file_name.title() + '](' + file + ')  '


        files.append(file_name)

    files.sort()
    position = 0
    for index, file in enumerate(files):
        if 'Implementation' in file:
            files[position], files[index] = files[index], files[position]
            position += 1
    for file in files:
        markdown.append(file)
    markdown.append('  ')
    



readme = '''
Data Structures and Algorithms
==============================
 
This repository contains my implementations of data structures and algorithms using Python 3. Most of the algorithm questions are taken from LeetCode. This is a work in progress.

## Install
You can use this as an API in your code as follows:

    $ pip3 install algorithms3

An example of running an algorithm:

```python3
#Check if a string containing brackets is valid or not

from algorithms.stack import is_valid

if __name__ == '__main__':
    test = is_valid('()[]')
    print(test)
```

If an algorithm is listed in this repository but is not in the pip package, it means that I have not uploaded the latest version. I will be doing that once a week. 

## Uninstall
If you want to uninstall, simply run:

    $pip3 uninstall algorithms3

## Tests
I have written basic tests for most of the modules. To run all the tests at once run:
    
    $python3 -m unittest discover tests

## Progress
**Data Structures** : {0}  
**Algorithms** &nbsp; &nbsp; &nbsp; &nbsp; : {1}

## List of Implementations


'''.format(count_ds, count_algo)

markdown.insert(0, readme)

with open('README.md', 'w') as f:
    for x in markdown:
        print(x, file=f)

