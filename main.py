from bull_shit_bingo import io
from bull_shit_bingo import bingo_table


def main():
    prompts = io.read_json("christmess_prompts_2023")

    RUNS = 5
    for run_index in range(RUNS):
        table = bingo_table.generate_bingo_table(prompts)
        io.write_to_latex(table)
        output_file = f"output_{run_index}"
        io.running_latex("bull_shit_bingo.tex", output_file=output_file)


if __name__ == "__main__":
    main()
