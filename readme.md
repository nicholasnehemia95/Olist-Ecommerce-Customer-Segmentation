# Olist Customer Segmentation using RFM
![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/imagesNotebook/user-segmentation.png?raw=true)

## What is Customer Segmentation?
Market segmentation can be defined as dividing a market into distinct groups of customers, with different needs, characteristics or behavior, who might require separate products or who may respond differently to various combinations of marketing efforts (Kotler & Armstrong, 1999). </br>


## Why is Customer Segmentation Important??
### Optimation of Resources
 - Segmentation is critical because a company has limited resources, and must focus on how to best identify and serve its customers. Individual customer segments are characterized by a certain degree of within-group homogeneity that helps ensure that the members of a segment will respond in similar ways to marketing efforts. <br>
### Understanding customer positions and movement:
- By using this method, we can see which customers are potential customers and high value customers. Through Customer Relationship Management (CRM), we can hopefully convert potential Customers into high value customers, and focus our energy into high value customers. <br>
- Rerunning the model over periods of time, we can see the growth of each cluster, and evaluate whether the marketing strategies we have employed are effective or not.
### Increase Customer Retention
- By understanding the position of each customer , we can anticipate customer churn, and reduce the occurence. According to Amy Gallo from Harvard Business Review , Depending on what industry you’re in, acquiring a new customer is anywhere from five to 25 times more expensive than retaining an existing one. Furthermore, studies by Bain & Company, along with Earl Sasser of the Harvard Business School, have shown that a 5% increase in customer retention can lead to an increase in profits between 25 and 95%. 

## Recency , Frequency , Monetary Analysis
In this project , I am using a behavioral customer segmentation method, which is the RFM analysis.</br>
The RFM segments customers based on 3 main components : 
- **Recency** : How much time has elapsed since the customers last activity or transaction with the Brand?
- **Frequency** : How often has a customer transacted or interacted with the brand during a particular period of time? 
- **Monetary** : Also referred to as “monetary value,” this factor reflects how much a customer has spent with the brand during a particular period of time. 

## Why RFM Works
According to Arthur Hughes from the Database Marketing Institute, Customers who have purchased from you recently are more likely to respond to your next promotion than those whose last purchase was further in the past. This is a universal principle which has been found to be true in almost all industries: insurance, banks, cataloging, retail, travel, etc. It is also true that frequent buyers are more likely to respond than less frequent buyers. Big spenders often respond better than low spenders. <br>
By identifying these big spenders, we can focus our marketing efforts to these big spenders to make good returns.

## Goal of Project
Reducing marketing cost through targeted marketing based on RFM Analysis.

