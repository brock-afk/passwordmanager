from argparse import Namespace
from .parser import create_parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    match args:
        case Namespace(command="vault", subcommand="create"):
            print("Creating vault")
        case Namespace(command="vault", subcommand="delete"):
            print("Deleting vault")
        case Namespace(command="vault", subcommand="list"):
            print("Listing vaults")
        case Namespace(command="vault", subcommand="open"):
            print("Opening vault")
        case _:
            parser.print_help()

    print(args)
