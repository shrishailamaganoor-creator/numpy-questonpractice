#20 moderate level questions on numpy
import numpy as np
#Explain broadcasting with an example of adding a (3,3) array and a (3,) array.
a=np.zeros((3,3))
b=np.array([1,2,3])
print("a+b",a+b)
#How do you perform boolean indexing to filter values greater than 5?
print(a[a>5])
#How do you use np.where() to replace values conditionally?
print(np.where(a,a<3,0))
#"What's the difference between .copy() and a view/slice in NumPy?"
a=np.array([1,2,3,4,5,6])
copy=a[0:3].copy()
copy[0]=1000#data here is copied and made new
view=a[0:3]
view[0]=11111#data here is shared
print(a)
#How do you stack arrays vertically and horizontally (vstack, hstack)?
a=np.empty(3)
b=np.ones((3))
print(np.hstack((a,b)))
print(np.vstack((a,b)))
#How do you split an array into 3 equal parts?
a=np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print(np.split(a,3))
#How do you compute row-wise and column-wise sums in a 2D array (axis parameter)?
print(np.sum(a,axis=0))#row
print(np.sum(a,axis=1))#coloum
#How do you find unique values in an array along with their counts?
print(np.unique_counts(a))
#How do you sort a 2D array by a specific column?
a=np.array([[1,2,3],
                    [7,8,9],
                    [4,5,6]])
d=a[0:3,0:1]
print(np.sort(d))    
#How do you use fancy indexing to select specific rows/columns by index list?
print(a[:,[0,2]])
#How do you compute the dot product of two matrices?
print(a@d)
#What's the difference between element-wise multiplication and matrix multiplication?
print(a*d)#elemntwise
print(np.matmul(a,d))
#How do you transpose a matrix?
print(a.T)
#How do you use np.newaxis or reshape(-1,1) to add a dimension?
print(a[:,np.newaxis])

#How do you handle NaN values (detect with isnan, replace with nanmean)?
#a=np.array([[1,2,3],
#                    [4,None,6],
#                    [7,8,9]])
#print(np.isnan(a),np.replace(a,np.isnan))
#How do you compute cumulative sum and cumulative product?
print(np.cumsum(a))
print(np.prod(a))
#How do you use np.clip() to bound values within a range?
print(np.clip(a,0,4))
#How do you generate a random array from a normal distribution?
print(np.random.normal(-10,10,6))
#How do you use np.argsort() and np.argmax()
a=np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print(np.argsort(a),np.argmax(a))
#How do you apply a custom function to every element using np.vectorize()?
def cube(x):
    return x**3
fun = (np.vectorize(cube))
print(fun(a))
