import time
import streamlit as st

st.title("⏱️ เกมคำนวณหาค่าพื้นที่และปริมาตรของทรงกลมและสี่เหลี่ยมผืนผ้า")

# 1. กำหนดค่าเริ่มต้นใน session_state
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.start = time.time()
    st.session_state.is_ended = False


@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    if u_ans1 == "38,808":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    if u_ans2 == "300":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    if u_ans3 == "3,000":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "616":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    if u_ans5 == "616 และ 1,437.33":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")


st.button("🎮 เริ่มเกม", on_click=reset_game)

# 📌 จองพื้นที่สำหรับแสดงเวลานับถอยหลัง
timer_placeholder = st.empty()

st.divider()

ans1 = st.text_input(
    "ข้อ 1: แตงโมรูปทรงกลมสมบูรณ์มีรัศมียาว 21 เซนติเมตร จงหาปริมาตรของแตงโมผลนี้ (กำหนดให้ค่า π คือ 22/7)",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: สนามหญ้ารูปสี่เหลี่ยมผืนผ้าแห่งหนึ่ง มีความกว้าง 12 เมตร และมีความยาว 25 เมตร จงหาพื้นที่ของสนามหญ้าแห่งนี้",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3: กล่องพัสดุทรงสี่เหลี่ยมมุมฉาก มีความกว้าง 10 เซนติเมตร ยาว 15 เซนติเมตร และสูง 20 เซนติเมตร กล่องใบนี้มีความจุหรือปริมาตรเท่าใด",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: ลูกบอลทรงกลมลูกหนึ่งมีรัศมี 7 เซนติเมตร จงหาพื้นที่ผิวของลูกบอลนี้ (กำหนดให้ค่า π คือ 22/7)",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5: ถังเก็บน้ำทรงกลมใบหนึ่ง มีเส้นผ่านศูนย์กลางยาว 14 เมตร จงคำนวณหาพื้นที่ผิวภายนอกของถังเก็บน้ำและปริมาตรสูงสุดที่ถังใบนี้สามารถบรรจุได้ (กำหนดให้ค่า π คือ 22/7)",
    value=st.session_state.ans5_val,
)

st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

if st.session_state.get("is_ended", False):
    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val,
        st.session_state.ans5_val,
    )

# 📌 วน Loop นับถอยหลังอยู่ข้างล่างสุด
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(600 - (time.time() - st.session_state.start))
    if time_left > 0:
        timer_placeholder.error(f"⏳ เหลือเวลา: {time_left} วินาที")
        time.sleep(1)
        st.rerun()
    else:
        st.session_state.is_ended = True
        st.rerun()
