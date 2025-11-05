import pytest
import hashlib
from program import read_hashes, read_passwords, check_matches, crack_passwords, main

def test_read_hashes(tmp_path):
    hash_file = tmp_path / "hashes.txt"
    hash_file.write_text("abc123\nxyz789\n")
    result = read_hashes(hash_file)
    assert result == ["abc123", "xyz789"]

def test_read_passwords(tmp_path):
    wordlist = tmp_path / "words.txt"
    wordlist.write_text("apple\nbanana\n")
    result = read_passwords(wordlist)
    assert result == ["apple", "banana"]

def test_check_matches(capsys):
    words = ["hello", "password123"]
    hashes = [hashlib.md5("password123".encode()).hexdigest()]
    check_matches(words, hashes)
    captured = capsys.readouterr()
    assert "Match found! password123" in captured.out

def test_crack_passwords(tmp_path, capsys):
    wordlist_file = tmp_path / "wordlist.txt"
    wordlist_file.write_text("test\n1234\npassword\n")
    hash_file = tmp_path / "hashes.txt"
    hash_file.write_text(hashlib.md5("password".encode()).hexdigest() + "\n")
    crack_passwords(hash_file, wordlist_file)
    captured = capsys.readouterr()
    assert "Match found! password" in captured.out