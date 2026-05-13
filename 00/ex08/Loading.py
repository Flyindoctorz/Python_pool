import os


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    termin_width = os.get_terminal_size().columns
    for i, elem in enumerate(lst):
        percent = i / total * 100
        size = len(f"{percent:.0f}%|") + len(f"| {total}/{total}") + 3
        toolbar_width = termin_width - size
        i += 1
        filled = int(percent * toolbar_width / 100)
        tofill = toolbar_width - filled
        bar = "[" + "=" * filled + ">" + " " * tofill + "]"
        print(f"{percent:.0f}%|{bar}| {i}/{total}", end="\r", flush=True)
        yield elem
