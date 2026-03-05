from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h1>Hostlab</h1>
        <p>Log in to get access to virtual machines.</p>
        <form>
            <label for="code-input">Code</label>
            <input id="code-input">
            <button type="submit">Log in</button>
        </form>
    """