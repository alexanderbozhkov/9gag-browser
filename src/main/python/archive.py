# Read the .txt file and extract the meme urls


def get_all_memes(meme_file, meme_list: list):
    with open(meme_file, 'r') as f:
        for line in f:
            if line.startswith('http'):
                meme_list.append(line.strip())
