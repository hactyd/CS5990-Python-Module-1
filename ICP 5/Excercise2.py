import numpy as np
import matplotlib.pyplot as plt
import random


def create_cluster(X, centroid_pts):
    cluster = {}
    # read about lambdas and np.linalg.form
    # https://stackoverflow.com/questions/32141856/is-norm-equivalent-to-euclidean-distance ,
    # here we are using order 1 to calculate normalized distance
    for x in X:
        value = \
        min([(i[0], np.linalg.norm(x - centroid_pts[i[0]])) for i in enumerate(centroid_pts)], key=lambda s: s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


def calculate_new_center(cluster):
    keys = sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k], axis=0)) for k in keys])
    return newmu


def matched(new_centroids, old_centroids):
    return (set([tuple(a) for a in new_centroids]) == set([tuple(a) for a in old_centroids]))


def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.
    centroids_old = np.random.randint(N, size=K)
    centroids_old_pts = np.array([X[i] for i in centroids_old])

    print("old :", centroids_old)
    print(centroids_old_pts)

    cluster_info = create_cluster(X, centroids_old_pts)

    print("Initial cluster information:")
    print(cluster_info)

    centroid_new_pts = calculate_new_center(cluster_info)
    print("new :", centroid_new_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    plot_cluster(centroids_old_pts, cluster_info, itr)
    while not matched(centroid_new_pts, centroids_old_pts):
        itr = itr + 1
        centroids_old_pts = centroid_new_pts
        cluster_info = create_cluster(X, centroid_new_pts)
        plot_cluster(centroid_new_pts, cluster_info, itr)
        centroid_new_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    plot_cluster(centroid_new_pts, cluster_info, itr)
    return


def plot_cluster(mu, cluster, itr):
    color = 10 * ['r.', 'g.', 'k.', 'c.', 'b.', 'm.']
    print('Iteration number : ', itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:, 0], mu[:, 1], marker='x', s=150, linewidths=5, zorder=10)
    plt.show()


def init_graph(N, p1, p2):
    X = np.array([(random.uniform(p1, p2), random.uniform(p1, p2)) for i in range(N)])
    return X


def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    # no. of students in the university

    N = int(input('Data Points:'))
    #

    K = 3  # no.of sizes i Need
    #
    p1 = 6.2  # maximum height
    p2 = 5  # minimum Height

    X = init_graph(N, p1, p2)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()
    temp = Apply_Kmeans(X, K, N)

if __name__ == '__main__':
    Simulate_Clusters()