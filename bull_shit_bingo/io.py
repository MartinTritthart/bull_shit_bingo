import pandas as pd
import json
import subprocess

# pandas table formate


def read_json(prompt: str, file_path: str = "input/prompts.json") -> list:
    with open(file_path, "r") as f:
        data = json.load(f)
    return data.get(prompt, [])


def write_to_latex(df, saving_path: str = "output/table.tex"):
    latex_table = df.to_latex(index=False, escape=False, header=False)
    with open(saving_path, "w") as file:
        file.write(latex_table)

    print("Latex table saved")


def running_latex(file_path: str):
    try:
        subprocess.run(["pdflatex", file_path], check=True)
        print("PDF generated")
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")
