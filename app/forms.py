from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired


class NestRequestForm(FlaskForm):
    items_quantity = StringField("Items quantity (comma separated, order same as uploaded files):",
                                 validators=[DataRequired()])
    bin_size_x = IntegerField("Bin size (x):", validators=[DataRequired()], default=3000)
    bin_size_y = IntegerField("Bin size (y):", validators=[DataRequired()], default=1000)
    timeout = IntegerField("Timeout (in seconds):", validators=[DataRequired()], default=10)
    submit = SubmitField("Submit")
