import datetime
def encode(input_text, shift):
    # Create a list of all lowercase letters (the first item in the returned tuple)
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
    encoded_chars = []
    
    for ch in input_text:
        if ch.isalpha():
            # Convert the character to lowercase (as per your examples)
            lower_char = ch.lower()
            
            # Determine its alphabet index
            old_index = ord(lower_char) - ord('a')
            
            # Shift and wrap around (using modulo 26)
            new_index = (old_index + shift) % 26
            
            # Convert back to a character
            new_char = chr(new_index + ord('a'))
            
            encoded_chars.append(new_char)
        else:
            # Non-alphabetical characters remain unchanged
            encoded_chars.append(ch)

    # The second item in the returned tuple is the encoded text
    encoded_text = "".join(encoded_chars)
    
    return (alphabet, encoded_text)

def decode(input_text, shift):
    decoded_chars = []

    for ch in input_text:
        # Check if the character is alphabetical
        if ch.isalpha():
            # Convert to lowercase for consistent decryption
            lower_char = ch.lower()

            # Find its alphabetical index (0 for 'a', 1 for 'b', etc.)
            old_index = ord(lower_char) - ord('a')

            # Shift backward by 'shift', wrapping around using modulo 26
            new_index = (old_index - shift) % 26

            # Convert index back to a character
            new_char = chr(new_index + ord('a'))

            decoded_chars.append(new_char)
        else:
            # Non-alphabetical characters remain unchanged
            decoded_chars.append(ch)

    # Join the list of characters into a string
    return "".join(decoded_chars)

class BankAccount:
    def __init__(self, 
                 name="Rainy", 
                 ID="1234", 
                 creation_date=None, 
                 balance=0):
        # If no creation_date is provided, set it to today's date
        if creation_date is None:
            creation_date = datetime.date.today()

        # Verify that creation_date is not in the future
        if creation_date > datetime.date.today():
            raise Exception("Account creation date cannot be in the future.")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        # Negative deposit amounts are not allowed
        if amount < 0:
            raise Exception("Deposit amount cannot be negative.")
        
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

    def view_balance(self):
        return self.balance
