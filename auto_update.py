import os
import sys
sys.path.append('Math')
sys.path.append('DP')
sys.path.append("Tree_and_Graph")
sys.path.append('Array')



def add_and_commit(file_name):
    os.system(f"git add {file_name}")
    os.system(f'git commit -m "Add solution for LeetCode problem: {file_name}"')


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    file_name = os.path.abspath(file_name)
    add_and_commit(file_name)
    os.system("git push origin master")
