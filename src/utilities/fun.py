import sklearn.metrics
import pandas as pd



def length_recipe_list(my_recipe_list):
  """This is a function that limits the length of the returned recipe list"""
  if len(my_recipe_list) <= 5:
    my_range_value = len(my_recipe_list)
    return my_range_value
  else:
    my_range_value = 5
    return my_range_value



def get_recipes(w1, w2, number_picked, model, df_tfidf, df_similarity):
    """The function that gets recipes from a list of ingredients."""
    try:
        result = model.wv.most_similar(positive=w1, negative=w2)

        my_food_0 = result[0][0]
        my_food_1 = result[1][0]

        choice = number_picked

        if choice == 1:    
            # USER -- Choose 1 result
            my_recipe_list = df_tfidf[(df_tfidf[my_food_0] > 0)].index.tolist()  
            if len(my_recipe_list) > 0:
                print(f'Here are some recipes with {my_food_0}:')
            for item in my_recipe_list:
                my_range_value = length_recipe_list(my_recipe_list)
                for i in range(my_range_value):
                    print(f'https://www.food.com/recipe/{my_recipe_list[i]}')

        else:
            # USER -- Choose 2 results
            # This set of 2 ingred tests this path
            # my_food_0 = "'chocolate'"
            # my_food_1 = "'milk'"
            my_food_list = [my_food_0, my_food_1]    

            my_recipe_list = df_tfidf[(df_tfidf[my_food_list[0]] > 0) & 
                                        (df_tfidf[my_food_list[1]] > 0)].index.tolist()  
            if len(my_recipe_list) > 0:
                print(f'Here are some recipes with {my_food_list}:')
            for item in my_recipe_list:
                my_range_value = length_recipe_list(my_recipe_list)
                for i in range(my_range_value):
                    print(f'https://www.food.com/recipe/{my_recipe_list[i]}')


    except KeyError:
        # To do:
        # Case: the user entered an ingredient that is not in the BOW from corpus
        print(f'There are no recipes with this ingredient set.')
        

    else:
        # Case: there are no recipes with the 2 chosen ingredients, so find something similar
        print(f'There are no recipes with this ingredient set. Here are some suggestions:')
        my_food_2 = result[2][0]
        my_recipe_list = df_tfidf[df_tfidf[my_food_2] > 0].index.tolist()
        list_secondary = []
        for id_ in my_recipe_list:
            # use the tf-idf cosine similarity to find something similar
            for column_id in df_similarity.columns:     
                # check if the similarity is between values   
                if df_similarity.loc[id_,  column_id] > .01:
                    value = df_similarity.loc[id_,  column_id]
                    list_secondary.append([column_id, value])
                
            pri_sec_values_df = pd.DataFrame(list_secondary, columns=['secondary', 'cs_value'])
            # sort by cosine similarity value 
            pri_sec_values_df = pri_sec_values_df.sort_values('cs_value')
            if len(pri_sec_values_df) > 4:
                pri_sec_values_df = pri_sec_values_df.tail(5)
            for i in range(5):
                sec_id = int(pri_sec_values_df.iloc[i]['secondary'])
                print(f'https://www.food.com/recipe/{sec_id}')

