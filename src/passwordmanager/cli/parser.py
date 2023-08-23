import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Password Manager CLI")

    commands = parser.add_subparsers(title="Commands")

    vault_parser = commands.add_parser("vault", help="Manage vaults")
    vault_parser.add_argument("action", action="store_const", const="create")

    return parser
