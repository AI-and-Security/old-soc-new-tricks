import pandas as pd

print("Testing....")
if pd.__version__ == "2.3.1":
    print("Your environment works!")
else:
    print("Trouble with environment, enjoy debugging and holler for help when needed!")
