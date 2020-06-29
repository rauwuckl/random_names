


def clean_text(input_file):
    path = "{}.txt".format(input_file)
    with open(path, 'r') as f:
        lines = f.readlines()
    unique = set([l.strip() for l in lines])

    sorted_unique = sorted(list(unique))

    out_path = "{}_clean.txt".format(input_file)
    with open(out_path, 'w') as f:
        f.write("\n".join(sorted_unique))


if __name__ == "__main__":
    clean_text("adj_character_raw")