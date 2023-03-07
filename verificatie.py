import difflib
import subprocess
import time


def verify(solution, input, output, subpath=""):
    solution = subpath + solution
    input = subpath + input
    output = subpath + output

    start_time = time.time()
    test = subprocess.run(['python3', solution], stdin=open(input), stdout=subprocess.PIPE, text=True)
    diff_time = time.time() - start_time
    with open(output) as file_2:
        output_text = file_2.readlines()
    output_text[-1] += '\n'  # missing the last newline in all my outputs somehow

    diffs = difflib.unified_diff(output_text, test.stdout.splitlines(True), fromfile=output, tofile=input, lineterm='')

    success = True
    for line in diffs:
        success = False
        print(repr(line))  # prevent escape chars from working

    if success:
        print(f"{input} matched {output} \n 🚀 SUCCESS 👍 🚀")
    print(f"took {diff_time:.2f}s ")


if __name__ == '__main__':
    verify("doodlopend.py", "wedstrijd.invoer", "wedstrijd.uitvoer", "./doodlopend/")
    verify("groen.py", "wedstrijd.invoer", "wedstrijd.uitvoer", "./groen/")
    verify("korting.py", "wedstrijd.invoer", "wedstrijd.uitvoer", "./korting/")
