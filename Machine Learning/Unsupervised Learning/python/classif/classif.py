import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import LinearSVC
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

# In this application :
# apply linear and non linear separators on toy data and on images


# ######################################################
# useful function to plot SVM boundary
# ######################################################
def plot_boundary(clf, X, y):
    """
    Function to plot a boundary decision
    """
    h = 0.002
    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure()
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

    plt.scatter(X[:, 0], X[:, 1], c=y, s = 100)
    plt.title('score : ' + str(clf.score(X,y)))
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')


# ######################################################
#       Linear Classifier on toy data
# ######################################################

# 1) Generate a separable training set and visualize it
np.random.seed(21)
X = np.random.rand(50,2)
# put linearly separable labels
y = X[:,0] > 0.5
plt.scatter(X[:,0],X[:,1], c = y, s = 100)
plt.savefig('linear_data.png')

# 2) Apply a linear classifier (use LinearSVC with C=1)
clf = LinearSVC(C=1)
# TO FILL
print("training scores:",clf.score(X,y))
plot_boundary(clf,X,y)
plt.savefig('linear_SVC.png')


#3) Add some noise in the dataset
np.random.seed(2)
X = np.random.rand(100,2)
y = X[:,0] > 0.5
lines_noise = np.random.choice(range(len(y)), 10)
y[lines_noise] = 1 - y[lines_noise]
plt.close()
plt.scatter(X[:,0],X[:,1], c = y, s = 100)
plt.savefig('linear_data_noise.png')

# Evaluate the effect of regularization coefficient
for C in [10**x for x in range(-5,6)]:
    # Fit a linear SVC with growing C
    # TO FILL
    print("training score for C = %.3f : %.3f"%(C,clf.score(X,y)))
    plt.clf()
    plot_boundary(clf,X,y)
    plt.title('C = ' + str(C))
    plt.savefig('boundary_C_%.3f.png'%C)

# ######################################################
#       Non linear Classifier on toy data
# ######################################################

# 3) Use non linear data (moon)
from sklearn.svm import SVC
from sklearn.datasets import make_moons

# Creation of a training set
X, y = make_moons(noise = 0.1, random_state=1, n_samples=40)
plt.clf()
plt.scatter(X[:,0],X[:,1], c = y, s = 100)
plt.savefig('moon_train_data.png')
# Creation of a testing set
X_test, y_test = make_moons(noise = 0.1, random_state=321, n_samples=20)
plt.scatter(X_test[:,0],X_test[:,1], c = y_test, s = 100)
plt.savefig('moon_test_data.png')

# Try a  SVM with polynomial kernel of degree 3 (and initial coef0 = 1, Better suited for these data)
# and evaluate the effect of the margin
for C in [10**x for x in range(-2,8)]:
    # TO FILL
    print("training score:",clf.score(X,y), ". testing score:", clf.score(X_test,y_test))
    plot_boundary(clf,X,y)
    plt.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1], c = 'green', s = 200, marker='*')
    plt.savefig('moon_polynomial_kernel_C_%.3f.png'%C)

# Try a  SVM with gaussian kernel (rbf)
# and evaluate the effect of the margin
for C in [10**x for x in range(-3,5)]:
    # TO FILL
    print("training score:",clf.score(X,y), ". testing score:", clf.score(X_test,y_test))
    plot_boundary(clf,X,y)
    plt.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1], c = 'green', s = 200, marker='*')
    plt.savefig('moon_gaussian_kernel_C_%.3f.png'%C)



# ######################################################
# Apply SVM on satellite images
# ######################################################
# Loading data
import pickle
# load sat data (3 bands)
with open('./images/sat_image_R.pkl', 'rb') as handle:
    sat_dataR = pickle.load(handle)
with open('./images/sat_image_G.pkl', 'rb') as handle:
    sat_dataG = pickle.load(handle)
with open('./images/sat_image_B.pkl', 'rb') as handle:
    sat_dataB = pickle.load(handle)
# load sat classes
with open('./images/sat_label.pkl', 'rb') as handle:
    sat_classes = pickle.load(handle)

# verify labels
table_of_labels=np.unique(sat_classes)
number_of_labels = len(table_of_labels)
print(number_of_labels , 'labels : ' , table_of_labels)
# reshape data
# verify the shape and reshape data to fit with
# a matrix (N x D) of N points in D dimension
channels=3
size_x,size_y=sat_dataR.shape
sat_data=np.zeros((size_x,size_y,channels))
sat_data[:,:,0]=sat_dataR
sat_data[:,:,1]=sat_dataG
sat_data[:,:,2]=sat_dataB
# Visualization of the image
plt.clf()
plt.imshow(sat_data.astype(np.float64)/255)
plt.show()
# Visualization of the labels
plt.clf()
plt.imshow(sat_classes)
plt.show()
# Creation of the dataset (data of size (size_x*size_y,channels)
# and labels (size_x*size_y,1))
# TO FILL
# Extract train data
nb_data_train=len(labels)
X=np.zeros((0,channels))
Y=np.zeros((0,1))
for i in range(1,number_of_labels):
    index_label=labels==table_of_labels[i]
    number_of_training_samples_i=len(np.where(index_label)[0])
    X=np.concatenate((X,data[np.where(index_label),:][0]),axis=0)
    Y=np.concatenate((Y,table_of_labels[i]*np.ones((number_of_training_samples_i,1))))
# split test train
# TO FILL
#
# PERFORM CLASSIFICATION
# TO FILL


# Print out performances
print("Classification report for classifier %s:\n%s\n"
      % (classification, metrics.classification_report(y_test, y_predict)))
y_image = classification.predict(data)

# Reshape image and save
label_image=y_image.reshape(size_x,size_y)
plt.clf()
plt.imshow(label_image)
plt.title('classification result')
plt.show()
plt.savefig('classification_result.png')

