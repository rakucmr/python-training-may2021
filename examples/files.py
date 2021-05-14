def grep(filename, text):
    with open(filename) as f:
        return [line.strip() for line in f if text in line]
