import sys
import os
import re
import io
from contextlib import redirect_stdout

def replace_exec_with_print(code):
    pattern = re.compile(r'\bexec\s*\((.*?)\)', re.DOTALL)
    replaced_code = pattern.sub(r'print(\1)', code)
    return replaced_code

def run_and_capture(code):
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            exec(code, {})
        except Exception as e:
            print(f"[!] Error during execution: {e}")
    return f.getvalue()

def main():
    if len(sys.argv) != 2:
        print("Usage: python s3cret-deobfuscator.py <target_script.py>")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}")
        sys.exit(1)

    with open(input_path, 'r', encoding='utf-8') as f:
        original_code = f.read()

    modified_code = replace_exec_with_print(original_code)

    # Run the modified code and capture output
    output = run_and_capture(modified_code)

    # Save output to file
    quoted_output_path = os.path.splitext(input_path)[0] + "-deobf.txt"
    with open(quoted_output_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"[+] Execution output saved to: {quoted_output_path}")

if __name__ == "__main__":
    main()
#if you want skid this code, idc about credits
