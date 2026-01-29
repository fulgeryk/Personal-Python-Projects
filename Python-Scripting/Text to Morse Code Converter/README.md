# Text to Morse Code Converter

A simple text-based Python program that converts user input into Morse code.

This project was built as a personal exercise in designing a small but robust encoding system. The focus was not only on conversion, but on handling edge cases, defining clear rules, and building a predictable output format.

---

## How it works

The program follows a structured pipeline:

1. Get user input
2. Normalize input (convert to uppercase for consistency)
3. Define Morse dictionary
4. For each character:
   - check if valid
   - convert using dictionary
   - handle spaces as word separators
   - replace unknown characters with a placeholder
5. Build final Morse output string
6. Display result

---

## Conversion rules

- Letters A–Z and digits 0–9 are supported
- Words are separated using `/`
- Letters are separated by spaces
- Unknown characters are replaced with `?`
- Unknown characters are reported to the user

Example:

```
HELLO WORLD 🙂
```

Output:

```
.... . .-.. .-.. --- / .-- --- .-. .-.. -.. ?
```

---

## Project goal

This project focuses on:

- building a clean encoding pipeline
- handling invalid input safely
- defining a consistent internal protocol
- improving UX with clear feedback
- practicing structured program design

The goal is robustness, not complexity.
