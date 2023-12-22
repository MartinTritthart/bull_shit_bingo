from bull_shit_bingo import io
from bull_shit_bingo import bingo_table


def main():
    prompts = io.read_json("christmess_prompts_2023")
    table = bingo_table.generate_bingo_table(prompts)
    io.write_to_latex(table)
    io.running_latex("bull_shit_bingo.tex", runs=5)


if __name__ == "__main__":
    main()
