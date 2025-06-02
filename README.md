# PRODIGY_CS_01
# Caesar Cipher 🔐

A simple Python implementation of the classic Caesar Cipher encryption technique.

## 📖 What is Caesar Cipher?

The Caesar Cipher is one of the oldest known encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. For example, with a shift of 3:

- A → D  
- B → E  
- C → F  
- ...  
- X → A  
- Y → B  
- Z → C

Non-alphabet characters (like punctuation or numbers) remain unchanged.

## 🛠️ Features

- Encrypt any message using a shift key
- Decrypt a message with the correct shift key
- Supports both uppercase and lowercase letters
- Ignores and preserves non-letter characters (e.g., spaces, punctuation)

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Running the Script

```bash
EXAMPLE
Enter message: Hello World!
Enter shift (number): 3
Encrypt or Decrypt? (e/d): e
Encrypted: Khoor Zruog!
python caesar_cipher.py
