"""
1. Which configuration of data in a list causes the smallest number of exchanges 
in a selection sort? Which configuration of data causes the largest number of 
exchanges?

 - smallest number of exchanges: when the data is already, or closest to smallest to largest values

 - largest number of exchanges: when the data has a reverse sort configuration, i.e. sorted largest => smallest

 2. Explain the role that the number of data exchanges plays in the analysis of 
 selection sort and bubble sort. What role, if any, does the size of the data 
 objects play?

 - they both grow quadratically (n^2) based on the number of objects in the sort

 3. Explain why the modified bubble sort still exhibits O(n^2) behavior on average.

 - The modified bubble sort will go through n elements + n-1 elements if even 1 swap operation occurs

 4. Explain why insertion sort works well on partially sorted lists. 

 - The inner loop will break whenever the item to insert >= the item at the position being checked
 - insertion points are found sooner in a sorted list...
"""