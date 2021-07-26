import hashlib
import time
import random
from stdiomask import getpass
from termcolor import colored
from os import system, name
from prettytable import PrettyTable


def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # others
    else:
        _ = system('clear')


# sample encryption function showing condensed usage of SHA 256 encryption algorythm
def sha_256_encrypt(my_string):
    # encode() function used rather than update() function for lower-level string conversion to the byte-stream
    encoded_string = my_string.encode()

    # sha256() constructor selected to create SHA-256 hash object
    encrypted_string = hashlib.sha256(encoded_string)

    # hexdigest() function used rather than digest() function to assure safe hash transfer via non-binary environments
    safe_sha256 = encrypted_string.hexdigest()

    return safe_sha256


block_id = 1
timestamp = 0
hashblock_previous = ""
hashblock_current = ""
transactions = ""


# block producing function for building new hash from: 3 provided parameters and hostorical hash of previous block
def produce_block(blockid, prev_hash, trx):
    global hashblock_previous

    cur_timestamp = int(time.time())
    current_hash = sha_256_encrypt(repr(blockid) + repr(cur_timestamp) + prev_hash + trx)
    block_table = PrettyTable(['Block ID', 'Timestamp', 'Current Hash', 'Previous Hash', 'Transactions'])
    block_table.add_row([blockid, cur_timestamp, current_hash, prev_hash, trx])
    print(block_table)

    # store current hash for future use
    hashblock_previous = current_hash


def random_sender():
    senders = ['Perry', 'Thomas', 'Otto', 'Kim', 'Raul', 'Jessica']
    return random.choice(senders)


def random_receiver():
    receivers = ['Paolo', 'Veronique', 'Felix', 'Victor', 'Marlin']
    return random.choice(receivers)


def random_amount():
    return random.choice(range(1, 1082))


# Use Cases
# ---------
clear()


'''
# 1. String encoding
print("\nUse Case 1: Input encryption")
string_sample = input("Input text for SHA 256 encryption: ")
encrypted_input = sha_256_encrypt(string_sample)
print("Encrypted input: " + encrypted_input + "\n")
'''


'''
# 2. Password validation
print("\nUse Case 2: Password validation")
# a] Set original password and return digest from hash function
original_password = getpass(prompt="\nInput original password: ", mask="*")
encrypted_orig_pass = sha_256_encrypt(original_password)


# b] Set check password and return digest from hash function
check_password = getpass(prompt="Input check password: ", mask="*")
encrypted_check_pass = sha_256_encrypt(check_password)

# c] Display hashes
time.sleep(1)
print("\nPassword 1 hash: " + encrypted_orig_pass)
print("Password 2 hash: " + encrypted_check_pass)

# d] Compare hashes and return success/fail
time.sleep(1)
print(colored("\nSuccess: Original and Check passwords are identical.\n", "green")) if encrypted_orig_pass == encrypted_check_pass else print(colored("\nFail: Original and Check passwords are different.\n", "red"))
'''

'''
# 3. Simplified block-chain
print("\nUse Case 3: Simplified blockchain")
# Prerequisites:
# - demonstratively used only SHA-256 (real application contains of multiple algorythms with nested hashing, e.g. bitcoin)
# - each block contains encrypted data, resp. there are no transaction-less blocks
# - hashes of previous blocks are being chained with new blocks with exception of the genesis block

# a] filter wrong values for desired blocks to be minted
try:
    desired_blocks = int(input("Enter desired amount of blocks to be minted (int): "))
    assert desired_blocks > 0

except:
    print(colored("Fail: Entered value isn't a positive integer\n", "red"))

# b] loop thru blocks production
while block_id <= desired_blocks:
    transactions = "From: " + random_sender() + ", To: " + random_receiver() + ", Amount: " + repr(random_amount()) + ", Currency: ADA"
    produce_block(blockid=block_id, prev_hash=hashblock_previous, trx=transactions)

    # iterate block id & sleep
    block_id += 1
    time.sleep(1)
'''
