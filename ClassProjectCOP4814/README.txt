The Color Palette Generator can be run by completing the following steps:

    Step 1 - Install flask-wtf by executing this command: pip install Flask requests Flask-WTF

    Step 2 - Once flask-wtf is finished downloading, run the python command to open the app.py file: python app.py

    Step 3 - Now that app.py is running, open your local browser and type in the following IP address: http://127.0.0.1:5000/


Now that the Color Palette Generator script is up and running, it is time to have some fun making cool color palettes!

Here is a step-by-step guide on how to create two different color palettes with the main color lavender (#E6E6FA):

1. Monochromatic Palette

    Step 1 - In the first box titled "Main Color", type in the HEX code for the color lavender. Make sure to NOT include the hashtag (#), as the form will not accept the request

    Step 2 - Choose the "Color Palette Type". For this first example, we will choose "Monochromatic: Colors that have the same tone".

    Step 3 - Select the Number of Colors in the Palette. The options range from 2-6, but for this example, we will select the number "4" (four).

    Step 4 - Once all the options explained in Steps 1-3 are selected, press "Generate Color Palette" to see the monochromatic color palette come to life!

    Step 5- To create another palette, press "Generate Another Palette" at the bottom of the form

2. Triadic Palette

    Step 1 - Type in the same HEX color for lavender

    Step 2 - Select "Triadic: Three evenly spaced colors"

    Step 3 - For this example, we want three colors, so select the number "3" (three)

    Step 4 - Press "Generate Color Palette" to see the new palette!

The API that I used for this project is called "X-Colors"

    1. X-Colors API link: https://x-colors.herokuapp.com/api/gen
    2. Purpose: The Color Palette Generator uses this API to generate color palettes by using JSON format based on the HEX color provided by the user and a specified color theory mode (monochromatic, triadic, complementary, and analogous)
    3. Additional Features
        - Data Transformation: Uses input "mode" into a detailed, user-friendly explanation
        - Robust Validation: Utilizes Flask-WTF for form validation to ensure the user input is properly formatted
        - Error Handling: app.py includes multiple try/except blocks to manage the API connection failures and any unexpected data processing issues that may occur