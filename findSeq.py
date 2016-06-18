'''Consider this puzzle: by starting from the number 1 and repeatedly
either adding 5 or multiplying by 3, an infinite amount of new numbers
can be produced. How would you write a function that, given a num-
ber, tries to find a sequence of such additions and multiplications that
produce that number? For example, the number 13 could be reached by
first multiplying by 3 and then adding 5 twice, whereas the number 15
cannot be reached at all.'''



def findSeq(start,history,target):
	if start==target:
		return history+"="+str(target)
	elif start>target:
		return 0
	else:
		return findSeq(5+start,"("+history+"+ 5)",target) or findSeq(3*start,"("+history+"*3)",target)

num=int(raw_input("Enter number: "))
print findSeq(1,"1",num) 