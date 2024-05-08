# Task 1: Posterior Proabilites

To run the optimized Python program, you'll need to follow a few simple steps to set up your environment and execute the script. Here’s a step-by-step guide:

### Prerequisites
Ensure you have Python (3.11 or later) installed on your computer. You can verify this by running the following command in your terminal or command prompt:

```bash
python3 --version
```

If Python is not installed, you can download and install it from [python.org](https://www.python.org/downloads/).

### Save the Script
1. **Create a Python file:** Open a text editor of your choice, paste the provided Python script, and save the file with a `.py` extension, for example, `compute_a_posteriori.py`.

### Prepare the Input
The script expects a command-line argument representing a sequence of candies where:
- `C` or `c` stands for cherry.
- `L` or `l` stands for lime.

### Run the Program
Open a terminal or command prompt, navigate to the directory where your script is saved, and run the script by providing a sequence of candies as an argument. Here’s how you can do it:

- **On Windows:**
  ```bash
  python compute_a_posteriori.py CLCCLL
  ```

- **On MacOS or Linux:**
  ```bash
  python3 compute_a_posteriori.py CLCCLL
  ```

Replace `CLCCLL` with the sequence of your choice. The program will process the sequence and save the output in a file named `result.txt` in the same directory.

### View the Output
After running the script, you can open the `result.txt` file to see the output. It will contain the probabilities calculated for each step in the sequence, as well as the final probabilities of picking a cherry or lime candy next.

### Troubleshooting
If you encounter errors:
- Ensure the sequence only contains the letters `C` or `L` (either uppercase or lowercase).
- Check that you are using the correct Python command (`python` or `python3`) based on your operating system and Python installation.
- Make sure you're in the correct directory where your Python file is located.

By following these steps, you should be able to successfully run and use the program.

---

# Task 2: Bayesian Networks

To run the `bnet.py` program, follow these steps:

1. **Save the Script**: Ensure the Python script (`bnet.py`) is saved on your machine.
2. **Open Terminal or Command Prompt**: Navigate to the directory where you saved `bnet.py`.
3. **Run the Program**: Use the following command structure in your terminal or command prompt:

   ```bash
   python3 bnet.py [arguments]
   ```

   Replace `[arguments]` with the specific parameters you want to test. For example:

   - To calculate the probability of `B=false, A=true, M=true`:
     ```
     python3 bnet.py Bf At Mt
     ```
   - To calculate the conditional probability of `J=true` given `E=true, B=false`:
     ```
     python3 bnet.py Jt given Et Bf
     ```

Each argument should consist of two letters: the first indicating the variable (`B`, `E`, `A`, `J`, `M`), and the second indicating the truth value (`t` for true, `f` for false). Use `given` to separate the evidence from the query in conditional probabilities.
