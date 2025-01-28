#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Exclude the program name
    num_args = len(argv)

    if num_args == 0:
        print(f"{num_args} arguments.")
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
