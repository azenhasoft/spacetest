from sklearn.linear_model import LogisticRegression

# Dados de exemplo (tamanho, velocidade, vai cair?)
X = [[10, 50], [5, 20], [15, 60], [8, 30]]
y = [1, 0, 1, 0]

# Criar e treinar o modelo
modelo = LogisticRegression()
modelo.fit(X, y)