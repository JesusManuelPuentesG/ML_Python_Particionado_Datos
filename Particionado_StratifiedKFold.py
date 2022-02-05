…

# Librería necesaria para utilizar el particionado estratificado
from sklearn.model_selection import StratifiedKFold

…

# Crear objeto StratifiedKFold.

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)

for train_index, test_index in skf.split(z, y2):
    X_train, X_test = z[train_index], z[test_index]
    y_train_pre, y_test_pre = y2[train_index], y2[test_index]
    
…