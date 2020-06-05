from scipy.spatial import distance

def knn_predict(k, X_data, y_data):
    
    ## Write your code here
    
    predicted_class = []
    meow = 0
    
    for x in X_data:
        
        distances = []
        woof = 0
        
        for i in X_data:
            distances.append(distance.euclidean(X_data[meow], X_data[woof]))
            woof+=1
            
        dist = np.array(distances)
        sortedDist = np.argsort(dist)

        g = 0
        h = 0
        
        for u in range(0, k):
            l = sortedDist[u]
            if y_data[l]==1:
                g+=1
            elif y_data[l]==0:
                h+=1
                       
        if g > h:
            predicted_class.append(1)
            
        elif g < h:
            predicted_class.append(0)
    
        meow+=1

    return predicted_class
