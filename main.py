from bull_shit_bingo import bingo_table, io


def main():
    prompts = io.read_json("christmess_prompts_2023")

    RUNS = 1
    for run_index in range(RUNS):
        table = bingo_table.generate_bingo_table(prompts)
        io.write_to_latex(table)
        output_file = f"output_{run_index}"
        io.running_latex("bull_shit_bingo.tex", output_file=output_file)


if __name__ == "__main__":
    main()
    # io.clear_output_pdf()
