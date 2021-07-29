from pathlib import Path
import argparse


def find_files(way, pattern):
    p = Path(way)
    return p.glob(pattern)


def rename_server_name(way, pattern, parameter_name, old_value, new_value):
    files = find_files(way, pattern)
    for f in files:
        with open(f, 'r') as conf:
            rows = conf.readlines()

        for i, row in enumerate(rows):
            if parameter_name in row and old_value in row:
                rows[i] = row.replace(old_value, new_value)

        with open(f, 'w') as conf:
            conf.writelines(rows)


parser = argparse.ArgumentParser()
parser.add_argument('way', help='input path to conf file')
parser.add_argument('pattern', help='input pattern for searching conf files')
parser.add_argument('parameter_name', help='input parameter name you want to change')
parser.add_argument('old_value', help='input value you need to change')
parser.add_argument('new_value', help='input new value')

args = parser.parse_args()


rename_server_name(args.way, args.pattern,args.parameter_name, args.old_value, args.new_value)
