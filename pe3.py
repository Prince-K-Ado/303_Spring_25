import datetime
import string
def encode(input_text, shift):
    # Create a list of all lowercase letters (the first item in the returned tuple)
    alphabet = list(string.ascii_lowercase)
    
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

        # Validate the creation date is not in the future
        if creation_date > datetime.date.today():
            raise Exception("Account creation date cannot be in the future.")

        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print(f"Negative deposits are not allowed({amount}). Current balance: {self.balance}")
        else:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        # Base BankAccount has no specific restrictions aside from showing new balance
        self.balance -= amount
        print(f"Withdrawal successful. New balance: {self.balance}")

    def view_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        # 1) Check account age (must be at least 180 days old)
        age_in_days = (datetime.date.today() - self.creation_date).days
        if age_in_days < 180:
            print("Cannot withdraw until the account has been active for at least 180 days.")
            return

        # 2) Check overdraft (no negative balances allowed)
        if amount > self.balance:
            print("Insufficient funds. Overdrafts are not permitted.")
            return

        # If checks pass, proceed with withdrawal
        super().withdraw(amount)

class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        # Use the base withdraw logic
        super().withdraw(amount)
        # If balance goes negative, apply a $30 overdraft fee
        if self.balance < 0:
            self.balance -= 30
            print(f"Overdraft fee incurred. New balance: {self.balance}")