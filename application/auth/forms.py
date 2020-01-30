from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators

class AuthForm_login(FlaskForm):
    username = StringField("Username", [validators.InputRequired(message="Username required")])
    password = PasswordField("Password", [validators.InputRequired(message="Password required")])
    
    class Meta:
        csrf = False

class AuthForm_create_account(FlaskForm):
    name = StringField("Name", [validators.InputRequired(message="Name required"), 
                                validators.Length(min=2, message="Name must be atleast 2 characters long"),
                                validators.Length(max=144, message="Name can't be longer than 144 characters")])
    username = StringField("Username", [validators.InputRequired(message="Username required"), 
                                        validators.Length(min=2, message="Username must be atleast 2 characters long"), 
                                        validators.Length(max=144, message="Username can't be longer than 144 characters")])
    password = PasswordField("Password", [validators.InputRequired(message="Password required"), 
                                            validators.Length(min=4, message="Password must be atleast 4 characters long"), 
                                            validators.Length(max=144, message="Password can't be longer than 144 characters"),
                                            validators.EqualTo("confirmation", message="Passwords must match")])
    confirmation = PasswordField("Confirm password")
    submit = SubmitField("Create account")
    
    class Meta:
        csrf = False