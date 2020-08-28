from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import glob
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_curve
from sklearn.metrics import f1_score, confusion_matrix, balanced_accuracy_score
from sklearn.metrics import classification_report, mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import KFold
from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray
import os



def open_images(path):
    train_images = imread(path)
    grey_image = rgb2gray(train_images) #makes image gray scale
    grey_size = resize(grey_image, (32, 32))
    # grey_ravel = gray_size.ravel()
    grey_reshaped = np.reshape(grey_size, 1024)
    # print(grey_reshaped.shape)
    return grey_reshaped

def make_X_y():
    X = []
    y = []   
    dog_ids = []

    all_images = os.listdir('../../../data/img/img_dumps/')[:10]

    for dog_pic_label in all_images:
        path = glob.glob('../../../data/img/img_dumps/*.jpg')[:10]
        label = (dog_pic_label)
        if 'adoptable' in label:
            label = 0
        # if 'adopted' in label:
            
        else:
            label = 1
        y.append(label)

               
    for p in path:                
        X.append(open_images(p))
        dog_ids.append(dog_pic_label) #this is for keeping track of the dogs if necessary     


    X = np.asarray(X).reshape(1, -1) #flatten()
    y = np.asarray(y).flatten().reshape(-1, 1) #[:-1] #the [:-1] compensates for an extra appended in y, otherwise data aligns


    print("length X: ", len(X))
    print("length y: ", len(y))
    # length X:  10240
    # length y:  10
    # print("all images: ", all_images)
    # print(y)
    
    # print("my y shape: ", y.shape)
    print("my x shape: ", X.shape)
    print("my y shape:", y.shape)
    # my y shape:  (10,)
    # my x shape:  (10240,)

    # print("X: ", X)
    # [0.80352947 0.78541051 0.7618935  ... 0.3539922  0.38858436 0.42183868]
    
    # print("my y:", y)
    # [0 1 0 1 0 1 0 1 1 1]
    return X, y, all_images


def naive_bayes():
    X, y, all_images = make_X_y()
    X_train, X_test, y_train, y_test = train_test_split(X, y)    
    
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("Naive Bayes Accuracy: ", acc)
    return acc

    
if __name__ == '__main__':
    # root_mean = rmse(y_true, y_predict)
    X, y, all_images = make_X_y()
    # naive_bayes = naive_bayes()
    # X = np.array(X)
    # print(X)
    # X = X_0.reshape(-1, 1)
    # y = y_0.reshape(-1, 1)
    
    print(__doc__)


# Code source: Gaël Varoquaux
#              Andreas Müller
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import make_moons, make_circles, make_classification
    from sklearn.neural_network import MLPClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.svm import SVC
    from sklearn.gaussian_process import GaussianProcessClassifier
    from sklearn.gaussian_process.kernels import RBF
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

    h = .02  # step size in the mesh

    names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
            "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
            "Naive Bayes", "QDA"]

    classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="linear", C=0.025),
        SVC(gamma=2, C=1),
        GaussianProcessClassifier(1.0 * RBF(1.0)),
        DecisionTreeClassifier(max_depth=5),
        RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
        MLPClassifier(alpha=1, max_iter=1000),
        AdaBoostClassifier(),
        GaussianNB(),
        QuadraticDiscriminantAnalysis()]

    # X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
    #                         random_state=1, n_clusters_per_class=1)
    
    
    rng = np.random.RandomState(2)
    # X += 2 * rng.uniform(size=X.shape)
    linearly_separable = (X, y)

    datasets = [make_moons(noise=0.3, random_state=0),
                make_circles(noise=0.2, factor=0.5, random_state=1),
                linearly_separable
                ]

    figure = plt.figure(figsize=(27, 9))
    i = 1
    # iterate over datasets
    for ds_cnt, ds in enumerate(datasets):
        # preprocess dataset, split into training and test part
        X, y = ds

        X = StandardScaler().fit_transform(X)
        X_train, X_test, y_train, y_test = \
            train_test_split(X, y, test_size=.4, random_state=42)

        x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
        y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                            np.arange(y_min, y_max, h))

        # just plot the dataset first
        cm = plt.cm.RdBu
        cm_bright = ListedColormap(['#FF0000', '#0000FF'])
        ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
        if ds_cnt == 0:
            ax.set_title("Input data")
        # Plot the training points
        ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
                edgecolors='k')
        # Plot the testing points
        ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6,
                edgecolors='k')
        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        i += 1

        # iterate over classifiers
        for name, clf in zip(names, classifiers):
            ax = plt.subplot(len(datasets), len(classifiers) + 1, i)
            clf.fit(X_train, y_train)
            score = clf.score(X_test, y_test)

            # Plot the decision boundary. For that, we will assign a color to each
            # point in the mesh [x_min, x_max]x[y_min, y_max].
            if hasattr(clf, "decision_function"):
                Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
            else:
                Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

            # Put the result into a color plot
            Z = Z.reshape(xx.shape)
            ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)

            # Plot the training points
            ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright,
                    edgecolors='k')
            # Plot the testing points
            ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright,
                    edgecolors='k', alpha=0.6)

            ax.set_xlim(xx.min(), xx.max())
            ax.set_ylim(yy.min(), yy.max())
            ax.set_xticks(())
            ax.set_yticks(())
            if ds_cnt == 0:
                ax.set_title(name)
            ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
                    size=15, horizontalalignment='right')
            i += 1

    plt.tight_layout()
    # plt.show()




