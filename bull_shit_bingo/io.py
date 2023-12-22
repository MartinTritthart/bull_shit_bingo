import json
import subprocess


def read_json(prompt: str, file_path: str = "input/prompts.json") -> list:
    with open(file_path, "r") as f:
        data = json.load(f)
    return data.get(prompt, [])


def write_to_latex(df, saving_path: str = "output/table.tex"):
    with open(saving_path, "w") as f:
        f.write("\\begin{table}[h]\n")
        f.write(
            "\\begin{tabularx}{\linewidth}{|"
            + "|".join(["X"] * len(df.columns))
            + "|}\n"
        )
        f.write("\\hline\n")

        # Write data rows
        for index, row in df.iterrows():
            f.write(" & ".join(map(str, row.values)) + " \\\\ \\hline\n")

        f.write("\\end{tabularx}\n")
        f.write("\\end{table}\n")

    print("Latex table saved")


def running_latex(file_path: str):
    try:
        subprocess.run(["pdflatex", file_path], check=True)
        print("PDF generated")
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")
