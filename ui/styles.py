CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap');

.stApp {
    background:
        radial-gradient(circle at top, #1b2838 0%, #0b1017 45%, #070b10 100%);
    color: #e8eef5;
}

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
}

.hero {
    text-align: center;
    padding: 1.2rem 0 0.4rem;
}

.hero img {
    width: 92px;
    filter: drop-shadow(0 8px 24px rgba(51, 102, 204, 0.35));
}

.hero h1 {
    margin: 0.7rem 0 0.25rem;
    font-size: 2rem;
    letter-spacing: 0.02em;
}

.hero p {
    color: #9db0c7;
    margin: 0;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #3366cc, #2a9d8f);
    color: white;
    border: 0;
    border-radius: 12px;
    padding: 0.75rem 1rem;
    font-weight: 700;
    font-size: 1.05rem;
}

.stButton > button:hover {
    filter: brightness(1.08);
}

.status-pass, .status-fail {
    border-radius: 16px;
    padding: 1rem 1.2rem;
    text-align: center;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 0.6rem 0 1rem;
}

.status-pass {
    background: rgba(42, 157, 143, 0.18);
    border: 1px solid #2a9d8f;
    color: #7ee0d0;
}

.status-fail {
    background: rgba(230, 57, 70, 0.16);
    border: 1px solid #e63946;
    color: #ff8a93;
}

.block-container {
    padding-top: 1.2rem;
}
</style>
"""

HEADER_HTML = """
<div class="hero">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/240px-Wikipedia-logo-v2.svg.png" alt="Wikipedia">
  <h1>Wikipedia Unique Words Runner</h1>
  <p>Runs the UI + API pytest and shows unique-word results</p>
</div>
"""
