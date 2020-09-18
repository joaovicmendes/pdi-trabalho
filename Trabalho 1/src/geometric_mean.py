import numpy as np

def geometric_mean(img, m, n):
    '''Calcula a média geométrica na imagem img com um filtro de tamanho m por n.

        Parâmetros
        ----------
        img : numpy array.
            Imagem a ser filtrada.
        m : uint
            Número de linhas para o filtro.
        n : uint
            Número de colunas para o filtro.
        Return
        -------
        img_filtered : numpy array, mesmo tamanho que img
            Imagem filtrada
    '''

    num_rows, num_cols = img.shape

    # Cria imagem com zeros ao redor da borda
    half_row_size = m//2
    half_col_size = n//2
    img_padded = np.pad(img, ((half_row_size,half_row_size),
                              (half_col_size,half_col_size)),
                        mode='constant')

    # Aplicação do filtro de média geométrica
    img_filtered = np.zeros((num_rows, num_cols))
    for row in range(num_rows):
        for col in range(num_cols):
            product_region = 1
            for s in range(m):
                for t in range(n):
                    # Pequena alteração na fórmula para impedir overflow durante
                    # a multiplicação, considera a propriedade da exponencial de 
                    # que (a * b)^n == a^n * b^n
                    product_region *= (img_padded[row+s, col+t])**(1./(m*n))
            img_filtered[row, col] = product_region

    return img_filtered
