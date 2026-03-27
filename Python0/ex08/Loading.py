import os


def ft_tqdm(lst: range) -> any:
    total = len(lst)
    for i, item in enumerate(lst):

        cols = os.get_terminal_size().columns
        bar_size = cols - 30
        progress = (i + 1) / total
        filled = int(bar_size * progress)
        bar = "=" * filled + ">" + " " * (bar_size - filled)
        output = f"\r{int(progress * 10)}%|[{bar}]| {i + 1}/{total}"
        os.write(1, output.encode())
        yield item
