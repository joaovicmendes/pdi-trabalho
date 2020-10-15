def flood_fill(img, origin):
    obj = []              # Lista com coordenadas do objeto
    visited = set()       # Conjunto dos pontos visitados
    queue = deque()       # Fila de pontos a serem visitados
    
    queue.append(origin)
    while queue:
        
        row, col = queue.popleft()
        
        if (row, col) not in visited:
            obj.append((row, col))
            visited.add((row, col))

            up    = (row-1, col)  # Vizinho de cima
            right = (row, col+1)  # Vizinho da direita
            down  = (row+1, col)  # Vizinho de baixo
            left  = (row, col-1)  # Vizinho da esquerda

            if row != 0:
                if (up not in visited) and \
                   (img[up] == img[origin]):
                    queue.append(up)

            if col != img.shape[1]-1:
                if (right not in visited) and \
                   (img[right] == img[origin]):
                    queue.append(right)

            if row != img.shape[0]-1:
                if (down not in visited) and \
                   (img[down] == img[origin]):
                    queue.append(down)

            if col != 0:
                if (left not in visited) and \
                   (img[left] == img[origin]):
                    queue.append(left)
                    
    return obj
