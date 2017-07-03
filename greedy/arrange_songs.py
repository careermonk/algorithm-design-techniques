# Copyright (c) June 02, 2017 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2017-06-02 06:15:46 
# Last modification		: 2017-06-02 
# Modified by		        : Narasimha Karumanchi 
# Book Title			: Algorithm Design Techniques
# Warranty         		: This software is provided "as is" without any 
# 				 warranty; without even the implied warranty of 
# 				 merchantability or fitness for a particular purpose. 

def arrange_songs( A ):
    # sort the songs based on their lenghs
    A.sort()

def forward_time_of_song(A, song_number):
    if song_number <= 0 or song_number > len(A):
        return -1
    return sum(A[:song_number-1])

# array of songs with their lengs in minutes 
A = [3, 6, 9, 3, 5, 1, 4 , 7, 19]
arrange_songs(A)

waiting_time_of_song = forward_time_of_song(A, 3)
print waiting_time_of_song

waiting_time_of_song = forward_time_of_song(A, 0)
print waiting_time_of_song

waiting_time_of_song = forward_time_of_song(A, 10)
print waiting_time_of_song
