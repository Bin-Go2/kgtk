"""
Remove columns from a file.
"""


import sys


def parser():
    return {
        'help': 'Remove columns from a file '
    }


def add_arguments(parser):
    """
    Parse arguments
    Args:
        parser (argparse.ArgumentParser)
    """
    parser.add_argument('-dt', "--datatype", action="store", type=str, dest="datatype",
                        help="Datatype of the input file, e.g., tsv or csv.", default="tsv")
    parser.add_argument('-c', "--columns", action="store", type=str, dest="columns",
                        help="Columns to remove as a comma-separated string, e.g., id,docid")
    parser.add_argument('input', nargs='?', action='store')


def run(datatype, columns, input): 
    # import modules locally
    import sh

    if input:
        sh.mlr('--tsv', 'cut', '-x', '-f', columns, input, _out=sys.stdout, _err=sys.stderr)
    elif not sys.stdin.isatty():
        print('reading from stdin')
        # print(sh.cat(_in=sys.stdin))
        print(sh.mlr('--tsv', 'cut', '-x', '-f', columns,
                     _in=sys.stdin, _out=sys.stdout, _err=sys.stderr))
    else:
        parser.print_help()

