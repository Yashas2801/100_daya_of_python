# Day 5: PyPassword Generator 🔐  

Welcome to the **PyPassword Generator**! This project generates a secure and randomized password based on user-defined preferences for the number of letters, numbers, and symbols. It's perfect for creating strong passwords for your accounts.  

## Features  
- Customize the length of your password by choosing:  
  - Number of **letters**  
  - Number of **symbols**  
  - Number of **numbers**  
- Randomized password generation for enhanced security.  
- Ensures the password includes a mix of characters for better protection.  

## How It Works  
1. The program starts by asking the user how many letters, symbols, and numbers they would like in their password.  
2. It randomly selects characters from predefined lists of letters, numbers, and symbols.  
3. The selected characters are shuffled to create a randomized password.  
4. The generated password is displayed along with its length.  

## Code Highlights  
- **Random Selection**: The `random.choice()` method is used to select characters randomly.  
- **Shuffling**: The `random.shuffle()` method ensures the password is randomized.  
- **Dynamic Input**: The password adjusts dynamically based on user input.  

## Example Output  
```plaintext
Welcome to the PyPassword Generator!  
How many letters would you like in your password?  
5  
How many symbols would you like?  
3  
How many numbers would you like?  
2  

Your final randomized password is !a#5F2g$J  
The length of your final password is 10  

