# Movie Recommendation Model

The Movie Recommendation Model is a machine learning-based system that takes a movie title as input and provides 5 movie recommendations based on it. Additionally, the model also offers direct streaming links for these recommended movies, leveraging publicly available sources. The model utilizes a dataset from Kaggle, which is limited to movies released up until the year 2015.

## Features

- Recommends 5 movies similar to the input movie.
- Provides streaming links for the recommended movies (where publicly available).
- Utilizes a machine learning algorithm to make recommendations.
- Trained on a Kaggle dataset up to the year 2015.

## How It Works

The Movie Recommendation Model employs a machine learning algorithm to analyze the characteristics of movies and their relationships. Here's a high-level overview of how it works:

1. **Input Movie**: Provide the title of a movie you're interested in.

2. **Processing**: The model processes the input movie title and extracts relevant features or attributes from the dataset.

3. **Similarity Analysis**: The model calculates the similarity between the input movie and all other movies in the dataset. This similarity score is based on various features like genre, actors, directors, etc.

4. **Recommendations**: The model selects the top 5 movies with the highest similarity scores as recommendations.

5. **Streaming Links**: For each recommended movie, if there are publicly available streaming links, the model provides those links for easy access.


## Dataset

The Movie Recommendation Model was trained on a dataset sourced from Kaggle, containing information about movies up to the year 2015. The dataset includes details such as movie titles, genres, actors, directors, release years, and more. Please note that the recommendations provided by the model are influenced by the data available in this dataset.

## Limitations

- The recommendations are based on data available only up to the year 2015.
- The model's accuracy and relevance depend on the quality and completeness of the training dataset.
- Streaming link availability is subject to change and might not always be accurate or up-to-date.

## Contributing

Contributions are welcome! If you'd like to improve the model, enhance the recommendations, or add new features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
