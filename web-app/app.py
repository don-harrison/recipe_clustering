from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
columns = {0: 'name', 
            1: 'id', 
            2: 'minutes', 
            3: 'contributor_id', 
            4: 'submitted', 
            5: 'tags',
            6: 'nutrition', 
            7: 'n_steps', 
            8: 'steps', 
            9: 'description', 
            10: 'ingredients',
            11: 'n_ingredients'}
@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/search/<int:column>/<string:value>')
def search(column, value):
    #return data associated with page number
    return food_recipe_df[food_recipe_df[columns[column]].str.contains(value, case=False, na=False)].values.tolist()

@app.route('/data/<int:page>')
def data(page):
    #return data associated with page number
    return food_recipe_df.iloc[page*10:(page*10) + 10].values.tolist()

if __name__ == '__main__':
    food_recipe_df = pd.read_csv('./Food Recipes Dataset/RAW_recipes.csv')
    food_recipe_df = food_recipe_df.where(pd.notnull(food_recipe_df), None)
    increment_amount = 10
    page = 0
    total_pages = len(food_recipe_df)//increment_amount
    app.run(debug=True)