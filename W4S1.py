from collections import deque

#Problem 1

# def extract_nft_names(nft_collection):
#     res = []

#     for nft in nft_collection:
#         res.append(nft["name"])
    
#     return res


# # def extract_nft_names(nft_collection):
# #     pass

# # # Example usage:
# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
# ]

# nft_collection_2 = [
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
# ]

# nft_collection_3 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))
# Example Output:

# ['Abstract Horizon', 'Pixel Dreams', 'Future City']
# ['Crypto Kitty', 'Galactic Voyage']
# ['Golden Hour']

# Problem 2

# def extract_nft_names(nft_collection):
#     nft_names = []
#     for nft in nft_collection:
#         nft_names.append(nft["name"])
#     return nft_names

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
# ]

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# nft_collection_3 = []

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))

#Problem 3

# def identify_popular_creators(nft_collection):
#     creatorCount = {}
#     res = []

#     for nft in nft_collection:
#         creator = nft["creator"]

#         if creator in creatorCount:
#             creatorCount [creator]+= 1
#         else:
#             creatorCount [creator] = 1
#     res = []

#     for creator, count in creatorCount.items():
#         if count > 1:
#            res.append(creator) 
#     return res

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]

# nft_collection_2 = [
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
#     {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
# ]

# nft_collection_3 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# print(identify_popular_creators(nft_collection))
# print(identify_popular_creators(nft_collection_2))
# print(identify_popular_creators(nft_collection_3))

#Problem 4

# def average_nft_value(nft_collection):
#     total = 0
#     count = 0 

#     for nft in nft_collection:
#         total += nft["value"]
#         count += 1
    
#     return total / count if (count > 0) else 0

# # Example Usage:

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]
# print(average_nft_value(nft_collection))

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]
# print(average_nft_value(nft_collection_2))

# nft_collection_3 = []
# print(average_nft_value(nft_collection_3))

#Problem 5
# O(n^3) for time, O(n) for space? Only one list made...
# def search_nft_by_tag(nft_collections, tag):
#     res = []

#     for coll in nft_collections:
#         for nft in coll:
#             if tag in nft["tags"]:
#                 res.append(nft["name"])

#     return res

# nft_collections = [
#     [
#         {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
#         {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
#     ],
#     [
#         {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
#         {"name": "City Lights", "tags": ["modern", "landscape"]}
#     ]
# ]

# nft_collections_2 = [
#     [
#         {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
#         {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
#     ],
#     [
#         {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
#     ]
# ]

# nft_collections_3 = [
#     [
#         {"name": "The Last Piece", "tags": ["finale", "abstract"]}
#     ],
#     [
#         {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
#         {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
#     ]
# ]

# print(search_nft_by_tag(nft_collections, "landscape"))
# print(search_nft_by_tag(nft_collections_2, "sunset"))
# print(search_nft_by_tag(nft_collections_3, "modern"))

#Problem 6
# def process_nft_queue(nft_queue):
#     queue = deque(nft_queue)
#     res = []

#     while queue:
#         nft = queue.popleft()
#         res.append(nft["name"])

#     return res

# Example Usage:

# nft_queue = [
#     {"name": "Abstract Horizon", "processing_time": 2},
#     {"name": "Pixel Dreams", "processing_time": 3},
#     {"name": "Urban Jungle", "processing_time": 1}
# ]
# print(process_nft_queue(nft_queue))

# nft_queue_2 = [
#     {"name": "Golden Hour", "processing_time": 4},
#     {"name": "Sunset Serenade", "processing_time": 2},
#     {"name": "Ocean Waves", "processing_time": 3}
# ]
# print(process_nft_queue(nft_queue_2))

# nft_queue_3 = [
#     {"name": "Crypto Kitty", "processing_time": 5},
#     {"name": "Galactic Voyage", "processing_time": 6}
# ]
# print(process_nft_queue(nft_queue_3))
# Example Output:

# ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
# ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
# ['Crypto Kitty', 'Galactic Voyage']

#Problem 7
# def validate_nft_actions(actions):
#     stack = []

#     for action in actions:
#         if action == "add":
#             stack.append(action)
#         elif stack and action == "remove":
#             stack.pop()

#     return len(stack) == 0


# actions = ["add", "add", "remove", "remove"]
# actions_2 = ["add", "remove", "add", "remove"]
# actions_3 = ["add", "remove", "remove", "add", "remove"]

# print(validate_nft_actions(actions))
# print(validate_nft_actions(actions_2))
# print(validate_nft_actions(actions_3))

# Problem 8
