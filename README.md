# Picked For Me

This README.md file will serve as a roadmap to this repository. The repository is open and available to the public.

Directories and files to be aware of:

1. An “environment.yml” file that contains the packages necessary to running the executables.

2. An src/ directory that contains a .py module.
    - In the root directory of this folder on your local machine, in your terminal please run 'pip install -e .' to allow the notebooks to access our functions. This will run our 'setup.py' file in the root directory.
3. A notebooks/ directory that contains two Jupyter notebooks: a. A data exploration notebook (EDA_and_data_reduction) b. A modeling notebook (implementation)

4. A data/ directory containing four data files a. Due to GitHub upload restrictions, these are included as .gitignore files. They are, in brief:   
    - The word2vec model 
    - The TF-IDF model 
    - The cosine similarity matrix 
    - The recipe data

5. One “Executive Summary” slideshow PDF available as “Presentation-MVP.pdf” 

Data: The data files described above can be found on https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions. An account setup is required for download.

Methodology: After performing an initial EDA of the dataset, we build two models to predict a recipe from a user’s choice of food ingredients.      
   - The first model used word2vec for a recipe ingredient to user ingredient comparison. 
   - The second model used a TF-IDF vectorizer for a recipe to recipe comparison. 

Result: The functionality was used in the creation of Picked For Me, an app that aids picky eaters find diverse recipes. The github repo can be found here - https://github.com/karenkathryn/picked4me-app. 
