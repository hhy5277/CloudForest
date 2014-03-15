import sys
from sklearn.datasets import load_svmlight_file

from sklearn.ensemble import RandomForestClassifier

from time import time

import numpy as np


def dumptree(atree, fn):
	from sklearn import tree
	f = open(fn,"w")
	tree.export_graphviz(atree,out_file=f)
	f.close()

# def main():
fn = sys.argv[1]
X,Y = load_svmlight_file(fn)

rf_parameters = {
	"n_estimators": 1,
	"n_jobs": 1,
	"max_features":1
}
clf = RandomForestClassifier(**rf_parameters)
X = X.toarray()

print clf

print "Starting Training"
t0 = time()
clf.fit(X, Y)
train_time = time() - t0
print "Training on %s took %s"%(fn, train_time)

if len(sys.argv) == 2:
	score = clf.score(X, Y)
	count = np.sum(clf.predict(X)==Y)
	print "Score: %s, %s / %s "%(score, count, len(Y))
else:
	fn = sys.argv[2]
	X,Y = load_svmlight_file(fn)
	X = X.toarray()
	score = clf.score(X, Y)
	count = np.sum(clf.predict(X)==Y)
	print "Testing Score: %s, %s"%(score, count)


# if __name__ == '__main__':
# 	main()
 	