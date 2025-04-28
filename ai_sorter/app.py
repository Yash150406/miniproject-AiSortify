from flask import Flask, render_template, request
import os
import pandas as pd

app = Flask(__name__, template_folder="templates", static_folder="static")

CSV_FILE = "tools_updated.csv"

if not os.path.exists(CSV_FILE):
    print(f"❌ ERROR: {CSV_FILE} not found! Make sure it's in the project folder.")
    exit()

tools_df = pd.read_csv(CSV_FILE)

@app.route('/', methods=['GET', 'POST'])
def index():
    filtered_tools = tools_df
    message = None

    if request.method == 'POST':
        user_query = request.form.get('category', '').strip().lower()
        pricing_filter = request.form.get('pricing', '').strip().lower()

        # Apply category filter if given
        if user_query:
            filtered_tools = filtered_tools[filtered_tools['Major Category'].str.lower().str.contains(user_query, na=False)]

        # Apply pricing filter if given
        if pricing_filter:
            filtered_tools = filtered_tools[filtered_tools['Free/Paid/Other'].str.lower().str.contains(pricing_filter, na=False)]

        # Show message if nothing found
        if filtered_tools.empty:
            message = "No tools found matching the criteria."

    return render_template('index.html', tools=filtered_tools.to_dict(orient='records'), message=message)

if __name__ == '__main__':
    app.run(debug=True)
