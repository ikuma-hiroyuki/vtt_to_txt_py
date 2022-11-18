import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--from", type=str, help="変換対象ファイルが格納されているディレクトリ")
parser.add_argument("-t", "--to", type=str, help="変換後ファイルの保存先")

base_dir = Path(__file__).absolute().parent
vtt_dir = base_dir / "vttfiles"
text_dir = base_dir / "textfiles"

vtt_list = vtt_dir.glob("**/*.vtt")

for vtt in vtt_list:
    with open(vtt, "r", encoding="utf-8") as f:
        data = f.readlines()

        lst = []
        flag = False
        for row in data:
            if flag:
                lst.append(row)
                flag = False
            if "-->" in row:
                flag = True

    new_name = vtt.parent.name / Path(vtt).with_name(vtt.parent.name + "_" + vtt.stem + ".txt")
    to_path = text_dir / new_name.name

    with open(to_path, "w", encoding="utf-8") as f:
        f.writelines(lst)
