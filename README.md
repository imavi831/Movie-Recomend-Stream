# Movie Recommendation Model
<p align="center">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlhbm5-jNGTy-WdvLk2Jk6qFkhqn__ERYOaEJdq3WzkxQgZBFgtojzp2eASe6lOdo-iVyWkhutwwwKTXh1o084rcZshjnDcN8xqNWiTW9jONpY5wTjxch75vLsOF5WHnziG-42wShyvt375fXGOGauYHhoxlpoChUK-3OuKiM9sRTJ-nHoFXFLjLIZ/w400-h229/H95B.gif" width="600" height="449">
</p>

# Objective
The Movie Recommendation Model is a machine learning-based system that takes a movie title as input and provides 5 movie recommendations based on it. Additionally, the model also offers direct streaming links for these recommended movies, leveraging publicly available sources. The model utilizes a dataset from Kaggle, which is limited to movies released up until the year 2015.

# Problem aimed to solve 

1. **Information Overload:** With the vast amount of movie choices available, users often struggle to narrow down their options and find movies that match their preferences. This problem aims to simplify the selection process by providing personalized movie recommendations.

2. **Discoverability:** Many great movies often go unnoticed because users are unaware of their existence. This project addresses discoverability issues by recommending movies that users might not have otherwise encountered.

3. **Streamlining the Streaming Process:** Finding legitimate streaming links for movies can be time-consuming and frustrating. This objective seeks to simplify the process by providing direct streaming links to recommended movies, making it easier for users to access and enjoy their chosen films.



# Tools & Technologies Used
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisMIVHbKjYAF3lQvTF9suc_QjNLS-SoQuykTbyjoZmyfoM2C9V5vsW12Dvt-hOsUT8GrfJ1aWuGPdbf9pOeZD204T_VUT3G1ckiy5OzxOaAVJngclB_H8IY6vzLiRti4qoFjIsZ8CImcLKrs4sM9BLY-t6ynUsyZ0Ly7ZXpT3j26hgWYocU0ioFbEY/s16000/Untitled%20design%20(6).png)


# OUR APPROACH FOR THE PROJECT
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhJyS7DvGnjb42Oaeys03VdGnRG5lKlzGtjA3VkkYLHDiByno0dkOmIeba1Qhx_FuR9vG3TkU3v2iAFnNEzGdTEUB-fEP3mDK63ZuyiZDSV2R3bA6loiqJsBbRxIaA8q7cXBXiIcrwvAAW59i7mBYRQLTSLlMQ21MydHgACdP75zlu4nN1DQqzEgS4s/s16000/cht.png)

# User's Manual
</head>
<body>
	<table>
		<thead>
			<tr>
				<th>Files</th>
				<th>Description</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>&nbsp;Datasets</td>
				<td>This folder contains TMDB dataset used<br>for model creation in .zip format&nbsp;</td>
			</tr>
			<tr>
				<td>Data Cleaning&nbsp;</td>
				<td>This folder contain .ipynb file which is used&nbsp;<br>to clean data and data pre-processing</td>
			</tr>
			<tr>
				<td>Streamlit Application</td>
				<td>This folder contains app.py file based on&nbsp;<br>Streamlit interface</td>
			</tr>
			<tr>
				<td>&nbsp;Webpage</td>
				<td>This folder contains files for model and <br>webpage integration</td>
			</tr>
			<tr>
				<td>&nbsp;Final Presentation</td>
				<td>This folder contains .pptx file for Project Presentation</td>
			</tr>
      <tr>
				<td>README.MD</td>
				<td>This is Readme file of the project</td>
			</tr>
		</tbody>
	</table>
</body>
</html>

# Data Preparation

# Data Cleaning and Feature selection (few code snippets)
1. Null Handling & Remove Noise Values
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixT6rNJYG6Hp0UDCN5Uh5ai3h7GTxEm1TBqEPK0AkJwwPOUjwTA3GA8VE65mjSknVCkk1nthaQTE7jESxo1_cw7Zfdl99EflH3rwszB8_2ULNUkSaxC8OTOOxpMzAbz4TBc8RigvxyOvNEybb5PUx-jCNlZdrPXDTTv-Vd3bLZIJb_ix9oVVNn347V/s16000/11zon_cropped.png)
In this step, we address missing values and eliminate noisy data points from our dataset. Proper data cleaning is essential to ensure the accuracy of our analysis.


