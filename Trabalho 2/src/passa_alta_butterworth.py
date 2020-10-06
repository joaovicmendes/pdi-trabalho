def filtro_passa_baixa_butterworth(img, d0, n):
    num_rows, num_cols = img.shape   
    freq_r, freq_c = generate_frequencies(num_rows, num_cols)
    
    low_pass_butterworth = np.zeros([num_rows, num_cols])
    for row in range(num_rows):
        for col in range(num_cols):
            dist = np.sqrt(freq_r[row]**2 + freq_c[col]**2)
            H = 1/(1 + (dist/d0)**(2*n))
            
            low_pass_butterworth[row, col] = H
    
    return low_pass_butterworth