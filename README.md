# HW21 – Python Binary Search

## Task Definition

The goal of this homework is to extend the classical binary search algorithm and adapt it to support two additional behaviors while maintaining **O(log N)** time complexity:

1. **Return the index of the first occurrence**  
   If the searched value appears multiple times in the list, the function must return the index of its **first appearance**, not just any matching index.  
   This requires modifying the usual binary search logic to continue scanning the left half of the list even after a match is found.

    **Example:**

    ```py
    numbers = [20, 20, 20, 20, 20]
    bSearchSortedList(numbers, 20)
    # → 0
    ```

2. **Return encoded negative insertion index when no match is found**  
   If the value does not exist in the list, the function must return a negative number of the form:  
   -`(insertion_index + 1)`  
   where `insertion_index` is the place where the number should be inserted to maintain the list’s sorted order.

    **Example:**

    ```py
    numbers = [20, 30, 40, 50, 60]
    bSearchSortedList(numbers, 45)
    # → -4   # insertion index = 3 → -(3 + 1)
    ```

This behavior mimics the Java `Arrays.binarySearch` API and is useful in many real-world cases such as maintaining sorted collections, implementing indexable trees, or designing efficient lookup tables.

---

## 📝 Description

This project implements an enhanced version of the binary search algorithm in Python.  
Binary search is a fundamental algorithm used to find the position of a target value within a **sorted list** by repeatedly splitting the search interval in half.

The improved version implemented here supports:

-   **Accurate first-occurrence search**
-   **Encoded insertion-point calculation**
-   **Handling of edge cases**
-   **Strict O(log N) time complexity**
-   **Clear typing and documentation**

This assignment also includes a comprehensive set of automatic test cases to validate correctness for a wide range of input scenarios.

---

## 🎯 Purpose

The main objectives of the homework are:

### 📌 Algorithmic Understanding

To deepen your understanding of efficient search algorithms and the importance of logarithmic time performance in large datasets.

### 📌 Handling Duplicate Values

Classic binary search does not guarantee locating the _first_ occurrence of a duplicated value.  
You will learn how to adjust the mid-point logic to ensure that the leftmost instance is returned without resorting to linear scanning.

### 📌 Insertion Index Encoding

A powerful extension used in popular libraries: returning a negative insertion index when the value is not present.  
This allows callers to use the function for both searching **and** constructing sorted lists efficiently.

### 📌 Strengthening Python Skills

The exercise reinforces:

-   Static typing (`List[int]`)
-   Clean function design
-   Writing meaningful docstrings
-   Designing and running automated tests
-   Handling edge cases (empty list, single-element list, boundaries)

---

## 🔍 How It Works

The algorithm follows these steps:

### 1. Initialize boundaries

`left = 0`  
`right = len(lst) - 1`

### 2. Continue searching while the interval is valid

```
while left <= right:
    middle = (left + right) // 2
```

### 3. Compare middle with the target

-   If a match is found:
    -   Check if this is the first occurrence  
        If the previous value is smaller or we're at index `0`, return it
    -   Otherwise continue searching to the left (`right = middle - 1`)
-   If the target is smaller → search left half
-   If the target is larger → search right half

### 4. If not found

The `left` pointer ends at the **correct insertion index**.  
Return the encoded value:

```
return -(left + 1)
```

### 5. Time complexity

At every step we divide the search interval by half.  
This guarantees:

**O(log N)** time  
**O(1)** memory

---

## 📜 Output Example

### ✔ When the number is found

```py
[1, 5, 20, 20, 20, 30]
num = 20
→ 2      # first occurrence
```

### ❌ When the number is not found

```py
[10, 20, 30]
num = 5
→ -1     # insertion at index 0
```

```py
[10, 20, 30]
num = 40
→ -4     # insertion at index 3
```

### ✔ Empty list

```py
[]
num = 10
→ -1     # insertion at index 0
```

---

## 📦 Usage

### Importing and using the function

```py
from binary_search import b_search_sorted_list

numbers = [1, 5, 20, 20, 20, 30]
print(b_search_sorted_list(numbers, 20))
# 2
```

### Running tests

A set of 10 tests is included to ensure:

-   Correct first-occurrence detection
-   Correct insertion-index encoding
-   Proper edge-case handling

To run tests:

```bash
python binary_search.py
```

Expected output:

```
TEST 1 PASSED
TEST 2 PASSED
...
TEST 10 PASSED
```

---

## ✅ Dependencies

This project uses only Python’s standard library.

-   Python **3.10+**
-   No external packages required
-   Uses `typing.List` for type annotations

---

## 📊 Project Status

**Status:** ✔ Completed  
All tests pass, and the algorithm complies fully with the requirements.

This implementation is production-ready and can be integrated into any Python project that needs a fast and reliable search mechanism.

---

## 📄 License

MIT License

---

## 🧮 Conclusion

This project demonstrates how a classical algorithm like binary search can be expanded to support real-world use cases such as handling duplicates and calculating insertion points efficiently.  
By accounting for edge cases and maintaining O(log N) performance, this solution represents a robust and scalable approach suitable for educational, academic, and practical software development contexts.

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
