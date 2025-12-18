import os


def ft_tqdm(lst: range) -> None:

    total = len(lst)
    columns = os.get_terminal_size().columns
    bar_size = columns - 43

    for i, elem in enumerate(lst, start=1):
        progress = int(i / total * 100)
        filled = int(bar_size * i / total)

        bar = "=" * filled + ">" + " " * (bar_size - filled)
        print(f"\r{progress:3d}%|[{bar}]| {i}/{total}", end="", flush=True)

        yield elem

    print()
