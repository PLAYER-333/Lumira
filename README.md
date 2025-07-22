# Lumira
# 🌟 Lumira v0.1 — Beginner-Friendly Programming Language

> 🎉 A language by dreamers, for dreamers.  
> Built by **Shaurya** with ChatGPT — fully vibe-coded, from scratch.

---

## 🔥 What is Lumira?

**Lumira** is a simple, beginner-focused, interpreted programming language designed for learning, fun, and lightweight development.  
It is:
- Fast to read like **Python**
- Simple to write like **HTML**
- Custom, creative, and vibe-based like **you**

Lumira is currently written in Python and runs `.lm` files using a custom interpreter.

---

## ✅ Features of Lumira v0.1

| Feature | Description |
|--------|-------------|
| `printos()` | Prints to the screen (like `print` in other languages) |
| `inscan()` | Takes user input and auto-detects type (int, float, or string) |
| `let` | Declares variables |
| `defn` | Declares functions (basic support) |
| `~!` | Comment syntax |
| Type Detection | No need to specify type for strings, just declare |
| Type Conversion | Built-in functions like `toint()`, `tofloat()`, `tostr()`, `datatype()` |
| Conditional Statements | Use `check:` and `elsecheck:` for `if-else` logic |
| `.lm` | Custom file extension for Lumira scripts |

---

## 🧠 Syntax Guide (v0.1)

```lm
~! This is a comment

let name = "Lumira"
printos("Hello,", name)  ~! also works with +

let age = inscan("Enter your age: ")

check: age >= 18
    printos("You are eligible!")
elsecheck:
    printos("You are not eligible.")

let val = "123"
let number = toint(val)
let pi = tofloat("3.14")
printos(datatype(pi))  ~! prints: float
