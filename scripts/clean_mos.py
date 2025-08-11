import os

def sort_by_video_name(lines):
    # Sort function for filenames like "1-14.mp4"
    def extract_sort_key(line):
        video_name = line.split(",")[0]
        base_name = video_name.replace(".mp4", "")
        parts = base_name.split("-")
        return tuple(map(int, parts))

    return sorted(lines, key=extract_sort_key)

def clean_mos_data(header_file, data_file, output_file):
    # Read header (first line only)
    with open(header_file, "r") as f:
        header_line = f.readline().strip()

    # Read data (excluding any empty lines)
    with open(data_file, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    sorted_lines = sort_by_video_name(lines)

    # Write header + sorted lines to output file
    with open(output_file, "w") as f:
        f.write(header_line + "\n")
        for line in sorted_lines:
            f.write(line + "\n")

    print(f"Cleaned file saved to {output_file}")

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dataset', 'original'))
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dataset', 'cleaned'))

    header_file = os.path.join(base_dir, 'MOS-descriptions.txt')
    data_file = os.path.join(base_dir, 'MOS.txt')

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'cleaned-mos.csv')
    
    clean_mos_data(header_file, data_file, output_file)
