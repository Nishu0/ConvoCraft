# ConvoCraft

Talk to a bot specialized in the development of Streamlit apps.
Indicate what you want to appear on the app and the bot will generate the code for you and update the existing app.

## Instructions Examples

Tell ChatbotX the following instructions:

Simple instructions:
- "Add a title with the text 'Hello World' and a subtitle with the text 'This is my first Streamlit application'."
- "Add an input text box with the label 'Enter your name' and an other one with the label 'Enter your age' and a button with the label 'Submit'. When the button is clicked, display the text 'Hello, <name>! You are <age> years old.'"
- "Add a sidebar to the application with a dropdown menu for selecting options ("update", "save", "reset")."

Upload files and display charts:
- "Display the function f(x) = x^2 in a line chart for x in [-10, 10] and give the graph an adequat name."
- "Give the possibility to upload a csv file and display its content in a table after upload"
- "Give the possibility to upload a csv file and display a bar chart showing the data"

Useful apps:
- "Ask to enter a first date and a second date input and display the number of days between them. Add a title and some explanation text accordingly before the date inputs."
- "Ask to enter a first date and a second date input and display the number of business days between them. Add a title and some explanation text accordingly before the date inputs."

Webscraping:
- "Webscrap the site Generate a scatter plot with the temperature and humidity data given earlier."

Creating games:
- "Create me a rolling dice game"

Using open APIs:
- "Display me random cats pictures using open apis and add button to update the image"

More complexe instructions:
- "store the csv values from this url : "https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/prix-des-carburants-en-france-flux-instantane-v2/exports/csv?limit=-1&timezone=UTC&use_labels=false&epsg=4326" in a pandas dataframe (and cache it). use the ";" delimiter. Clean the data by applying a 100000 division to the latitude and longitude column and removing all None datas in the "gazole_prix" column and remove all "gazole_prix" above 3 . And add a plotly graph with streamlit lib that displays an open-street-map layout map with the coordinates from the dataframe "latitude" and "longitude" column and label them with the "gazole_prix" column. Also use "gazole_prix" to color and size the markers. The marker color range should correspond to the min and max of the column. Create a new size column that is 1/("gazole_prix")^4 thus the pricier the gazole the smaller the marker is."