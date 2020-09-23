def median(img,m,n):
    
    num_row, num_col = img.shape

    half_row_size = m//2
    half_col_size = n//2
    img_padded = np.pad(img, ((half_row_size,half_row_size),
                              (half_col_size,half_col_size)),
                        mode='symmetric')
    
    img_filtered = np.zeros((num_row,num_col))
    for row in range(num_row-1):
        for col in range(num_col-1):
            
            med_array = []
            for k in range(m):
                for y in range(n):
                    med_array.append(img_padded[row+k][col+y])
            med_array = np.sort(med_array)
            median = len(med_array)//2
            if(len(med_array)%2 == 0):
                img_filtered[row][col] = ((med_array[median-1]*0.5)+(med_array[median]*0.5)).astype('uint8')
            else:
                img_filtered[row][col] = med_array[median]
    return img_filtered
