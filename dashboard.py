import streamlit as st
import os

# Paths to log files
COMMAND_LOG_PATH = "command_log.txt"
LOGS_DIR = "logs"
LOGS_FILE_PATH = os.path.join(LOGS_DIR, "commands.txt")

st.set_page_config(page_title="Voice-Guided Git Automation", layout="wide")

st.title("🗣️ Voice-Guided Git Automation Dashboard")
st.markdown("### ✅ Real-time log view of your Git voice commands")

# --- Load logs ---
def load_log_file(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "⚠️ No logs available yet."

# Display Command Log (EXECUTED only, no Recognized)
st.subheader("📌 Command Execution Log (command_log.txt)")
command_log = load_log_file(COMMAND_LOG_PATH)

# Keep only lines that contain EXECUTED, skip Recognized
executed_only = "\n".join(
    [line for line in command_log.splitlines() if "EXECUTED" in line]
)

st.text_area("Command Log", executed_only if executed_only else "⚠️ No executed commands yet.", height=300)


# Display Detailed Logs
# Display Detailed Logs
st.subheader("📝 Detailed Logs (logs/commands.txt)")
detailed_log = load_log_file(LOGS_FILE_PATH)

# Add some extra info about file stats
if os.path.exists(LOGS_FILE_PATH):
    file_size = os.path.getsize(LOGS_FILE_PATH) / 1024  # KB
    last_modified = os.path.getmtime(LOGS_FILE_PATH)
    import time
    st.markdown(f"**📂 File size:** {file_size:.2f} KB  |  **🕒 Last updated:** {time.ctime(last_modified)}")

# Show the actual log content
st.text_area("Detailed Log", detailed_log, height=300)

# Option to download logs
if os.path.exists(LOGS_FILE_PATH):
    with open(LOGS_FILE_PATH, "r", encoding="utf-8") as f:
        st.download_button("⬇️ Download Detailed Logs", f, file_name="commands.txt")

if st.button("🔄 Refresh Logs"): st.rerun() 