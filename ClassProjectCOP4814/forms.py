
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class ColorForm(FlaskForm):
    # Field 1: StringField for the user to input a HEX color
    hex_color = StringField(
        'Main Color (HEX code)',
        validators=[
            DataRequired(message="A main color is required."),
            Length(min=6, max=6, message="HEX code must be exactly 6 characters (e.g., 0099FF)."),
            Regexp(r'^[0-9a-fA-F]{6}$', message="Invalid HEX formatting. You can only use the numbers 0-9 and letters a-f.")
        ],
        description="Please enter a 6-digit hex code. Do not include the hashtag (#), e.g., 0099ff."
    )

    # Field 2: SelectField for the color palette mode
    scheme_mode = SelectField(
        'Color Palette Type',
        choices=[
            ('monochromatic', 'Monochromatic: Colors that have the same tone'),
            ('analogic', 'Analogous: Colors that are next to each other on the color wheel'),
            ('triad', 'Triadic: Three evenly spaced colors'),
            ('complement', 'Complementary: Opposite colors that still fit well together'),
        ],
        validators=[DataRequired()]
    )

    # Field 3: SelectField for the number of colors in the palette
    num_colors = SelectField(
        'Number of Colors in Palette',
        choices=[(str(i), str(i)) for i in range(2, 7)],  # outputs 2 to 6 colors
        default='5',
        validators=[DataRequired()]
    )

    # Submission button
    submit = SubmitField('Generate Color Palette ')