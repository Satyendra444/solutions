def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    rows, columns = len(map_matrix), len(map_matrix[0])
    visited = [[False for _ in range(columns)] for _ in range(rows)]
    queue = [(from_row, from_column)]
    visited[from_row][from_column] = True
    
    while queue:
        cur_row, cur_column = queue.pop(0)
        if cur_row == to_row and cur_column == to_column:
            return True
        for row, column in [(cur_row-1, cur_column), (cur_row+1, cur_column), (cur_row, cur_column-1), (cur_row, cur_column+1)]:
            if 0 <= row < rows and 0 <= column < columns and map_matrix[row][column] and not visited[row][column]:
                queue.append((row, column))
                visited[row][column] = True
    return False

if __name__ == '__main__':
    map_matrix = [
        [True, False, False],
        [True, True, False],
        [False, True, False]
    ]
    print(route_exists(0, 0, 2, 2, map_matrix))
