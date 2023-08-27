import os
import json
import traceback
from src.config import REPLAY_ROOT
from typing import Tuple, Dict
from tqdm import tqdm


def read_file(filename) -> bytes:
    contents = None
    with open(f"{REPLAY_ROOT}/{filename}", "rb") as f:
        contents = f.read()
    return contents

def get_chunks(contents):
    header = contents[:12]
    body = contents[12:]
    chunk_len = int.from_bytes(header[8:12], byteorder="little")
    #print(chunk_len)
    first_chunk = json.loads(body[:chunk_len])
    #print(first_chunk.keys())
    # remove first chunk
    # print(len(body))
    body = body[chunk_len:]
    # print(len(body))
    second_chunk_len = int.from_bytes(body[:4], byteorder="little")
    body = body[4:]
    try:
        #print(second_chunk_len)
        second_chunk = json.loads(body[:second_chunk_len])
        body = body[second_chunk_len:]
        return first_chunk, second_chunk, body
    except Exception as e:
        #traceback.print_exc(e)
        return first_chunk, 0, body

def main():
    files = os.listdir(REPLAY_ROOT)
    for file in files:
        content = read_file(file)
        first, second, data = get_chunks(content)
        if second == 0:
            # replay is incomplete
            continue
        # replay is complete and can bne processed
        # first contains information at the start of the game and second contains the postgame results
        print(data[:10])




if __name__ == "__main__":
    main()
