from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.ingredients.models import Ingredient
from application.ingredients.forms import IngredientForm_new, IngredientForm_modify

@app.route("/ingredients/", methods=["GET"])
def ingredients_index():
    return render_template("ingredients/list.html", ingredients = Ingredient.query.all())

@app.route("/ingredients/new/")
@login_required
def ingredients_form():
    return render_template("ingredients/new.html", form = IngredientForm_new())

@app.route("/ingredients/", methods=["POST"])
@login_required
def ingredients_create():
    form = IngredientForm_new(request.form)
    
    if not form.validate():
        return render_template("ingredients/new.html", form = form)
    
    i_name = Ingredient(form.name.data)
    
    db.session().add(i_name);
    db.session().commit()
    
    return redirect(url_for("ingredients_index"))

@app.route("/ingredients/modify/<p_id>/", methods=["POST"])
@login_required
def ingredients_modify(p_id):
    ingredient = Ingredient.query.get(p_id)

    return render_template("ingredients/modify.html", ingredient=ingredient, form = IngredientForm_modify())

@app.route("/ingredients/update/<p_id>/", methods=["POST"])
@login_required
def ingredients_update(p_id):
    form = IngredientForm_modify(request.form)
    ingredient = Ingredient.query.get(p_id)
    
    if form.bool_delete.data == True:
        db.session.delete(ingredient)
        db.session.commit()
        return redirect(url_for("ingredients_index"))
    
    if not form.validate():    
        return render_template("ingredients/modify.html", ingredient=ingredient, form = form)
    
    ingredient.name = form.newName.data
    db.session().commit()
    
    return redirect(url_for("ingredients_index"))
    
