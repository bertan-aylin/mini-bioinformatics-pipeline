import csv
import sys


def mean_quality(quality_string):
    scores = [ord(char) - 33 for char in quality_string.strip()]
    return sum(scores) / len(scores) if scores else 0


def gc_content(sequence):
    sequence = sequence.strip().upper()
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100 if sequence else 0


def process_fastq(input_fastq, output_csv):
    with open(input_fastq, "r") as infile, open(output_csv, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["read_id", "read_length", "gc_content", "mean_quality"])

        while True:
            header = infile.readline().strip()
            if not header:
                break

            sequence = infile.readline().strip()
            plus = infile.readline().strip()
            quality = infile.readline().strip()

            read_id = header[1:] if header.startswith("@") else header
            read_length = len(sequence)
            gc = gc_content(sequence)
            mean_q = mean_quality(quality)

            writer.writerow([read_id, read_length, round(gc, 2), round(mean_q, 2)])


if __name__ == "__main__":
    input_fastq = sys.argv[1]
    output_csv = sys.argv[2]
    process_fastq(input_fastq, output_csv)