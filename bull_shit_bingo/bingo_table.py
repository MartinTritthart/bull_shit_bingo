import numpy as np
import random
import pandas as pd


def generate_bingo_table(prompts: list):
    prompts = prompts.copy()
    if np.sqrt(len(prompts)) % 1 != 0:
        raise ValueError("The number of prompts must be a square number")
    else:
        rows = int(np.sqrt(len(prompts)))
        cols = rows
        random.shuffle(prompts)
        bingo_table = np.array(prompts).reshape(rows, cols)
        df = pd.DataFrame(bingo_table)
        return df
