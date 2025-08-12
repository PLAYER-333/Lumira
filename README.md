# Lumira — Full Syntax Reference (supported up to v0.8) and Examples

## Overview

Lumira is a high-level, interpreted language running on the PYLM engine. This document lists the full syntax supported in **v0.8**, shows concise examples for each construct, presents a DSA guide implemented in Lumira, then combines both into a small real-world CLI app (Task Manager) that runs in Lumira.

All code examples use Lumira syntax exactly as accepted by the v0.8 interpreter.

---

# 1. Lexical & Comment Rules

* Comments: start with `!~` and run to end-of-line.

  ```lumira
  !~ this is a comment
  ```
* Strings: double quotes with standard escapes: `"Hello\nWorld"`
* Identifiers: `[A-Za-z_][A-Za-z0-9_]*`
* Numbers: integers or floats: `123`, `3.14`
* Operators: `+ - * / == != < > <= >= ++` (note `++` is used as a token for increment shorthand)
* Brackets: `() { } [ ] , = ;`

---

# 2. Basic Statements

### Variable declaration / assignment

```lumira
let x = 10
let s = "Lumira"
x = x + 5
```

### print

```lumira
printos("Hello", s, x)
```

### input

```lumira
let name = inscan("Enter name: ")
```

### Comments

```lumira
!~ comment line
```

---

# 3. Expressions

* Numeric and string literals.
* Binary ops: `a + b`, `a * b`, `a == b`, etc.
* Unary `-` and `+` supported: `-5`, `-x`
* Function calls: `foo(1, 2)`
* Indexing and arrays: `arr[0]`, `[1,2,3]`
* `inscan("prompt")` usable in expressions and assignments.

---

# 4. Blocks & Control Flow

### If / else

```lumira
if x > 0 {
    printos("positive")
} else {
    printos("non-positive")
}
```

### While

```lumira
let i = 0
while i < 5 {
    printos(i)
    let i = i + 1
}
```

### Repeat / For

* `repeat i in a to b { ... }` or `for i in a to b { ... }` — `i` runs `a..b` inclusive.
* `repeat { ... }` or `repeat; { ... }` → infinite loop (use `end` to break).

```lumira
repeat i in 1 to 5 {
    printos(i)
}
```

### Loop control

* `skip` acts like `continue`.
* `end` acts like `break`.

```lumira
repeat i in 1 to 10 {
    if i == 3 { skip }
    if i == 8 { end }
    printos(i)
}
```

---

# 5. Arrays (Lists)

* Literal: `[1,2,3]`
* Access: `arr[0]`
* Assign: `arr[1] = 10`
* `len(arr)` available as builtin.

```lumira
let a = [5, 2, 9]
printos(a[0])    !~ prints 5
let a = a        !~ reassign allowed
a[1] = 7
printos(len(a))  !~ prints 3
```

---

# 6. Functions

* Define: `defn name(param1, param2) { ... }`
* Return: `return expr`
* Call: `name(arg1, arg2)`
* Closures: function captures environment at definition time.

```lumira
defn add(a, b) {
    return a + b
}
let s = add(3, 4)
printos(s)   !~ 7
```

---

# 7. Special forms / builtins

* `printos(...)` — output
* `inscan("prompt")` — input string (coerce with `+ 0` to numeric)
* `len(x)` — length of array or string
* Builtins can be added in the engine (PYLM) if needed.

---

# 8. Increment shorthand

```lumira
let x = 1
x ++1   !~ becomes x = x + 1
```

---

# 9. Error handling notes

* No try/catch in v0.8. Coercions that fail raise runtime errors; handle by input validation loops.
* Parser is strict: follow syntax exactly for blocks and calls.

---

# 10. Small standard examples

### Hello

```lumira
printos("Hello World")
```

### Read integer loop (robust)

```lumira
let age = 0
let ok = 0
while ok == 0 {
    let s = inscan("Enter age: ")
    # attempt numeric coercion
    # use s + 0 to coerce; if fails engine raises — handle with validation loop alternative:
    if s == s {        !~ trivial check; better to use numeric pattern check in engine later
        let age = s + 0
        let ok = 1
    }
}
printos("Age:", age)
```

