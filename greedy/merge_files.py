def merge_files( F ):
	# sort the files based on their lenghs
	F.sort()
	merge_time_for_two_files = F[0] + F[1]
	total_merge_time = merge_time_for_two_files
	for i in range(2, len(F)):
	    merge_time_for_two_files = merge_time_for_two_files + F[i]
	    total_merge_time += merge_time_for_two_files
	return total_merge_time

# array of files with their lengs 
F = [10,5,100,50,20,15]
print merge_files(F)
