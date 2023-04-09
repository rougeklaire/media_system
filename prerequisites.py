import subprocess

prerequisites = ["tkinter", "tkvideo", "customtkinter"]

for i in prerequisites:
    try:
        subprocess.call(f"pip install {i}")
        print(f"package --{i}-- installed successsfully")
    except Exception as e:
        print(e)
