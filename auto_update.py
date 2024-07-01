import os



def add_and_commit(file_name, problem_name):
    os.system(f"git add {file_name}")
    os.system(f'git commit -m "Add solution for LeetCode problem: {problem_name}"')


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    problem_name = input("Enter the problem name: ")
    add_and_commit(file_name, problem_name)
    os.system("git push origin master")