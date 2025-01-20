#! python3
import argparse
import time

from aoc import run_day, download_day, template_day

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run an Advent of Code day')
    parser.add_argument('-y', '--year', type=int)
    parser.add_argument('-d', '--day', type=int)
    parser.add_argument('-p', '--part', type=int)
    parser.add_argument('-s', '--sample', action='store_true')
    parser.add_argument('--download', action='store_true')
    parser.add_argument('--template', action='store_true')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if args.download:
        download_day(args.year, args.day)
    if args.template:
        template_day(args.year, args.day)
    if not args.download and not args.template:
        start_time = time.perf_counter_ns()
        run_day(args.year, args.day, args.part, args.sample, *args.args)
        end_time = time.perf_counter_ns()
        elapsed_nanoseconds = end_time-start_time
        elapsed = f"{elapsed_nanoseconds} ns"
        if elapsed_nanoseconds / 1000 > 1:
            elapsed = f"{elapsed_nanoseconds/1000:.1f}µs"
        if elapsed_nanoseconds / 1000000 > 1:
            elapsed = f"{elapsed_nanoseconds/1000000:.1f}ms"
        if elapsed_nanoseconds / 1000000000 > 1:
            elapsed = f"{elapsed_nanoseconds / 1000000000:.1f}s"
        print(f"Solved in {elapsed}")
