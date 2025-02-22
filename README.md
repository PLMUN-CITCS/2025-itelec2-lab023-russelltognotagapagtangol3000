# 2025-ITELEC2-LAB023
Week 05 - Working with Functions

Laboratory # 23 - Group Activity # 01 - Problem 05: Word Counter in a Sentence with Input and Counting Functions

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 23 - Group Activity # 01 - Problem 05: Word Counter in a Sentence with Input and Counting Functions**

   **Objective:**
   This challenge focuses on string manipulation and function design. You will practice:
   - Creating functions for specific tasks (input and word counting).
   - Using the split() method for string manipulation.
   - Handling user input.
   - Returning values from functions and using them in the main program.

   **Desired Output:**
   ```bash
   Enter a sentence: This is a sample sentence.
   The sentence has 5 words.
   
   Enter a sentence:  Hello world!  
   The sentence has 2 words.
   ```
   
   **Notable Observations:**
   - Function Decomposition: The program is divided into two functions: get_sentence_input for handling user input and count_words for counting words. This promotes modularity and code organization.
   - String Manipulation: The count_words function uses the split() method to split the sentence into a list of words based on spaces. This is a common technique for working with words in a sentence.

   **Python Best Practices**
   - Meaningful Function and Variable Names: Use descriptive names that clearly indicate the purpose of functions and variables (e.g., get_sentence_input, count_words, sentence).
   - Docstrings: Include docstrings for each function to explain its purpose, parameters, and return value.
   - Type Hints (Optional but Recommended): Use type hints to specify the expected data types for function parameters and return values.
   - Input Handling: The get_sentence_input function directly returns the user's input, allowing for any type of sentence, including those with punctuation and extra spaces.
   - Test Thoroughly: Test your program with various sentences, including sentences with different lengths, punctuation, and leading/trailing spaces to ensure it works correctly in all cases.

   **Challenge Requirements:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `word_counter_functions.py`
      
   2. get_sentence_input() Function:
      - Purpose: Obtains a sentence input from the user.
      - No parameters.
      - Prompts the user to enter a sentence.
      - Reads and returns the user's input as a string.
      
   3. count_words(sentence) Function:
      - Purpose: Counts the number of words in a given sentence.
      - Takes one parameter: sentence (string).
      - Uses the split() method to split the sentence into a list of words based on spaces.
      - Returns the number of words in the sentence (the length of the list of words).

   4. Main Program Flow:
      - Calls get_sentence_input() to get the sentence from the user.
      - Calls count_words(), passing the returned sentence as an argument.
      - Displays the word count to the user in a user-friendly format (e.g., "The sentence has 5 words.").

   **Conclusion**
   This challenge helps you practice creating functions to handle input and perform string manipulation. You learn how to use the split() method to break a sentence into words and count them. By decomposing the problem into functions, you create more modular and reusable code. This approach also makes your code easier to understand and maintain.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 05 - Laboratory # 23"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
