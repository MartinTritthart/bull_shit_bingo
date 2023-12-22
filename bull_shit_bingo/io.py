import pandas as pd
import json


def read_json(promt: str, file_path: str = "input/prompts.json") -> list:
    with open(file_path, "r") as f:
        data = json.load(f)
    return data.get(promt, [])


def write_to_latex(df, saving_path: str = "output/table.tex"):
    latex_table = df.to_latex()
    with open(saving_path, "w") as file:
        file.write(latex_table)

    print("Latex table saved")
