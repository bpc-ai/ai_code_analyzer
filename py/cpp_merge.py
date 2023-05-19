import os
import sys
import glob


def is_file_local(file_name, source_dir):
    splits = file_name.split(".")
    if len(splits) > 1:
        ext = splits[1].strip()
        for f in glob.glob(f"{source_dir}/**/*.{ext}", recursive=True):
            if os.path.basename(f) == file_name:
                return f
        return None
    else:
        return None


def combine(file_path, source_dir):
    with open(file_path, "r") as fd:
        lines = fd.readlines()
    final_lines = list()
    for i, line in enumerate(lines):
        if "#include" in line:
            incl_file = line.split(" ")[1].strip()[1:-1]
            incl_file_path = is_file_local(incl_file, source_dir)
            if incl_file_path:
                ret_lines = combine(incl_file_path, source_dir)
                final_lines.insert(i, ret_lines)
            else:
                final_lines.append(line)
        else:
            final_lines.append(line)
    return final_lines


def merge(fd, comb_lines):
    for comb_sub_lines in comb_lines:
        if isinstance(comb_sub_lines, list):
            merge(fd, comb_sub_lines)
        else:
            fd.writelines(comb_sub_lines)
    return fd


if __name__ == "__main__":
    entry_file = sys.argv[1]
    src_dir = os.path.dirname(entry_file)
    merge_file = f"{src_dir}/combined.cpp"
    combined_lines = combine(entry_file, src_dir)
    with open(merge_file, "a") as fp:
        merge(fp, combined_lines)
    print("c")
