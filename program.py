import hashlib
import sys

def read_hashes(hash_file_path):
    with open(hash_file_path, "r") as h_file:
        hashes = [line.strip() for line in h_file.readlines()]
    return hashes
def read_passwords(wordlist_path):
    with open (wordlist_path, "r") as w_file:
        words = [line.strip() for line in w_file.readlines()]
    return words
def check_matches(words, hashes):
    for word in words:
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        if hashed_word in hashes:
            print(f"Match found! {word} --> {hashed_word}")
def crack_passwords(hash_file_path, wordlist_path):
    hashes = read_hashes(hash_file_path)
    words = read_passwords(wordlist_path)
    check_matches(words, hashes)

def main():
    hash_file = input("Enter path to hash file: ").strip()
    wordlist_file = input("Enter path of wordlist file: ")

    print("\nCracking passwords... Please wait\n")
    crack_passwords(hash_file, wordlist_file)
    print("\nDone!")

if __name__ == "__main__":
    main()