3. Create Function to Extract genres from Table
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUQXMtit-FTp5vVa7otvLCHjfW-WG2PiI0ZTq_i780zViQpvwt-U1uvO0SMemDG1HD_cJn0M8ZkejlecsndZEbqvMqCQ7XmKJbrTmouLtDV6vA6C3UG-YMRlWDveb2Ie6CZ0NtgUZ48EduMoC73-dCPD605ygljy-LvttkkyN6Lj7XhGAst9VXXUfN/s16000/11zon_cropped%20(1).png)
The data is in Disctionary format we only need text we will uses this simple function to extract genre as text from the column
   
4. The crew column has name of all the crew who worked on the movie, but only directors play bigger role in movie selection so extracting Directors name from
   crew column
   ![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLThdR8TEyx65KW1Gjk_2UmxhrvmN0AFrcUrWBwDm9r_1arSroyqYP10pVhfZjbW8cUc9toEpd7gtvxGhgI9mTwxflmmEtdD0WfxqgDUcSHCVvOGHtpuFB2t4I4-k6cNOVIx2WwIHNOXrfqhEvwmMfxX-Y5Lss49BTYdiB9PBXZRHBku5vdPxF1TnK/s16000/11zon_cropped%20(2).png)
   While the crew column contains information about everyone involved in the movie, we're primarily interested in directors as they play a significant role in movie selection. We've developed a process to extract director names from the crew column.

6. Cast column has name of all the actors who worked on the movie but we will only use top 3 actors since they are primary character that influence people choice
   ![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiF4QWuo6OKGKCNim5qqogT1tEXJydzsAMNbXmMCRJH9eGelEDw4s_LQYVq6ZsNb8DRxG-oFNGK3U-hS0V8BaqqP5dqczO__aSRNVl2Hs2efpE2NQRnsgUb6N-fOvEcKwbgWSEAa3c8OPlu24hdks6gW5766jbEDEN8WHfXRETAvhNHVzCE1cT6KqGJ/s16000/11zon_cropped%20(3).png)
   For our analysis, we focus on the top 3 actors in each movie. These actors are often the primary influencers of people's movie choices.

# Model Creation

# Using Cosine vectors to create vectors for all the movies available in dataset
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8sHX9b4g0xKIbxuN4bM-3Om8lFlvOyxJL91uP7j8Qtw84N8EyerlnODqoWmXbP8Vmvg0TBZyacFPA1g0Si9LmW5BRRzB160DIaXz66NWqfuweXEU5NWPZIVthaMX_4Pt83T4kjoJDCRNJVxBI3kgKr1HS5q7OY1CmcOh_Vk-LaBjNGeGyA2yOwZZe/s16000/11zon_cropped%20(4).png)
We use cosine vectors to represent all the movies in our dataset. This vectorization method helps us compare and analyze movies efficiently.

------------------------------------------------------------------------------------------------------------------------

# Used Nltk Library to normalize similar words for better model accuracy 
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh5Pf7j4kDF-DSKZ86Q-zNIz7ykdT1VQOddTZfsZ_kFuOOWA1XqNISiDeDb3en1k99IWoEwh1ehO6lAMPLIs6XnKxO-C-Jl079tzPC1BKPplpHpA0LdUJ31NwRKKDlrD_d5Pr4jDzgYWy805PimvxftrjaHvZQR5GtlugMNYz12Wde8qMgxL15aSyzb/s16000/11zon_cropped%20(5).png)
To improve the accuracy of our model, we employ the NLTK library for text normalization. This process normalizes similar words, reducing noise in our data and enhancing model performance.

-------------------------------------------------------------------------------------------------------------------------

# Pickle library to store Model 
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgG90vR7M-LM7r35_xfjRcn9bFSX9VC0Tp3W6rHpWOg0qW3-Oklx32kkUhUeMksWUhWvbM7g-kcfko0JyiytQOAZ4-8aFG9GCHL11G3uhpuKlSBhE6FSSivSe3j7e-QL7q8Ntlo_AUWkrNc0qSi5C74xtMa_LdNCGT6FdP2BsmiY2fKJAAz4JYOw_4A/s16000/11zon_cropped%20(6).png)
We use the Pickle library to store our model. This allows us to save the trained model and load it for future use without the need to retrain it every time.
 