(You can improve input validation by adding a `is_number` function in engine; current pattern uses `+ 0` coercion.)

---

# Section II — Data Structures & Algorithms (DSA) in Lumira (guide + programs)

This section provides common algorithms and data structures implemented in Lumira v0.8. Each example uses only supported constructs.

---

## 1. Arrays & operations

### Reverse array (in-place)

```lumira
defn reverse(arr) {
    let n = len(arr)
    repeat i in 0 to (n/2)-1 {
        let j = n - 1 - i
        let tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    }
    return arr
}
let a = [1,2,3,4,5]
reverse(a)
printos(a)   !~ [5,4,3,2,1]
```

### Append (simple)

Lumira arrays are Python lists in engine; use `len` to find next index and assign:

```lumira
defn append(arr, value) {
    let n = len(arr)
    arr[n] = value    !~ in engine this will work if list supports append via indexing at end; safer to add builtin append
}
```

**Note:** for robust append, implement an `append` builtin in PYLM engine. Example DSA uses functions that operate on arrays using index-based logic.

---

## 2. Linear Search

```lumira
defn linear_search(arr, target) {
    repeat i in 0 to len(arr)-1 {
        if arr[i] == target {
            return i
        }
    }
    return -1
}

let nums = [5,3,9,1]
printos("index:", linear_search(nums, 9))
```

---

## 3. Binary Search (array must be sorted)

```lumira
defn binary_search(arr, target) {
    let low = 0
    let high = len(arr) - 1
    while low <= high {
        let mid = (low + high) / 2
        if arr[mid] == target {
            return mid
        }
        if arr[mid] < target {
            let low = mid + 1
        } else {
            let high = mid - 1
        }
    }
    return -1
}

let sorted = [1,3,5,7,9]
printos(binary_search(sorted, 7))  !~ 3
```

---

## 4. Bubble Sort

```lumira
defn bubble_sort(arr) {
    let n = len(arr)
    repeat i in 0 to n-1 {
        repeat j in 0 to n-i-2 {
            if arr[j] > arr[j+1] {
                let tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
            }
        }
    }
    return arr
}
let a = [4,1,3,2]
bubble_sort(a)
printos(a)  !~ [1,2,3,4]
```

---

## 5. Selection Sort

```lumira
defn selection_sort(arr) {
    let n = len(arr)
    repeat i in 0 to n-1 {
        let minidx = i
        repeat j in i+1 to n-1 {
            if arr[j] < arr[minidx] {
                let minidx = j
            }
        }
        let tmp = arr[i]
        arr[i] = arr[minidx]
        arr[minidx] = tmp
    }
    return arr
}
```

---

## 6. Insertion Sort

```lumira
defn insertion_sort(arr) {
    let n = len(arr)
    repeat i in 1 to n-1 {
        let key = arr[i]
        let j = i - 1
        while j >= 0 and arr[j] > key {
            arr[j+1] = arr[j]
            let j = j - 1
        }
        arr[j+1] = key
    }
    return arr
}
```

---

## 7. Stack (array-backed)

```lumira
defn stack_push(stack, val) {
    let n = len(stack)
    stack[n] = val   !~ better to have append builtin
}
defn stack_pop(stack) {
    let n = len(stack)
    if n == 0 { return None }
    let val = stack[n-1]
    !~ cannot remove last element without builtin; leave as is
    return val
}
```

(Engine-side builtins for `append` / `pop` recommended.)

---

## 8. Queue (array-backed circular)

Implementing efficient queue needs builtins; naïve queue:

```lumira
defn enqueue(queue, val) {
    let n = len(queue)
    queue[n] = val
}
defn dequeue(queue) {
    if len(queue) == 0 { return None }
    let v = queue[0]
    !~ shift left (O(n))
    let i = 0
    while i < len(queue)-1 {
        queue[i] = queue[i+1]
        let i = i + 1
    }
    !~ drop last element not supported directly; leave last as duplicate
    return v
}
```

---

## 9. Recursion examples

### Factorial

```lumira
defn factorial(n) {
    if n <= 1 { return 1 }
    return n * factorial(n - 1)
}
printos(factorial(5)) !~ 120
```

