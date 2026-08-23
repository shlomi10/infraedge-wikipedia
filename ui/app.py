import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st

from utils.constants import BASE_URL
from styles import CUSTOM_CSS, HEADER_HTML
from runner import run_test


st.set_page_config(
    page_title="Wikipedia Unique Words Runner",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed",
)
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
st.markdown(HEADER_HTML, unsafe_allow_html=True)

url = st.text_input("Wikipedia URL", value=BASE_URL)

if st.button("Run test"):
    with st.spinner("Running pytest. The browser will open for the UI check."):
        result = run_test(url.strip() or BASE_URL)
    st.session_state["result"] = result

result = st.session_state.get("result")
if not result:
    st.info("Set a URL and click Run test to execute tests/test_unique_word_count.py")
    st.stop()

if result["passed"]:
    st.markdown('<div class="status-pass">PASSED — unique word counts match</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="status-fail">FAILED — unique word counts do not match</div>', unsafe_allow_html=True)

ui_unique = result["ui_unique"]
api_unique = result["api_unique"]
left, middle, right = st.columns(3)
left.metric("UI unique words", ui_unique if ui_unique is not None else "-")
middle.metric("API unique words", api_unique if api_unique is not None else "-")
right.metric(
    "Match",
    "Yes" if result["passed"] else "No",
)

ui_col, api_col = st.columns(2)
with ui_col:
    st.subheader("UI word occurrences")
    if result["ui_counts"]:
        st.dataframe(
            [{"word": word, "count": count} for word, count in result["ui_counts"].items()],
            hide_index=True,
            use_container_width=True,
        )
    else:
        st.write("No UI counts parsed")

with api_col:
    st.subheader("API word occurrences")
    if result["api_counts"]:
        st.dataframe(
            [{"word": word, "count": count} for word, count in result["api_counts"].items()],
            hide_index=True,
            use_container_width=True,
        )
    else:
        st.write("No API counts parsed")

with st.expander("Pytest output"):
    st.code(result["output"], language="text")
