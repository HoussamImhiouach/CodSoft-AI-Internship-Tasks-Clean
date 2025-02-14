# Movie Recommendation System

## Overview

This project suggests movies based on their **genre similarity**. The system uses **Content-Based Filtering**, comparing genres to recommend similar movies. The dataset used is **MovieLens**, which contains real movie ratings.

## How It Works

1. **TF-IDF Vectorization**
   - Transforms **movie genres into numerical data**.
2. **Cosine Similarity**
   - Measures how similar two movies are.
3. **GUI Interface**
   - Users enter a movie title, and similar movies are displayed.

## Technologies Used

- **Python**
- **Pandas & NumPy (Data Handling)**
- **Scikit-Learn (Machine Learning)**
- **Tkinter (GUI)**
- **TF-IDF (Feature Extraction)**
- **Cosine Similarity (Recommendation Algorithm)**

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-Internship-Tasks.git
   cd AI-Internship-Tasks/movie-recommendation-system
   ```
2. **Install dependencies:**
   ```bash
   pip install pandas numpy scikit-learn
   ```
3. **Run the script:**
   ```bash
   python recommendation_system_gui.py
   ```

## Usage Guide

1. Enter a movie title in the GUI.
2. Click **"Get Recommendations"**.
3. The system finds **similar movies** based on their genre.

## Expected Output

- **User enters:** `"Toy Story"`
- **System recommends:** `"A Bug's Life", "Finding Nemo", "Shrek"` (or other animated movies)

## Future Improvements

- Add **Collaborative Filtering** (User-based recommendations).
- Allow users to **rate movies** for better suggestions.
- Integrate **a larger dataset**.

## License

This project is open-source and available under the MIT License.