# ######################################################
# Problem ???? Some classes are imbalanced
# ######################################################
# Print the number of classes
number_of_training_samples_1=len(np.where(labels==1)[0])
number_of_training_samples_2=len(np.where(labels==2)[0])
number_of_training_samples_0=len(np.where(labels==0)[0])
print('number of samples in class 0 : %d'%number_of_training_samples_0)
print('number of samples in class 1 : %d'%number_of_training_samples_1)
print('number of samples in class 2 : %d'%number_of_training_samples_2)
# Modify the number of samples in class 0
number_of_training_samples_0=int(0.5*(number_of_training_samples_1+number_of_training_samples_2))
# Recreate the dataset
X=np.zeros((0,channels))
Y=np.zeros((0,1))
for i in range(0,number_of_labels):
    if i==0:
        # index with label 0
        index_label=np.where(labels==table_of_labels[i])
        # choose randomly number_of_training_samples_0 inside
        index_for_training = np.random.randint(0,len(index_label[0]),number_of_training_samples_0)
        X=np.concatenate((X,data[index_label[0][index_for_training],:]),axis=0)
        Y=np.concatenate((Y,table_of_labels[i]*np.ones((number_of_training_samples_0,1))))
    else:
        index_label=labels==table_of_labels[i]
        number_of_training_samples_i=len(np.where(index_label)[0])
        X=np.concatenate((X,data[np.where(index_label),:][0]),axis=0)
        Y=np.concatenate((Y,table_of_labels[i]*np.ones((number_of_training_samples_i,1))))

# split test train
# TO FILL
#
# PERFORM CLASSIFICATION
# TO FILL


# Print out performances

print("Classification report for classifier %s:\n%s\n"
      % (classification, metrics.classification_report(y_test, y_predict)))


y_image = classification.predict(data)
label_image=y_image.reshape(size_x,size_y)
plt.clf()
plt.imshow(label_image)
plt.title('classification result with balanced labels')
plt.savefig('classification_result_balanced.png')


# ######################################################
#       Apply on time series
# ######################################################
import tslearn
from tslearn.barycenters import \
    euclidean_barycenter, \
    dtw_barycenter_averaging, \
    dtw_barycenter_averaging_subgradient, \
    softdtw_barycenter
from tslearn.datasets import CachedDatasets

# ######################################################
#       Barycenter computation
# ######################################################

# fetch the example data set
np.random.seed(0)
X_train, y_train, _, _ = CachedDatasets().load_dataset("Trace")
X = X_train[y_train == 1]
length_of_sequence = X.shape[1]

# Useful function to plot series and eventually barycenter
def plot_series(X,barycenter=None):
    # plot all points of the data set
    for series in X:
        plt.plot(series.ravel(), "k-", alpha=.2)
    # plot the given barycenter of them
    if barycenter is not None:
        plt.plot(barycenter.ravel(), "r-", linewidth=2)

# Visualize series, Euclidian and DTW barycenters
plt.clf()
ax1 = plt.subplot(3, 1, 1)
plt.title("Series")
plot_series(X)
ax2 = plt.subplot(3, 1, 2)
plt.title("Eucledian Barycenter")
plot_series(X,euclidean_barycenter(X))
ax3 = plt.subplot(3, 1, 3)
plt.title("DTW Barycenter")
plot_series(X,dtw_barycenter_averaging(X, max_iter=50, tol=1e-3))
plt.show()


# ######################################################
#       KNN search based on DTW
# ######################################################


from tslearn.neighbors import KNeighborsTimeSeries
from tslearn.datasets import CachedDatasets

seed = 0
np.random.seed(seed)
X_train, y_train, X_test, y_test = CachedDatasets().load_dataset("Trace")

n_queries = 2
n_neighbors = 4

knn = KNeighborsTimeSeries(n_neighbors=n_neighbors)
knn.fit(X_train)
ind = knn.kneighbors(X_test[:n_queries], return_distance=False)

plt.figure()
for idx_ts in range(n_queries):
    plt.subplot(n_neighbors + 1, n_queries, idx_ts + 1)
    plt.plot(X_test[idx_ts].ravel(), "k-")
    plt.xticks([])
    for rank_nn in range(n_neighbors):
        plt.subplot(n_neighbors + 1, n_queries,
                    idx_ts + (n_queries * (rank_nn + 1)) + 1)
        plt.plot(X_train[ind[idx_ts, rank_nn]].ravel(), "r-")
        plt.xticks([])


plt.suptitle("Queries (in black) and their nearest neighbors (red)")
plt.show()

# ######################################################
# Apply SVM on time series
# ######################################################


from tslearn.datasets import CachedDatasets
from tslearn.preprocessing import TimeSeriesScalerMinMax
from tslearn.svm import TimeSeriesSVC

np.random.seed(0)
X_train, y_train, X_test, y_test = CachedDatasets().load_dataset("Trace")
# visualization of the time series
plt.clf()
plot_series(X_train)
plt.show()
# Homogeneieze data
X_train = TimeSeriesScalerMinMax().fit_transform(X_train)
X_test = TimeSeriesScalerMinMax().fit_transform(X_test)
clf = TimeSeriesSVC(kernel="gak")
clf.fit(X_train, y_train)
print("Correct classification rate:", clf.score(X_test, y_test))

n_classes = len(set(y_train))
plt.clf()
plt.figure()
support_vectors = clf.support_vectors_
for i, cl in enumerate(set(y_train)):
    plt.subplot(n_classes, 1, i + 1)
    plt.title("Support vectors for class %d" % cl)
    for ts in support_vectors[i]:
        plt.plot(ts.ravel())

plt.tight_layout()
plt.show()
