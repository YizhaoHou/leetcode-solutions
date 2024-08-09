import os
import sys
sys.path.append('Math')
sys.path.append('DP')
sys.path.append("Tree_and_Graph")
sys.path.append('Array')



def add_and_commit(Question_name):
    file_name = os.path.abspath(Question_name  + '.py')
    os.system(f"git add {file_name}")
    os.system(f'git commit -m "Add solution for LeetCode problem: {Question_name}"')


if __name__ == "__main__":
    Question_name = input("Enter the Question_name: ")
    Question_name = os.path.abspath(Question_name)
    add_and_commit(Question_name)
    os.system("git push origin master")
