# Array
An **[Array](https://en.wikipedia.org/wiki/Array)** is a data structures that holds a number of data items or elements of the same data type. When you want to store many pieces of data that are related and have the same data type,it is often better to use an array instead of many separate variables.

Each position in an array is identified by an index, most language use zero-based indexing which means that the indexing start at 0 (Zero). The value stored in array are mutable, which mean they can be changed while the program is running, just like a content of variable.

### One Dimensional Arrays
You can think of a one-dimesional array as a single row of values. here is an example storing 5 values in an array.

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- | 
| values | Orange | Apple | Avocado | Rambutan | Banana | Durian | 

### Two Demensional Arrays
Array can have more than one dimension. you could envisage a two-dimensional array as a table with rows and columns.

| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Shcool | Pull | Where | Said | Today | Tomorrow |
| 1 | Path | Floor | Sugar | Because | Beautiful | Book |
| 2 | Question | Answer | Group | Minute | Populer | Pen | 

### Three Demensional Arrays
When you work with three or more dimensions, it is hard to visualise the data. Fortunately, in the programming you do not need to do this, you just decide the dimensions and the order in which you will index the data. Then be consistent throughout.

In a three-dimensional arrays every item is positioned using three indexes. We can build on our example of a spelling game to imagine a game that could be used for children across five years of learning. There would be 5 years x 3 levels x 10 words.