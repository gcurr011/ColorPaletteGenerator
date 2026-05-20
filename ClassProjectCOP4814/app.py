import requests
from flask import Flask, render_template
from forms import ColorForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '6483095'  # Required for Flask-WTF CSRF protection

# API endpoint for generating color palettes
COLOR_API_URL = "https://www.thecolorapi.com/scheme"

def generate_description(mode):
    # Return a description based on the selected color scheme mode.
    descriptions = {
        'monochromatic': "Monochromatic palettes use different shades and tones of the main color given.",
        'analogic': "Analogous palettes use colors next to each other on the color wheel.",
        'triad': "Triadic palettes use three evenly spaced colors on the color wheel.",
        'complement': "Complementary palettes use opposite colors on the color wheel.",
    }
    return descriptions.get(mode, "This palette was generated using color theory principles.")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ColorForm()

    if form.validate_on_submit():
        # Extract user input from the form
        hex_color = form.hex_color.data
        mode = form.scheme_mode.data
        count = int(form.num_colors.data)

        # TheColorAPI uses "monochrome", not "monochromatic"
        api_mode = mode
        if mode == "monochromatic":
            api_mode = "monochrome"

        try:
            # Make API request
            response = requests.get(
                COLOR_API_URL,
                params={
                    "hex": hex_color,
                    "mode": api_mode,
                    "count": count
                }
            )

            response.raise_for_status()  # Raise error for bad status codes
            data = response.json()

            # Try to extract the name of the main color from the API response
            main_name = None
            if "colors" in data and len(data["colors"]) > 0:
                main_name = data["colors"][0]["name"]["value"]

            palette_data = {
                'main_color_hex': hex_color,
                'main_color_name': main_name or "Unknown",
                'mode': mode,
                'colors': [],
                'description': generate_description(mode)
            }

            # Safely handle colors list
            if 'colors' in data:
                for color in data['colors']:

                    # FIX #3 — Safely extract nested color values
                    hex_value = color.get('hex', {}).get('value')
                    name_value = color.get('name', {}).get('value')

                    palette_data['colors'].append({
                        'hex': hex_value,
                        'name': name_value or "Unnamed Color"
                    })

            else:
                return render_template('index.html', form=form, error=f"API returned no colors.")

            # Render results page
            return render_template('palette_results.html', palette=palette_data)

        except requests.exceptions.RequestException as e:
            # Handle API connection issues
            return render_template('index.html', form=form, error=f"API connection error: {e}")

        except Exception as e:
            # Handle unexpected errors
            return render_template('index.html', form=form, error=f"Unexpected data processing error: {e}")

    # Render initial form page
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)