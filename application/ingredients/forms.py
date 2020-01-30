from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators

class IngredientForm_new(FlaskForm):
    name = StringField("Ingredient name", [validators.InputRequired(message="Name required"), 
                                            validators.Length(min=2, message="Name must be atleast 2 characters long")])
    
    class Meta:
        csrf = False

class IngredientForm_modify(FlaskForm):
    newName = StringField("New name", [validators.Length(min=2, message="Name must be atleast 2 characters long")])
    bool_delete = SubmitField("Delete ingredient")
    
    class  Meta:
        csrf = False