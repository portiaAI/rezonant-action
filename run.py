import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--coding-agent", required=True)
parser.add_argument("--task", required=True)
parser.add_argument("--extra-args", default="{}")
args = parser.parse_args()

openai_api_key = os.getenv("OPENAI_API_KEY")
extra = json.loads(args.extra_args)

print("=== Hello from run.py ===")
print(f"coding_agent = {args.coding_agent}")
print(f"task         = {args.task}")
print(f"extra        = {extra}")
print(f"OPENAI_API_KEY set? {'yes' if bool(openai_api_key) else 'no'}")

# --- Working directory info ---
print("\n--- Working Directory Info ---")
print("Current working dir:", os.getcwd())
print("Contents:")
for entry in os.listdir("."):
    path = os.path.join(".", entry)
    if os.path.isdir(path):
        print(f"  [DIR]  {entry}")
    else:
        print(f"  [FILE] {entry}")

# If you also want the absolute path for clarity
print("\nAbsolute path:", os.path.abspath("."))

# TODO: call your actual code here instead of print
