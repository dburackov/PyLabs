import functions
import constants

if __name__ == "__main__":
    with open("text.txt", "r") as textfile:
        text: str = textfile.read()

    if not functions.check_input_text(text):
        raise Exception("Invalid input text")

    k: int = constants.K
    n: int = constants.N
    if input("Do u want input K and N values? [Y/N]") == "Y":
        k = int(input("Enter K: "))
        n = int(input("Enter N: "))

    functions.solve(text, k, n)
