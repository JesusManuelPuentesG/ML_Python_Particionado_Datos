# ML_Python_Particionado_Datos

Código Python con varias formas de particionar los datos con y sin estratificación


## CONTENIDO:

### Train_test_split

Se muestra el código necesario para aplicar un particionado distribuyendo los datos con un reparto al 20% para pruebas (_test_size_) y al 80% para entrenamiento, distribuyendo las muestras de forma aleatoria. Se guardan los distintos datasets en variables.

### StratifiedKFold

Se muestra el código necesario para aplicar un particionado estratificado a 5 capas mediante validación cruzada, distribuyendo los datos por igual en un reparto al 20% para pruebas y al 80% para entrenamiento. Primero se crea el objeto con muestras aleatorias y después se particiona con la función _Split_ del objeto. Se guardan los distintos datasets en variables.


##

_Nota: Todas las variables mostradas con referencia a las letras X o y (X, y, X_test, y_test, ytest, ypred, etc.) hacen referencia al conjunto de datos utilizado, donde los contenidos con la letra X son el conjunto de características disponible y con la letra y son la característica a predecir._