## Data Used
[Brazilian Ecommerce Public Dataset by Olist](https://www.kaggle.com/olistbr/brazilian-ecommerce)
Database Structure : <br>
![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/readme_images/database_structure.png?raw=true)

## Analysis of Olist 
![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/readme_images/olist_logo.png?raw=true) <br>
Olist is an online E-Commerce to connect shopkeepers and their products to the main marketplaces of brazil.
At the date of the last data within the dataset (17 September 2018) Olist has received it's series B Funding. 
According to [Investopedia](https://www.investopedia.com/articles/personal-finance/102015/series-b-c-funding-what-it-all-means-and-how-it-works.asp#series-b-funding), startups in the series B funding round typically have substantial userbase, and are now focusing on reaching a bigger market. Through RFM analysis, we can identify potential valuable customers and hopefully convert them into regulars.

## Data Processing
1. Import the required data from the csv, and merge the dataframes, then subset the columns needed. We need the order_id,customer_unique_id,customer_city,order_status,price,order_delivered_customer_date columns from the tables :orders,customers,order_items,order_payments.

2. Clean the dataset. For this project, we will use only data from Sao Paolo to reduce the dimensionality of the data, We choose Sao Paolo, because in the dataset the highest userbase comes from Sao Paolo.

3. Create the RFM data through Aggregation.

4. Scale the data into an RFM scale.Arthur Hughes uses Equal Binning Frequency in his RFM Matrix, but in this case this method is inappropriate , as most of the data in Frequency (Over 14000 data /16000 of total data) has a value of 1.  This will create multiple bins with the same value. So for this dataset , we used Quartiles of category, and for the Frequency category we use a special method using the mean instead of the median for the middle score. <br>

|   | Recency     | Frequency | Monetary    |
|:-:|-------------|-----------|-------------|
| 1 | x<-336      | x<2       | x<=42.9     |
| 2 | -335<x<-209 | 3         | 43<x<79.99  |
| 3 | -208<x<-112 | 4         | 80<x<149.81 |
| 4 | x>-112      | x>4       | x>149.81    |

5. After The RFM Matrix is created, we will then use K-Means Clustering. To determine the number of clusters , we shall use the Silhouette Score method and also the elbow Method for the validation metrics.<br>
A high Silhouette score shows that the clusters are well separated. Below is the result of the checking of the silhouette score. <br>

![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/imagesNotebook/sil_score.png?raw=true) <br>
From the results , we can see that high silhouette scores can be seen from values 2-5 Clusters. To ensure which value we will use, we will also employ the Elbow Method. <br>
![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/imagesNotebook/optimal_clusters_elbow_method.jpg?raw=true) <br>
From the elbow method , we can see that the elbow is located at the value of 4 clusters. The elbow method shows separation in each cluster. A high Inertia shows that the datapoints are not similar, and a low inertia means the data is more similar. In this analysis the elbow is located at 4 clusters. <br>
For this analysis, we shall use a value of 4 clusters, which is in line with the BCG Growth share matrix, which divides customers into 4 Groups.<br>

## Analysis of Clusters

Through the K-Means clustering, we have divided the data into 4 clusters with about equal amounts of data. <br>
![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/imagesNotebook/distribusi_kmeans.png?raw=true)

### Cluster Characteristics

| Rank | Recency | Frequncy | Monetary |
|:----:|---------|----------|----------|
| 1    | Class 3 | Class 2  | Class 1  |
| 2    | Class 2 | Class 1  | Class 2  |
| 3    | Class 1 | Class 3  | Class 0  |
| 4    | Class 0 |  Class 0 | Class 3  |

### Cluster Definitions Based on Characteristics

#### Cluster 0 (Low Value, Churned)
- Has low recency,frequency, and monetary Scores.
    - From those metrics, it can be assumed that Cluster 0 Customers have used Olist, but was not satisfied , thus stopped using it.
- Strategy for Cluster 0 Customers :
    1. Do not waste too much resources for this cluster, as according to [BCG Growth Share Matrix](https://www.bcg.com/about/our-history/growth-share-matrix),this cluster is in the pet, as it is hard to bring back churned customers, and also these customers have low monetary score.

#### Cluster 1 (High Value , Churned)
- Has High Monetary and Frequency Score, but low recency Score.
    - From the RFM Metrics, we can assume that the customer used to be a regular customer, but overtime stopped using the platform and has churned.
- Strategy for cluster 1 Customers :
    1. We can try to bring back these customers using special offers.
    2. Ask for feedback from them , to find out why they have stopped using the platform.
    3. See what marketing efforts have been used on these customers, and evaluate the mistakes.

#### Cluster 2 (High Value Active)
- Has high RFM scores.
    - From these metrics , we can assume that Cluster 2 Customers are the High Value Customers, and are our spenders. We must retain these customers.
- Strategy for cluster 2 Customers :
    1. Give them incentive to keep on using our platform, e.g : Loyalty Programs
    2. For these Customers , we can ask for reviews, so that they can influence others to use our platform too.
    3. As these customers have high monetary scores, we can consider not giving them too many discounts , as they are already loyal to the brand.

#### Cluster 3 (Potential Customer)
- Has low monetary and frequency scores, bu have high recency score.
    - From these metrics , It can be assumed that cluster 3 customers are recent users of the platform (Potential Customers). These customers should be given attention in hopes that they can be converted to High Value Customers.
- Strategy for Cluster 3 Customers :
    1. Create a loyalty program, in which will give incentive for higher value / more frequent transactions to build a habbit of using the platform. 

## Dashboard App

Using Flask, I have created a dashboard to see the analysis, and we can also predict new data on the dashboard. <br>
![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/readme_images/dashboardface.png?raw=true) <br>

![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/readme_images/dashboard_predict.png?raw=true) <br>

![alt text](https://github.com/nicholasnehemia95/JCDSAH_Final_Project/blob/main/readme_images/dashboard_result.png?raw=true)


## Resources : 
https://www.dbmarketing.com/articles/Art123.htm
https://www.bcg.com/about/our-history/growth-share-matrix


