import sys
from pathlib import Path
from colorama import Fore, Style, init


init(autoreset=True)


def show_directory_structure(path: Path, indent: str = ""):
    for item in path.iterdir():
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
            show_directory_structure(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")


def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Error: Please provide a directory path.{Style.RESET_ALL}")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Error: This path does not exist.{Style.RESET_ALL}")
        return

    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: This path is not a directory.{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}📦 {directory_path.name}{Style.RESET_ALL}")
    show_directory_structure(directory_path)


if __name__ == "__main__":
    main()