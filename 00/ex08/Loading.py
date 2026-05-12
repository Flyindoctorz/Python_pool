import os


def ft_tqdm(lst: range) -> None:
    termin_width = os.get_terminal_size().columns
    for i, elem in enumerate(lst):
        i += 1
        total = len(lst)
        percent = i / total *100
        yield elem
