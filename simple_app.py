from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    github_owner_login = "pruthvirajguddu"  # Replace with actual GitHub login (can fetch from GitHub API)
    site_icon_url = "/static/images/icon.png"  # Replace with your actual icon URL

    # Example links data (you can load this from a file or database)
    links = [
        {"name": "GitHub", "url": "https://github.com"},
        {"name": "LinkedIn", "url": "https://linkedin.com"},
        {"name": "Twitter", "url": "https://twitter.com"}
    ]

    return render_template('index.html', 
                           github_owner_login=github_owner_login,
                           site_icon_url=site_icon_url,
                           links=links)


if __name__ == "__main__":
    app.run(debug=True)
