import os
import random
import time
import argparse

def open_program(program):
    try:
        os.system(f"start {program}")
    except Exception as e:
        print(f"Error opening program: {e}")

def main(programs, num_programs, delay_seconds, random_selection):
    for _ in range(num_programs):
        if random_selection:
            program = random.choice(programs)
        else:
            program = programs[0] if programs else None

        if program:
            open_program(program)
        else:
            print("No programs to open.")

        time.sleep(delay_seconds)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Repeatedly open programs.")
    parser.add_argument("programs", nargs="+", help="Program names to open")
    parser.add_argument("-n", "--num-programs", type=int, default=50, help="Number of times to open the programs")
    parser.add_argument("-d", "--delay-seconds", type=float, default=5, help="Delay in seconds between program launches")
    parser.add_argument("-r", "--random-selection", action="store_true", help="Randomly select programs")
    args = parser.parse_args()

    main(args.programs, args.num_programs, args.delay_seconds, args.random_selection)
