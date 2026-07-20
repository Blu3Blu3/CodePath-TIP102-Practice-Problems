"""
	Abby Lee of Dance Moms is looking for the perfect song to choreograph a group routine to and needs a song of a specified length. Given a specific song length length and a list of song lengths playlist sorted in ascending order, use the binary search algorithm to return the index of the song in playlist with length. If no song with the target length exists, return -1.
	
	(U)
	Use binary search on list "playlist" for the int song length "length". Return its index if it's found, and -1 otherwise.
	
	Input: playlist ([int]) to search to for length (int) in
	Output: index of length OR -1 if not found
	
	Edge cases:
	-   Empty playlist --> -1, can't check for anything in an empty list
	
	(M)
	Binary search
	
	(P)
	Binary search
"""

def find_perfect_song(playlist, length):
    l = 0
    r = len(playlist) - 1
    m = (l + r) // 2
    while l <= r:
        if playlist[m] == length:
            return m
        elif playlist[m] < length:
            l = m + 1
            m = (l + r) // 2
        else:
            r = m - 1
            m = (l + r) // 2
    return -1

print(find_perfect_song([101, 102, 103, 104, 105], 103))
print(find_perfect_song([201, 202, 203, 204, 205], 206))
		
def can_attend(tour_dates, available):
    """
    Your favorite artist is doing a short residency in your city and you're hoping to attend one of their concerts! But because of school, you're only free one day this month 😭. Given a sorted list of integers tour_dates representing the days this month your favorite artist is playing, and an integer available representing the day you are available, write a recursive function can_attend() that returns True if you will be able to attend one of their concerts (some date in tour_dates matches available) and False otherwise.

	Your solution must have O(log n) time complexity.
    """