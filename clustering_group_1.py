import pandas as pd
import warnings
warnings.filterwarnings("ignore")
from scipy.spatial.distance import cosine

#read excel file for created tfidf vectors
tfidf_vectors = pd.read_excel('group_1_tfidf_vectors.xlsx', index_col=0)

#select centroids from given articles
tfidf_vectors['sports_centroid'] = tfidf_vectors['cleaned_9901_sports.txt_tfidf']
tfidf_vectors['food_centroid'] = tfidf_vectors['cleaned_9902_food.txt_tfidf']
tfidf_vectors['tech_centroid'] = tfidf_vectors['cleaned_9903_tech.txt_tfidf']
tfidf_vectors['science_centroid'] = tfidf_vectors['cleaned_9904_science.txt_tfidf']
tfidf_vectors['business_centroid'] = tfidf_vectors['cleaned_9905_business.txt_tfidf']
tfidf_vectors['politics_centroid'] = tfidf_vectors['cleaned_9906_politics.txt_tfidf']

#create empty distance matrix
distance_matrix = pd.DataFrame(columns=['sports_centroid','food_centroid','tech_centroid','science_centroid','business_centroid','politics_centroid'])

#fill distance matrix using scipy's cosine function
for col in tfidf_vectors.columns:
    if 'tfidf' in str(col):
        idx = str(col)
        sports_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['sports_centroid']),10)
        food_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['food_centroid']),10)
        tech_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['tech_centroid']),10)
        science_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['science_centroid']),10)
        business_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['business_centroid']),10)
        politics_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['politics_centroid']),10)
        distance_matrix.loc[idx] = [sports_dist, food_dist, tech_dist, science_dist, business_dist, politics_dist]



sports_cluster = []
food_cluster = []
tech_cluster = []
science_cluster = []
business_cluster = []
politics_cluster = []

for doc in distance_matrix.index:
    
    centroid = distance_matrix.loc[doc].idxmin()
    
    if 'sports' in str(centroid):
        sports_cluster.append(str(doc))
    
    if 'food' in str(centroid):
        food_cluster.append(str(doc))
        
    if 'tech' in str(centroid):
        tech_cluster.append(str(doc))
        
    if 'science' in str(centroid):
        science_cluster.append(str(doc))
        
    if 'business' in str(centroid):
        business_cluster.append(str(doc))
        
    if 'politics' in str(centroid):
        politics_cluster.append(str(doc))

# print("Iteration #1 sports cluster:")
# print(sports_cluster)

# print("\nIteration #1 food cluster:")
# print(food_cluster)

# print("\nIteration #1 tech cluster:")
# print(tech_cluster)

# print("\nIteration #1 science cluster:")
# print(science_cluster)

# print("\nIteration #1 business cluster:")
# print(business_cluster)

# print("\nIteration #1 politics cluster:")
# print(politics_cluster)


tfidf_vectors['sports_centroid'] = tfidf_vectors[sports_cluster].sum(axis=1)
tfidf_vectors['food_centroid'] = tfidf_vectors[food_cluster].sum(axis=1)
tfidf_vectors['tech_centroid'] = tfidf_vectors[tech_cluster].sum(axis=1)
tfidf_vectors['science_centroid'] = tfidf_vectors[science_cluster].sum(axis=1)
tfidf_vectors['business_centroid'] = tfidf_vectors[business_cluster].sum(axis=1)
tfidf_vectors['politics_centroid'] = tfidf_vectors[politics_cluster].sum(axis=1)


#second iteration of clustering
distance_matrix = pd.DataFrame(columns=['sports_centroid','food_centroid','tech_centroid','science_centroid','business_centroid','politics_centroid'])


for col in tfidf_vectors.columns:
    if 'tfidf' in str(col):
        idx = str(col)
        sports_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['sports_centroid']),10)
        food_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['food_centroid']),10)
        tech_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['tech_centroid']),10)
        science_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['science_centroid']),10)
        business_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['business_centroid']),10)
        politics_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['politics_centroid']),10)
        
        distance_matrix.loc[idx] = [sports_dist, food_dist, tech_dist, science_dist, business_dist, politics_dist]
        


sports_cluster2 = []
food_cluster2 = []
tech_cluster2 = []
science_cluster2 = []
business_cluster2 = []
politics_cluster2 = []

for doc in distance_matrix.index:
    
    centroid = distance_matrix.loc[doc].idxmin()
    
    if 'sports' in str(centroid):
        sports_cluster2.append(str(doc))
    
    if 'food' in str(centroid):
        food_cluster2.append(str(doc))
        
    if 'tech' in str(centroid):
        tech_cluster2.append(str(doc))
        
    if 'science' in str(centroid):
        science_cluster2.append(str(doc))
        
    if 'business' in str(centroid):
        business_cluster2.append(str(doc))
        
    if 'politics' in str(centroid):
        politics_cluster2.append(str(doc))

print(sports_cluster == sports_cluster2)
print(food_cluster == food_cluster2)
print(tech_cluster == tech_cluster2)
print(science_cluster == science_cluster2)
print(business_cluster == business_cluster2)
print(politics_cluster == politics_cluster2)
