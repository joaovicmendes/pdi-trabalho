def flood_fill_rec(img, x, y, replacement):
    target = img[x][y]
    flood_fill_recursao(img, x, y, target, replacement)
    return

def flood_fill_recursao(img, x, y, target, replacement):
    row,cols = img.shape
    if img[x][y] != target:
        return
    elif img[x][y] == replacement:
        return
    else:
        img[x][y] = replacement
        if (x-1)>=0:
            flood_fill_recursao(img, x-1, y, target, replacement)
        if(y-1)>=0:
            flood_fill_recursao(img, x, y-1, target, replacement)
        if(x+1<row):
            flood_fill_recursao(img, x+1, y, target, replacement)
        if(y+1<cols):
            flood_fill_recursao(img, x, y+1, target, replacement)
        