# Streamlit Application
# Code[snapshot]
![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiMEfB2sFlTxZnZNUrx0g3qOGfz5lYLn1h25M47w_kYk6nASlOdtDE6Hfj-s_qPlfbDhadtWDg_lRz0KP9lCQk9_gJPUX8FA1c8VerMW7VspImRGBJ5fSkcZqSVOb5DjuqHI9Pz5s27hj_f6bbomp7De6lZQ7nHnKNkWQRmEfjsSO156jr_a5u4gCXn/s16000/11zon_cropped%20(7).png)
Our Streamlit application is the user interface for interacting with our movie recommendation system. It provides a user-friendly experience for users to discover movies.

# Code Structure
- Importing Necessary Libraries: The code starts by importing required libraries such as Streamlit, Pandas, Pickle, and Requests for web scraping and web API interaction.

- Fetching Movie Posters: There's a function fetch_poster(movie_id) that fetches movie posters from The Movie Database (TMDb) API. It requests movie data, extracts poster 
  paths, and constructs full image URLs.

- Movie Recommendation Function: The recommend(mov) function recommends movies based on user input. It calculates movie similarities using a pre-computed similarity matrix 
  and returns a list of recommended movies along with their posters.

- Loading Data and Model: The code loads movie data and a pre-trained similarity matrix from Pickle files. These data are essential for the recommendation process.

- Streamlit Web Application: It creates a Streamlit web application with a title and a select box for users to choose a movie. Users can click the "Recommend" button to -  
  get movie recommendations.

- Displaying Recommendations: The recommended movies are displayed in columns, with each column containing a movie title, an image poster,and a button to go to the movie 
page. The user can click on a button to access more information about the recommended movie.

# Webpage
1. using a virtual environment is must along with streamlit running as administrator.
2. Replace TMDB api key by generating your own api key [it's free].
3. initiate the app using the command in terminal "Streamlit run app.py".
4. use the local url to open the webpage

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh4vCEtjm0ki54ZsFXME6x4XJ5KgRjouazXy7w4TbDJVVQx9gZyAAps_GiugSm2OJleyQaUCkKRJb8JYCXT3619CijOTWb_mPm-JJqgB232Moy7hAuwumqURKTuWPwAiDxsslkkyhtyMhbbSKpQSHyUrPOsvhZEc4-wtp7fAINCQWj9CHh2Slx5R2WC/s16000/Untitled%20design%20(4).png)

   
5. search for your favourite movie and click on recommend

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtswTl-SCfRRY0ScWc-rrparm4wsDEm5wykCMBMebu1vvRvQZtNcDb7R3FXPGg2_7ZwRqqfAyvWQlxAfjctrayYfmFhoiORmOvYXJG1obqKZBGVo6OnZWZ5N4RZkgusNs2K7-I18t44LwOTycdTLLz_3538dHJRX9bX3ZBbBjJUpr96fKt9_TtmgTc/s16000/movie%20main.png)


6. Click on Go to movie button to get streaming link

![image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfJZk-e0qUM5dAIiqOH1oCd_Bxrb9llBpXddXmb237_QBV0aTG5bKRxvZB5dFw3ObhB7AHzDMsifJIK03TLJfOPMYgdynRhHXaG5URs8p_Ddyzoq_AUBAHKJDM57eq1nBnVIN_sREorsaOOxwS1WsPan-WlMslOBD_GuF-KwExdVkXtmIoK27uTRZu/s16000/Untitled%20design%20(5).png)

# ***Problems Faced***

1. Finding a movie streaming API that has no geo blocks.
2. Using Streamlit; as it has been updated, the syntax has changed, and old tutorials are no longer relevant.
3. Integration of the model with the Streamlit application.
4. TMDB has limited the API usage to 10,000 requests per month, so if usage exceeds that, you will need to purchase credits.
5. The model is quite large in size; as you add more movies to it, the data will grow exponentially, and the program will slow down.


# ***Future Scope***

1. The dataset used is limited to 2016 data; it could be updated to provide new movie recommendations, as the streaming API is regularly updated by the developers.
2. A separate section for TV shows could also be added for TV show recommendations.
3. More regional movies can be included, and a combination of multiple APIs can be used to obtain streaming links.
4. You can even create your own streaming API and monetize it with ads on the video; this model will automatically fetch all the streaming links.

