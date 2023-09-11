# Movie Recommendation Model
<p align="center">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlhbm5-jNGTy-WdvLk2Jk6qFkhqn__ERYOaEJdq3WzkxQgZBFgtojzp2eASe6lOdo-iVyWkhutwwwKTXh1o084rcZshjnDcN8xqNWiTW9jONpY5wTjxch75vLsOF5WHnziG-42wShyvt375fXGOGauYHhoxlpoChUK-3OuKiM9sRTJ-nHoFXFLjLIZ/w400-h229/H95B.gif" width="600" height="449">
</p>


# Tools & Technologies Used
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisMIVHbKjYAF3lQvTF9suc_QjNLS-SoQuykTbyjoZmyfoM2C9V5vsW12Dvt-hOsUT8GrfJ1aWuGPdbf9pOeZD204T_VUT3G1ckiy5OzxOaAVJngclB_H8IY6vzLiRti4qoFjIsZ8CImcLKrs4sM9BLY-t6ynUsyZ0Ly7ZXpT3j26hgWYocU0ioFbEY/s16000/Untitled%20design%20(6).png)

# Objective
The Movie Recommendation Model is a machine learning-based system that takes a movie title as input and provides 5 movie recommendations based on it. Additionally, the model also offers direct streaming links for these recommended movies, leveraging publicly available sources. The model utilizes a dataset from Kaggle, which is limited to movies released up until the year 2015.


# OUR APPROACH FOR THE PROJECT
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJyS7DvGnjb42Oaeys03VdGnRG5lKlzGtjA3VkkYLHDiByno0dkOmIeba1Qhx_FuR9vG3TkU3v2iAFnNEzGdTEUB-fEP3mDK63ZuyiZDSV2R3bA6loiqJsBbRxIaA8q7cXBXiIcrwvAAW59i7mBYRQLTSLlMQ21MydHgACdP75zlu4nN1DQqzEgS4s/s16000/cht.png)

# User's Manual
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/fc9f0b0b-ce13-4f24-946b-629e803315dd)



# Data Preparation
# Data Scarpping (Snapshots)
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/1e286d03-131f-4665-88b0-c5cf6a801b36)

----------------------------------------------------------------------------------------------------------------------
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/063e6947-46c3-4e1d-a306-8f4168a3e9a0)


# Data Cleaning (few code snippets)
1. Null Handling & Remove Noise Values
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/df0a8a1f-c73b-478b-b7a8-1523afb43c1e)


3. Change Data type of Consultation Column
   ![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/b0833efa-fb9d-4b76-80b1-f64ab82fb2fb)
   
   
5. In the data sets Location column and city column both have city name which is not generally required. so here we will split the column using ',' delimeter and then remove the column contain city name.
   ![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/dc2f6215-8f87-4e6e-89bb-9a958b9b3476)
   

# Exploratory Data Analysis(EDA)

# Number of Doctors by each City
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/a59d9f4e-ffdb-4082-be88-8a6dff9da469)

------------------------------------------------------------------------------------------------------------------------

# Count  of Doctors in each Speciality
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/11079f23-5985-46d7-a25c-7913f54395fb)



-------------------------------------------------------------------------------------------------------------------------

# Speciality wise Fees Analysis
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/3120eb36-d8f8-4fe7-9113-ee97cb757565)


--------------------------------------------------------------------------------------------------------------------------

# Percentage of  Doctors avilable in each of the city
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/c29cc699-51b6-47e8-9b0c-30814cb4e045)


-------------------------------------------------------------------------------------------------------------------------

# Correlation between the Variables By using Heatmap
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/b25da979-d418-46a0-8614-50963db2ba7a)


-------------------------------------------------------------------------------------------------------------------------

# Doctors Having Maximum number of Specialization
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/43d79d51-d358-444d-918e-258b987c37ba)



-------------------------------------------------------------------------------------------------------------------------

# Distribution of  year of experience
![image](https://github.com/Sudhansu352010/Doctor-Fee-Prediction/assets/131376814/e7aaa642-9722-4285-8638-63fa1bc0421b)



# Key Insights
1. Most of the doctors have 13 to 15 years of experience.

2. Cities like Bangalore have a higher percentage of doctors, accounting for approximately 40.23%.

3. The majority of doctors specialize in Dentistry (1460), while the fewest doctors specialize in Chiropractic (7).

4. Bangalore has the highest number of doctors compared to Delhi and Mumbai.

5. In each city, the number of dentists is higher than other specialties because their consultation fees are completely free.

6. Neurosurgeons and Ophthalmologists charge high consultation fees, while specialties like Dentistry, Dermatology, Gynecology/Obstetrics, Infertility Specialists, Physiotherapy, and Dietetics/Nutritionists offer almost free consultations.

7. Locations like Saket in Delhi have the highest concentration of doctors.

8. The most common degree among doctors is BDS.
