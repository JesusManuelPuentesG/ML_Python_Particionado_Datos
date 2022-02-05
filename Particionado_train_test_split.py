…

# Librería necesaria para utilizar el particionado
from sklearn.model_selection import train_test_split

…

# Generamos los datasets de entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(z, y2, test_size=0.20, random_state=42)

…