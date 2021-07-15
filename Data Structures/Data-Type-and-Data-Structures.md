# Data Type and Data Structures
There are to many different type of data and many ways in which data be stored, in this section we will learn about
data type, data structures and intro to Abstract Data Type (ADT)

### Data type
The variable can determines what value it can handle or what data can be stored in the variable here is some data type
1. **Integer** is an example of a [Primitive Data Type](https://en.wikipedia.org/wiki/Primitive_data_type) it can only contain one value
2. **Composite** or **Compound data type** is built by combining primitive data type example is like a **Class** or **record** read more in C [Compound Data Type](https://en.wikipedia.org/wiki/Composite_data_type)
3. **Data Structures** is a collection of a data is organised to allow effecient processing. ex, Array can be sorted using a wide range of algorithms. Different data structures lend themselves of different applications.
4. **Abstract Data Type** is conceptual model that describes how data organised and which operations can be carried out on the data (e, g Delete, Insert) from the perspective of an end user who does not need to know how this is implemented.

### Static and Dynamic Data Structures
**Static Data Sctuctures** work with reserve memory for a set of data, many programming language ***Array*** usually implemented as a static data structure, it fized size and can only contaion elements in the same data type, it can be changed, but can not be resized, if programmer need an array of a different size,they would need to create new array and copy the content from original array to the new array.

### Dynamic Data Structures
**Dynamic Data Structures** are memory efficient, the memory capability not fixed, the number of data items it can hold is contained only overall memory allocation to the program, Linked-list is an example of [Dynamic Data Structures](https://www.webopedia.com/definitions/dynamic-data-structure/)

### Built-in Data Structures
**Built-in Data Structures** most programming languages have it own built-in data structures, for example python has a built-in Data structures list (the best features of combination of array and linked-list)

with built-in data structures the implementation is abstracted, you will not know how it has been built.

### Memory Management
Memory for dynamic data structures such as [Linked-list](https://en.wikipedia.org/wiki/Linked_list) is taken from memory heap in the most high-level programming languages, we do not have to worry about managing the heap.