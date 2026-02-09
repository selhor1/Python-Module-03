import sys


def main() -> None:
    print("=== Command Quest ===\n")

    program_name = sys.argv[0]
    total_args = len(sys.argv)

    if total_args == 1:
        print("No arguments provided!")
        print("Program name:", program_name)
        print("Total arguments:", total_args)
    else:
        print("Program name:", program_name)
        print("Arguments received:", total_args - 1)

        i = 1
        while i < total_args:
            print("Argument", i, ":", sys.argv[i])
            i += 1

        print("Total arguments:", total_args)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Caught unexpected error: {e}")
