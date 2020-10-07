def filtro_passa_alta_butterworth(img, d0, n):    
    num_rows, num_cols = img.shape   
    freq_r, freq_c = generate_frequencies(num_rows, num_cols)
    
    high_pass_butterworth = np.zeros([num_rows, num_cols])
    
    for row in range(num_rows):
        for col in range(num_cols):
            dist = np.sqrt(freq_r[row]**2 + freq_c[col]**2)
            if dist == 0:
                dist = 1
            H = 1/(1+(d0/dist)**(2*n))
            
            high_pass_butterworth[row,col] = H
    
    return high_pass_butterworth
