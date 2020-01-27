from application import app, db
from flask import render_template, request, redirect, url_for
from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm

@app.route("/ingredients/", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients = Ingredient.query.all())

@app.route("/ingredients/new/")
def ingredients_form():
    return render_template("ingredients/new.html", form = IngredientForm())

@app.route("/ingredients/", methods=["POST"])
def ingredients_create():
    form = IngredientForm(request.form)
    
    if not form.validate():
        return render_template("ingredients/new.html", form = form)
    
    i_name = Ingredient(form.name.data)
    
    db.session().add(i_name);
    db.session().commit()
    
    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/modify/<p_id>/", methods=["POST"])
def ingredients_modify(p_id):
    ingredient = Ingredient.query.get(p_id)

    return render_template("ingredients/modify.html", ingredient=ingredient)

@app.route("/ingredients/update/<p_id>/", methods=["POST"])
def ingredients_update(p_id):
    newName = request.form.get("newName")
    ingredient = Ingredient.query.get(p_id)
    
    ingredient.name = newName
    db.session().commit()
    
    return redirect(url_for("ingredients_index"))
    
