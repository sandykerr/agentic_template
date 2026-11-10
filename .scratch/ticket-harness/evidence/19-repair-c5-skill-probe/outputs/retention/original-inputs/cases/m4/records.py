def parse_csv(text):
    return tuple(tuple(line.split(",")) for line in text.splitlines())
