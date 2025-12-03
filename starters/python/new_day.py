#!/usr/bin/env python3

"""Script to create a new day's directory and template files for daily tasks"""

import sys
import shutil
import os
from pathlib import Path

def main():
    # Check if a day number was provided
    if len(sys.argv) != 2:
        print("Usage: python new_day.py <day_number>")
        print("Example: python new_day.py 4")
        sys.exit(1)
    
    try:
        day_num = str(sys.argv[1])
    except ValueError:
        print("Error: Day number must be an integer")
        sys.exit(1)
    
    script_dir = Path(__file__).parent.resolve()
    source_dir = script_dir / "day00"
    dest_dir = script_dir / f"day{day_num}"
    
    # Copy the day00 directory
    shutil.copytree(source_dir, dest_dir)
    
    # Rename all files in the new directory (replace 00 with the padded day number)
    print("Renaming files...")
    for file_path in dest_dir.iterdir():
        if "00" in file_path.name:
            new_name = file_path.name.replace("00", day_num)
            new_path = file_path.parent / new_name
            file_path.rename(new_path)
            print(f"  Renamed: {file_path.name} -> {new_name}")
    
    print("Updating file contents...")
    for file_path in dest_dir.iterdir():
        if file_path.is_file():
            try:
                content = file_path.read_text()
                updated_content = content.replace("00", day_num)
                file_path.write_text(updated_content)
                print(f"  Updated: {file_path.name}")
            except Exception as e:
                print(f"  Warning: Could not update {file_path.name}: {e}")
    
    print(f"Successfully created day{day_num}!")
    print(f"Location: {dest_dir}")

if __name__ == "__main__":
    main()
