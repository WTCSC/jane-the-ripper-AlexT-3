[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/d_w3ds2H)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21362188)

## Jane the Ripper
### Alexandria Tuell
> This program is a password cracker that reads a file of MD5 hashes and a word list and finds plaintext password matches for as many of the hashes as possible.

### Requirements:
* Python3
* Pytest (for running tests)

### Testing:
This program includes several test functons that make sure the program can read the list of hashes and passwords, as well as looking for matches between the two lists. All of these functions ultimately help the program crack as many passwords as possible.
When running `pytest`, this is the expected output:
```
=================================================================================================== test session starts ====================================================================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/tuella@CSGP.EDU/Projects/jane-the-ripper-AlexT-3
collected 4 items                                                                                                                                                                                                                    

test_program.py ....                                                                                                                                                                                                 [100%]

==================================================================================================== 4 passed in 0.02s =====================================================================================================
```

### Installation and startup:
1. In the terminal, clone the repository using `https://github.com/WTCSC/jane-the-ripper-AlexT-3.git`
2. Navigate to the project directory with `cd jane-the-ripper-AlexT-3/`
3. Start the program using the command `python3 program.py`

### Program usage:
The program already comes with a file for the hashes, labeled `hashes.txt` and a password file, labeled `wordlist.txt`. When prompted for the path to the hash and wordlist file, you can use the files given in this program, or you can import your own. 
```
Enter path to hash file: hashes.txt
Enter path of wordlist file: wordlist.txt

Cracking passwords... Please wait

Match found! abc123 --> e99a18c428cb38d5f260853678922e03
Match found! master --> eb0a191797624dd3a48fa681d3061212
Match found! 654321 --> c33367701511b4f6020ec61ded352059
Match found! welcome --> 40be4e59b9a2a2b5dffb918c0e86b3d7
Match found! matrix --> 21b72c0b7adc5c7b4a50ffcb90d92dd6
Match found! charlie --> bf779e0933a882808585d19455cd7937
Match found! edward --> a53f3929621dba1306f8a61588f52f55
Match found! angel --> f4f068e71e0d87bf0ad51e6214ab84e9
Match found! daniel --> aa47f8215c6f30a0dcdb2a36a9f4168e
Match found! samsung --> fe546279a62683de8ca334b673420696

Done!
```