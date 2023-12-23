import json
import os
import subprocess


def read_json(prompt: str, file_path: str = "input/prompts.json") -> list:
    with open(file_path) as f:
        data = json.load(f)
    return data.get(prompt, [])


def write_to_latex(df, saving_path: str = "output/table.tex"):
    with open(saving_path, "w") as f:
        f.write("\\begin{table}[h]\n")
        f.write("\\begin{tabularx}{\\linewidth}{|" + "|".join(["X"] * len(df.columns)) + "|}\n")
        f.write("\\hline\n")

        # Write data rows
        for index, row in df.iterrows():
            f.write(" & ".join(map(str, row.values)) + " \\\\ \\hline\n")

        f.write("\\end{tabularx}\n")
        f.write("\\end{table}\n")

    print("Latex table saved")


def running_latex(file_path: str, output_file: str):
    try:
        output_file = f"{output_file}"
        clear_latex_helpers()
        subprocess.run(["pdflatex", "-jobname", output_file, file_path], check=True)
        print("PDF generated")
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")


def clear_latex_helpers(directory: str = "."):
    aux_file_extensions = [
        ".aux",
        ".fdb_latexmk",
        ".fls",
        ".log",
        ".synctex.gz",
    ]

    for output_file in os.listdir(directory):
        if output_file.endswith(tuple(aux_file_extensions)):
            os.remove(os.path.join(directory, output_file))


def clear_output_pdf(directory: str = "."):
    output_file_extensions = [".pdf"]
    for output_file in os.listdir(directory):
        if output_file.endswith(tuple(output_file_extensions)):
            os.remove(os.path.join(directory, output_file))
