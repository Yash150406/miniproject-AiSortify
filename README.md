🧠 AI Sortify
AI Sortify is a simple web application built with Flask and HTML that helps users filter and discover AI tools based on category and pricing from a dataset.

🚀 Features
🔎 Search AI tools by Major Category.

💸 Filter tools based on Pricing (Free / Paid / Other).

🖥️ Dynamic rendering using Flask backend and HTML frontend.

📢 Graceful message display if no matching tools are found.

🛠 Tech Stack
Backend: Python, Flask, Pandas

Frontend: HTML, CSS (optional)

Data: tools_updated.csv

📂 Project Structure
bash
CopyEdit
/ai-sortify
│
├── app.py            # Flask backend
├── tools_updated.csv # Dataset file
├── /templates
│   └── index.html    # Frontend HTML page
├── /static           # (Optional) For CSS, JS, Images
└── README.md         # Project documentation
📋 Setup Instructions
Clone the repository:

bash
CopyEdit
git clone https://github.com/your-username/ai-sortify.git
cd ai-sortify
Install dependencies:

Make sure you have Python installed. Then:

bash
CopyEdit
pip install flask pandas
Add the dataset:

Make sure tools_updated.csv is placed in the root directory.
(The app will not start without it.)

Run the application:

bash
CopyEdit
python app.py
Access the app:

Open your browser and visit:

cpp
CopyEdit
http://127.0.0.1:5000/
✨ Usage
Enter a category (example: "Data Analysis", "NLP") to filter tools by type.

Enter a pricing option (example: "Free", "Paid") to filter based on cost.

Click Submit to view matching tools.

If no tools match your search, a user-friendly message will be displayed.

📑 Notes
Ensure your tools_updated.csv has columns like Major Category and Free/Paid/Other.

You can customize the front-end by editing index.html inside the templates folder.

For better UI, you can add CSS/JS files inside the static folder.

📄 License
This project is open-source and free to use.
