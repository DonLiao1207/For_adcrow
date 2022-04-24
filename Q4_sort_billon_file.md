## Question:
### Please explain how you would sort a file containing a billion numbers of integers?
### Answer:
* **STEP 1**:  
**1-1.** Divide a billion data into 100 blocks, read in blocks and store them in 100 small files.
* **STEP 2**:  
**2-1.**  Sort 100 small files (100 million data).  
**2-2.**  For memory consideration, for 100 files, read 1 million data each time, do merge sort or quick sort in loop, and write the result to the target file.
* **STEP 3**:  
**3-1.**  Repeat 2-2 operations, read the remaining data in turn, sort and append to the end of the target file.

