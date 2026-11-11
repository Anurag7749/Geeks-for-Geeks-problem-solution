class Solution:
	def subsetSums(self, arr):
		result=[]
		def func(index,subset):
		    if index>=len(arr):
		        result.append(sum(subset))
		        return
		    subset.append(arr[index])
		    func(index+1,subset)
		    subset.pop()
		    func(index+1,subset)
		func(0,[])
		return result
		

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna