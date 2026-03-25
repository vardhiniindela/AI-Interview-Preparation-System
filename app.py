import streamlit as st
import time
from questions import get_questions
from evaluator import evaluate_answer
from database import save_result

st.set_page_config(page_title="AI Interview System", layout="centered")

# -------------------------------
# 🎨 UI Styling (Colors)
# -------------------------------
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-size: 18px;
    height: 50px;
    border-radius: 10px;
}
.stTextArea textarea {
    border-radius: 10px;
}
h1 {
    color: #2E86C1;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.markdown("<h1>🎯 AI Interview Preparation System</h1>", unsafe_allow_html=True)

# -------------------------------
# Sample Guide
# -------------------------------
if st.button("📘 Use Sample Answers Guide"):
    st.info("👉 Open 'sample_answers.txt' file and copy answers to test")

# -------------------------------
# Skill Selection
# -------------------------------
skills = st.multiselect("Select Skills", ["Python", "SQL"])

# -------------------------------
# Start Button (CENTER)
# -------------------------------
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("🚀 Start Interview", use_container_width=True):

        if not skills:
            st.warning("⚠ Please select at least one skill")
        else:
            st.session_state["questions"] = get_questions(skills)
            st.session_state["index"] = 0
            st.session_state["score"] = 0
            st.session_state["history"] = []
            st.session_state["start_time"] = time.time()

# -------------------------------
# Interview Flow
# -------------------------------
if "questions" in st.session_state:

    idx = st.session_state["index"]
    questions = st.session_state["questions"]

    # Progress bar
    progress = int((idx / len(questions)) * 100)
    st.progress(min(progress, 100))

    if idx < len(questions):

        st.markdown(f"### 🧠 Question {idx+1}")
        st.info(questions[idx])

        answer = st.text_area("✍ Your Answer", key=f"answer_{idx}")

        if st.button("✅ Submit Answer", key=f"submit_{idx}"):

            if answer.strip() == "":
                st.warning("⚠ Please write an answer")
            else:
                time_taken = int(time.time() - st.session_state["start_time"])

                feedback, score = evaluate_answer(answer)

                st.success(feedback)
                st.write(f"🧠 Score: {score}")
                st.write(f"⏱ Time Taken: {time_taken} sec")

                st.session_state["score"] += score
                st.session_state["history"].append(
                    (questions[idx], answer, score, time_taken)
                )
                st.session_state["index"] += 1
                st.session_state["start_time"] = time.time()

                st.rerun()

    else:
        # -------------------------------
        # Final Result
        # -------------------------------
        
        st.markdown("### ⭐ ⭐ ⭐ ⭐ ⭐")
        st.success("🌟 Great Job! Interview Completed")

        final_score = st.session_state["score"]
        st.subheader(f"🏆 Final Score: {final_score}")

        if final_score > 150:
            st.success("🚀 Excellent Performance")
        elif final_score > 100:
            st.info("👍 Good Performance")
        else:
            st.warning("⚠ Needs Improvement")

        save_result(final_score)

        # -------------------------------
        # Download Report
        # -------------------------------
        report = f"Final Score: {final_score}\n\n"

        for q, a, s, t in st.session_state["history"]:
            report += f"Q: {q}\nA: {a}\nScore: {s}\nTime: {t} sec\n\n"

        st.download_button("📥 Download Report", report, file_name="report.txt")

        # -------------------------------
        # Answer Review
        # -------------------------------
        st.subheader("📜 Answer Review")

        for q, a, s, t in st.session_state["history"]:
            st.markdown(f"**Q:** {q}")
            st.markdown(f"**Your Answer:** {a}")
            st.markdown(f"**Score:** {s}")
            st.markdown(f"**Time:** {t} sec")
            st.markdown("---")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("👩‍💻 Developed by Vardhini | AI Interview System")

st.markdown("""
<style>
@keyframes glow {
  0% {opacity: 0.3;}
  50% {opacity: 1;}
  100% {opacity: 0.3;}
}

.stars {
  font-size: 30px;
  text-align: center;
  animation: glow 1s infinite;
  color: gold;
}
</style>

<div class="stars">🌟 ⭐ 🌟 ⭐ 🌟</div>
""", unsafe_allow_html=True)