import argparse
import os
import os.path
from typing import Tuple

# Solution creator: REN
# Self-restriction:
# - Only material from week 0 until functions and lists
# - No regex (its allowed, though)
# - Minimize side effects as much as possible


def get_args():
    """Parses args and returns related values"""
    parser = argparse.ArgumentParser(exit_on_error=False)

    # Ensure only either of them are picked, or none.
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-w", action=argparse.BooleanOptionalAction)
    group.add_argument("-i", action=argparse.BooleanOptionalAction)

    parser.add_argument("pattern")
    parser.add_argument("path")

    args = parser.parse_args()

    whole_word: bool = args.w
    case_insensitive: bool = args.i
    path: str = args.path
    pattern: str = args.pattern

    if pattern.count("*") > 1:
        raise ValueError("Multiple wildcard")

    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found.")

    uses_wildcard = pattern.count("*") == 1
    return whole_word, case_insensitive, path, pattern, uses_wildcard


def match_wildcard(line: str, pattern: str) -> Tuple[bool, int, int]:
    """Check if line matches pattern with wildcard

    The start index points the FIRST character of the match, whereas
    the end index points the LAST character of the match

    Args:
        line (str): Line to check
        pattern (str): Pattern to match

    Returns:
        Tuple[bool, int, int]: Tuple of whether match is found,
            its start index, and end index
    """
    # Assumption: whitespace is matched by wildcard
    # Essentially, we search for Te*xt by finding "Te" first, then see
    # if "xt" appears later on.
    first, second = pattern.split("*")

    first_idx = line.find(first)
    rest_idx = first_idx + len(first)

    # If second is empty ("X*") just match until the end of line
    if second == "":
        second_idx = len(line)
    else:
        second_idx = line[rest_idx:].find(second)

        # Only fix the index to relative if found
        if second_idx != -1:
            second_idx = rest_idx + line[rest_idx:].find(second)

    if first_idx <= second_idx and first_idx != -1:
        return True, first_idx, second_idx + len(second) - 1

    return False, -1, -1


def match_word(line: str, pattern: str, uses_wildcard: bool) -> bool:
    """Find if line matches pattern whole word

    Args:
        line (str): Line to check
        pattern (str): Pattern to match
        uses_wildcard (bool): Whether pattern uses wildcard

    Returns:
        bool: Whether line matches pattern
    """
    if uses_wildcard:
        found, start_idx, end_idx = match_wildcard(line, pattern)
        # Set end pointer to AFTER last character
        end_idx += 1
        if not found:
            return False
    else:
        start_idx = line.find(pattern)
        if start_idx == -1:
            return False

        end_idx = start_idx + len(pattern)

    # We match at each end of string OR we are surrounded by spaces
    #
    # How:
    # - Check if we are at the start of string OR previous is whitespace
    # - Check if we are at the end of string OR
    #   the character AFTER the match pattern is a whitespace
    if (start_idx == 0 or line[start_idx - 1].isspace()) and (
        end_idx == len(line) or line[end_idx].isspace()
    ):
        return True

    return False


def match_pattern(line: str, pattern: str, uses_wildcard: bool) -> bool:
    """Check whether a substring of line matches pattern

    This will check via wildcard if pattern contains wildcard

    Args:
        line (str): Line to check
        pattern (str): Pattern to match
        uses_wildcard (bool): Whether pattern uses wildcard

    Returns:
        bool: Whether line matches or not
    """
    if uses_wildcard:
        return match_wildcard(line, pattern)[0]
    else:
        return pattern in line


def process_file(
    path: str,
    pattern: str,
    case_insensitive: bool,
    whole_word: bool,
    uses_wildcard: bool,
):
    """Process a file to check all matching lines

    Args:
        path (str): Path to file
        pattern (str): Pattern to match
        case_insensitive (bool): Whether case insensitive is enabled
        whole_word (bool): Whether whole word flag is enabled
        uses_wildcard (bool): Whether pattern uses wildcard
    """
    with open(path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        # Strip whitespaces around line
        line = line.strip()
        if case_insensitive:
            # Lower if case insensitive to match case with pattern
            processing_line = line.lower()
        else:
            processing_line = line

        valid = False
        if whole_word:
            valid = match_word(processing_line, pattern, uses_wildcard)
        else:
            valid = match_pattern(processing_line, pattern, uses_wildcard)

        if valid:
            print(f"{path:40} line {i + 1:<3} {line[:40].strip()}")


def process_folder(
    path: str,
    pattern: str,
    case_insensitive: bool,
    whole_word: bool,
    uses_wildcard: bool,
):
    """Recursively find all text files and prints all matching files
    and its matched line.

    Args:
        path (str): Path to folder
        pattern (str): Pattern to match
        case_insensitive (bool): Whether case insensitive is enabled
        whole_word (bool): Whether whole word flag is enabled
        uses_wildcard (bool): Whether pattern uses wildcard
    """
    # Assume all files are text files in the directory
    for (dirpath, _, fnames) in os.walk(path):
        for fname in fnames:
            new_path = os.path.join(dirpath, fname)
            process_file(
                new_path,
                pattern,
                case_insensitive,
                whole_word,
                uses_wildcard,
            )


if __name__ == "__main__":
    try:
        whole_word, case_insensitive, path, pattern, uses_wildcard = get_args()
    except ValueError:
        print("Argumen program tidak benar.")
        quit()
    except argparse.ArgumentError:
        print("Argumen program tidak benar.")
        quit()
    except FileNotFoundError as e:
        print(str(e))
        quit()

    # Lowercase if case insensitive to match case with line
    # (it'll be lowered too)
    if case_insensitive:
        pattern = pattern.lower()

    if os.path.isdir(path):
        process_folder(
            path,
            pattern,
            case_insensitive,
            whole_word,
            uses_wildcard,
        )
    else:
        process_file(
            path,
            pattern,
            case_insensitive,
            whole_word,
            uses_wildcard,
        )
