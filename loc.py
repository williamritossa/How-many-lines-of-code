#!/usr/bin/env python3

import os

def count_lines_in_swift_files(directory):
    total_lines = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".swift"):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        total_lines += sum(1 for _ in f)
                except Exception as e:
                    print(f"Could not read {full_path}: {e}")
    return total_lines

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    grand_total = 0
    
    for entry in sorted(os.listdir(script_dir)):
        path = os.path.join(script_dir, entry)
        
        if os.path.isdir(path) and not entry.startswith('.'):
            lines = count_lines_in_swift_files(path)
            print(f"{entry}: {lines}")            
            grand_total += lines
    
    print(f"\nGrand Total (all subfolders): {grand_total}")

if __name__ == "__main__":
    main()
