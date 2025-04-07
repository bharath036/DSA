#To check a number is prime or not

def is_prime(num):  #--> O(N),O(1)
    for i in range(2,num):
        print(i)
        if num%i == 0:
            return f"Not a prime number"
    return f"IS prime"

num = 11
print(is_prime(num))

'''
## **Understanding Loop Behavior Without `else` in Python**

### **Code Example Without `else`**
```python
class Solution:
    def isPrime(self, N):
        for i in range(2, N):  # Iterates from 2 to N-1
            if N % i == 0:  # If a divisor is found, return False
                return False
        return True  # Executes only if the loop completes fully
```

### **Why Does This Work Without `else`?**
- If `N` is divisible by any number in `[2, N-1]`, the function **immediately returns `False`**.
- If no divisor is found, the loop ends, and the function **returns `True`**.
- The function doesn’t need an `else` block because the `return True` **only executes if the loop completes normally**.

---

### **Using `else` with a Loop**
Python allows an `else` statement after a loop, which executes **only if the loop finishes without hitting `break` or an early `return`**.

#### **Example Using `else`**
```python
class Solution:
    def isPrime(self, N):
        for i in range(2, N):
            if N % i == 0:
                return False  # Exits immediately if a divisor is found
        else:
            return True  # Runs only if the loop completes fully
```

### **When to Use `else` After a Loop?**
- **Use `else` for clarity** when additional logic depends on the loop **completing successfully**.
- **Omit `else` when `return` naturally handles the flow**, reducing indentation and making the code simpler.

#### **Example Where `else` is Useful:**
```python
def find_first_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num  # Exits immediately if an even number is found
    else:
        return None  # Runs only if no even number was found
```

---

### **Key Takeaways**
1. **Both versions work**, but using `else` improves readability when needed.
2. **Omitting `else` saves indentation** and simplifies logic when no further actions are needed.
3. **Python’s loop `else` runs only if the loop doesn’t exit early**, making it useful for cases where checking a condition at the end matters.

🚀 **Use `else` in loops when it makes the code more readable, but it's not always necessary!**


'''