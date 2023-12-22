from bull_shit_bingo import io
from bull_shit_bingo import bingo_table


def main():
    a = io.read_json("christmess_prompts_2023")
    print(a)
    table = bingo_table.generate_bingo_table(a)
    print(table)
    io.write_to_latex(table)


if __name__ == "__main__":
    main()
