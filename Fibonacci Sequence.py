# Input asking the number of terms and using the fibonnaci sequence
nterms = int(input("How many terms? "))

# First two terms, nv1 and nv2 representing number variable one and two.
nv1, nv2 = 0, 1
count = 0

# Check if the number of terms is valid.
if nterms <= 0:
   print("Please enter a positive integer")

# If there is only one term, return nv1.
elif nterms == 1:
   print("Fibonacci sequence up to",nterms,":")
   print(nv1)

# Generate fibonacci sequence.
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(nv1)
       nth = nv1 + nv2
       
       # Update the values.
       nv1 = nv2
       nv2 = nth
       count += 1
