def nearest_meeting_point(edges, cell1, cell2):
  # cell1_count and cell2_count represent distance from root
  c1 = cell1
  cell1_count = 0
  while edges[c1] != -1:
    c1 = edges[c1]
    cell1_count += 1

  c2 = cell2
  cell2_count = 0
  while edges[c2] != -1:
    c2 = edges[c2]
    cell2_count += 1

  # get both nodes to same "level of ancestry"
  # note: only one of these while loops will ever execute
  while cell1_count > cell2_count:
    cell1 = edges[cell1]
    cell1_count -= 1
  while cell2_count > cell1_count:
    cell2 = edges[cell2]
    cell2_count -= 1

  # find the nearest meeting point (lowest common ancestor)
  while cell1 != cell2:
    cell1 = edges[cell1]
    cell2 = edges[cell2]
  return cell1
 
edges = [4, 4, 1, 4, 13, 8, 8, 8, 0, -1, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, -1, 21]
print nearest_meeting_point (edges, 2, 3)
print nearest_meeting_point (edges, 14, 16)
print nearest_meeting_point (edges, 7, 16)