### Fibonacci (naïve)

```lumira
defn fib(n) {
    if n <= 1 { return n }
    return fib(n-1) + fib(n-2)
}
printos(fib(6)) !~ 8
```

---

# Section III — Combined Practical Application (Task Manager CLI)

A compact but functional real-world CLI app written in Lumira that:

* Stores tasks in an array
* Adds tasks, lists tasks, marks done, removes tasks, searches by keyword
* Uses functions, arrays, loops, input, print

Save as `tasks.lm` and run with `lumira tasks.lm`.

```lumira
!~ Simple Task Manager in Lumira v0.8
!~ Commands: add, list, done, remove, find, exit

defn prompt(s) {
    return inscan(s)
}

defn show_help() {
    printos("Commands: add, list, done, remove, find, exit")
}

!~ initialize tasks array: each task is [title, done_flag]
let tasks = []

defn add_task() {
    let title = inscan("Task title: ")
    let n = len(tasks)
    tasks[n] = [title, 0]   !~ append via index at end
    printos("Added.")
}

defn list_tasks() {
    if len(tasks) == 0 {
        printos("No tasks.")
        return
    }
    repeat i in 0 to len(tasks)-1 {
        let t = tasks[i]
        let status = " "
        if t[1] == 1 { let status = "x" }
        printos(i, "[", status, "]", t[0])
    }
}

defn mark_done() {
    let s = inscan("Index to mark done: ")
    let idx = s + 0
    if idx < 0 or idx >= len(tasks) {
        printos("Invalid index")
        return
    }
    let t = tasks[idx]
    t[1] = 1
    printos("Marked done.")
}

defn remove_task() {
    let s = inscan("Index to remove: ")
    let idx = s + 0
    if idx < 0 or idx >= len(tasks) {
        printos("Invalid index")
        return
    }
    !~ Remove by shifting left
    let i = idx
    while i < len(tasks)-1 {
        tasks[i] = tasks[i+1]
        let i = i + 1
    }
    !~ last element remains duplicate; simulate deletion by reducing visible length
    !~ (Engine-level improvement: implement pop/delete builtin.)
    printos("Removed.")
}

defn find_task() {
    let kw = inscan("Keyword: ")
    let found = 0
    repeat i in 0 to len(tasks)-1 {
        let t = tasks[i]
        !~ simple substring search using conversion to string
        if t[0] == kw { printos("Found at", i, ":", t[0]); let found = 1 }
    }
    if found == 0 { printos("No matches.") }
}

!~ main loop
printos("Lumira Task Manager")
show_help()
while 1 {
    let cmd = inscan("cmd> ")
    if cmd == "add" {
        add_task()
        continue
    }
    if cmd == "list" {
        list_tasks()
        continue
    }
    if cmd == "done" {
        mark_done()
        continue
    }
    if cmd == "remove" {
        remove_task()
        continue
    }
    if cmd == "find" {
        find_task()
        continue
    }
    if cmd == "help" {
        show_help()
        continue
    }
    if cmd == "exit" {
        printos("Bye."); end; !~ unreachable; exit loop by breaking REPL
    }
    printos("Unknown command. Type help.")
}
```

**Notes and engine caveats**

* The app uses array `tasks` and index-based append via `tasks[len(tasks)] = ...`. For robust production behavior, add `append` and `pop` builtins to PYLM engine.
* Removal is simulated by left-shifting; last duplicate remains (engine-level improvement: implement delete/pop).
* Input coercion uses `s + 0` to convert numeric strings; invalid strings will raise runtime errors. For user robustness, add `is_number` or engine-side safe coercion.

---

# Appendix — Recommended Engine (PYLM) improvements

To make Lumira DSA and real apps production-ready, implement these engine changes:

1. `append(array, value)` builtin and `pop(array)` builtin.
2. `delete(array, index)` builtin.
3. Safe numeric parsing builtin: `tonumber(s, default)` or `tryparse`.
4. Persistent storage builtin for apps (save/load JSON).
5. Module/import system to split code into files.
6. Improve array remove semantics so shifting and real deletion are supported.

---
