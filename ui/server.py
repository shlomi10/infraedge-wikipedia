import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from flask import Flask, render_template_string, request, send_from_directory

from utils.constants import BASE_URL
from runner import run_test


app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Wikipedia Unique Words Runner</title>
  <style>
    body { margin: 0; font-family: Arial, sans-serif; background: #0b1017; color: #e8eef5; }
    .wrap { max-width: 1100px; margin: 0 auto; padding: 32px 20px 60px; }
    .hero { text-align: center; }
    .hero img { width: 140px; background: #fff; border-radius: 16px; padding: 10px; }
    h1 { margin: 16px 0 8px; }
    p.sub { color: #9db0c7; }
    form { display: flex; gap: 12px; margin: 28px 0; }
    input[type=url] { flex: 1; padding: 12px 14px; border-radius: 10px; border: 1px solid #2a3b52; background: #16202c; color: #e8eef5; }
    button { padding: 12px 22px; border: 0; border-radius: 10px; background: linear-gradient(90deg, #3366cc, #2a9d8f); color: #fff; font-weight: 700; cursor: pointer; }
    .status { padding: 16px; border-radius: 12px; text-align: center; font-weight: 700; margin: 16px 0; }
    .pass { background: rgba(42,157,143,.18); border: 1px solid #2a9d8f; color: #7ee0d0; }
    .fail { background: rgba(230,57,70,.16); border: 1px solid #e63946; color: #ff8a93; }
    .metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
    .metric { background: #16202c; padding: 16px; border-radius: 12px; text-align: center; }
    .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 20px; }
    table { width: 100%; border-collapse: collapse; background: #16202c; border-radius: 12px; overflow: hidden; }
    th, td { padding: 8px 10px; text-align: left; border-bottom: 1px solid #243246; }
    pre { background: #16202c; padding: 14px; border-radius: 12px; overflow: auto; }
    @media (max-width: 800px) { form, .metrics, .cols { display: block; } button { width: 100%; margin-top: 10px; } }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="hero">
      <img src="/assets/wikipedia-logo.png" alt="Wikipedia">
      <h1>Wikipedia Unique Words Runner</h1>
      <p class="sub">Runs the UI + API pytest and shows unique-word results</p>
    </div>
    <form method="post">
      <input type="url" name="url" value="{{ url }}" required>
      <button type="submit">Run test</button>
    </form>
    {% if result %}
      <div class="status {{ 'pass' if result.passed else 'fail' }}">
        {{ 'PASSED — unique word counts match' if result.passed else 'FAILED — unique word counts do not match' }}
      </div>
      <div class="metrics">
        <div class="metric">UI unique words<br><strong>{{ result.ui_unique if result.ui_unique is not none else '-' }}</strong></div>
        <div class="metric">API unique words<br><strong>{{ result.api_unique if result.api_unique is not none else '-' }}</strong></div>
        <div class="metric">Match<br><strong>{{ 'Yes' if result.passed else 'No' }}</strong></div>
      </div>
      <div class="cols">
        <div>
          <h3>UI word occurrences</h3>
          <table>
            <tr><th>word</th><th>count</th></tr>
            {% for word, count in result.ui_counts.items() %}
            <tr><td>{{ word }}</td><td>{{ count }}</td></tr>
            {% endfor %}
          </table>
        </div>
        <div>
          <h3>API word occurrences</h3>
          <table>
            <tr><th>word</th><th>count</th></tr>
            {% for word, count in result.api_counts.items() %}
            <tr><td>{{ word }}</td><td>{{ count }}</td></tr>
            {% endfor %}
          </table>
        </div>
      </div>
      <h3>Pytest output</h3>
      <pre>{{ result.output }}</pre>
    {% endif %}
  </div>
</body>
</html>
"""


@app.get("/assets/<path:filename>")
def assets(filename: str):
    return send_from_directory(ROOT / "assets", filename)


@app.route("/", methods=["GET", "POST"])
def home():
    url = (request.form.get("url") or BASE_URL).strip()
    result = run_test(url) if request.method == "POST" else None
    return render_template_string(PAGE, url=url, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8501)
