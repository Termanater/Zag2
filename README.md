CHAPTERS 2 & 3 NOTES 
Strings and String Concatenation
A string is a sequence of characters (i.e. "Mary"), that can be stored in a variable.Strings need to be surrounded by ' ' or " ".
This function can be used to save repetitive keystrokes
Concantenation adds mulitpul strings together (without whitespaces)
Len() Is a built in function that counts characters 
Type() will tell you what type the input is (Variable, Integer, String)

Formatted string literals (f-strings)\ F{} 

A formatted string literal, or f-string, allows a programmer to create a string with placeholder expressions that are evaluated as the program executes. 
An f-string starts with an f character before the starting quote and uses curly braces { } to denote the placeholder expressions. 
A placeholder expression is also called a replacement field, as its value replaces the expression in the final output.
Additional f-string features

An = sign is provided after the expression in a replacement field to print both the expression and its result, which is a useful debugging technique when dynamically generating lots of strings and output. Ex: f'{2*4=}' produces the string "2*4=8".
Additionally, double braces {{ and }} are used to place a curly brace into an f-string. Ex: f'{{Jeff Bezos}}: Amazon' produces the string "{Jeff Bezos}: Amazon".


List Basics 
Lists are used to store multiple items in a single variable. A list is a container created by surrounding a sequence of variables or literals with brackets [ ]. 

Ex: my_list = [10, 'abc'] creates a new list variable my_list that contains the two items: 10 and 'abc'.
A list item is called an element. A list is mutable, meaning that the elements in a list can be replaced, reordered, or removed.
Tuples allow for Multiple of the same items in a list
Or False = 0 True =1
| Feature       | List (`list`) | Tuple (`tuple`) | Set (`set`) |
|--------------|--------------|---------------|------------|
| **Mutability** | ✅ Mutable (can change) | ❌ Immutable (cannot change) | ✅ Mutable (but elements are immutable) |
| **Ordered** | ✅ Yes | ✅ Yes | ❌ No |
| **Allows Duplicates** | ✅ Yes | ✅ Yes | ❌ No |
| **Indexable** | ✅ Yes | ✅ Yes | ❌ No |
| **Allows Mixed Data Types** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Hashable (Can be a Dictionary Key)** | ❌ No | ✅ Yes | ❌ No |
| **Performance** | ❌ Slower | ✅ Faster | ✅ Fastest for membership tests |
| **Best for** | **Modifiable sequences** | **Fixed data** | **Unique items & fast lookups** |

- Use a **list** if your data **needs to be modified** frequently and order matters.  
- Use a **tuple** if your data **should remain constant** and you want **better performance**.  
- Use a **set** if you **need only unique elements** and **fast membership checks**.





