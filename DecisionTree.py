from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

# Modélisation de l'arbre de classification
def decisionTreeTrainTest(df_total, test_size):
    df_total_X = df_total[['platform', 'mapname', 'clearancelevel', 'skillrank', 'role', 'operator']]
    label_encoder = LabelEncoder()
    df_total_X = df_total_X.apply(label_encoder.fit_transform)

    X_train, X_test, y_train, y_test = train_test_split(df_total_X, df_total.haswon, random_state=111, test_size=test_size)

    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(X_train, y_train)

    score = accuracy_score(y_test, dtree.predict(X_test))
    print("score de performance pour un pourcentage de données de test de " + str(test_size) + ": " + str(score))

def decisionTreeKFold(df_total, n_folds):
    df_total_X = df_total[['platform', 'mapname', 'clearancelevel', 'skillrank', 'role', 'operator']]
    label_encoder = LabelEncoder()
    df_total_X = df_total_X.apply(label_encoder.fit_transform)
    df_total_y = df_total.haswon

    kf = KFold(n_splits=n_folds, random_state=None)

    dtree = DecisionTreeClassifier()

    acc_score = []
    for train_index, test_index in kf.split(df_total_X) :
        X_train = df_total_X.iloc[train_index]
        X_test = df_total_X.iloc[test_index]
        y_train = df_total_y.iloc[train_index]
        y_test = df_total_y.iloc[test_index]

        dtree.fit(X_train, y_train)
        pred_values = dtree.predict(X_test)

        acc = accuracy_score(pred_values, y_test)
        acc_score.append(acc)

    avg_acc_score = sum(acc_score)/n_folds

    print("score de performance moyen pour tous les plis: " + str(avg_acc_score))