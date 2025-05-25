import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
main_file_path = os.path.join(current_dir, "..", "src")

sys.path.append(main_file_path)

def test_execute_operation():
    pass