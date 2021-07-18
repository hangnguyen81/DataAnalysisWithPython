import sys
 
def file_count(filename):
    lines=0
    words=0
    chars=0
    with open(filename) as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    return (lines, words, chars)
 
def main():
    for filename in sys.argv[1:]:
        lines, words, chars = file_count(filename)
        print(f"{lines}\t{words}\t{chars}\t{filename}")
 
if __name__ == "__main__":
    main()