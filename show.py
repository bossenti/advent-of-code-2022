import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    with open(f"day{os.getenv('day')}/input.txt") as f:
        print(f.read())
