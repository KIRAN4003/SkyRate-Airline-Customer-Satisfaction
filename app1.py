import streamlit as st

st.set_page_config(
    page_title="SkyRate | Airline Intelligence",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Shared state ────────────────────────────────────────
if "submissions" not in st.session_state:
    st.session_state.submissions = []
if "seat_counter" not in st.session_state:
    st.session_state.seat_counter = 0

# ── Live stats ──────────────────────────────────────────
total   = len(st.session_state.submissions)
sat     = sum(1 for s in st.session_state.submissions if s.get("Predicted") == "Satisfied")
sat_pct = round(sat / total * 100) if total > 0 else 0

# ── CSS ─────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
  --bg:        #03060F;
  --bg2:       #070D1C;
  --bg3:       #0C1528;
  --glass:     rgba(255,255,255,0.03);
  --glass2:    rgba(255,255,255,0.06);
  --border:    rgba(255,255,255,0.07);
  --border2:   rgba(99,179,255,0.2);
  --blue:      #3B8BFF;
  --blue2:     #1A6EFF;
  --cyan:      #00E5FF;
  --glow:      rgba(59,139,255,0.15);
  --text:      #E2EAF4;
  --text2:     #7A90AA;
  --text3:     #3D5166;
  --sat:       #00E5FF;
  --dis:       #FF6B6B;
  --gold:      #FFD166;
}

* { font-family: 'DM Sans', sans-serif; box-sizing: border-box; margin: 0; padding: 0; }
h1,h2,h3,.logo-text,.hero-title,.stat-val { font-family: 'Syne', sans-serif; }

/* ── Base ── */
.stApp { background: var(--bg) !important; }
section[data-testid="stSidebar"] { display: none !important; }
#MainMenu, footer, header { visibility: hidden !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 3px; height: 3px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--blue2); border-radius: 2px; }

/* ── Grid bg pattern ── */
.stApp::before {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background-image:
    linear-gradient(rgba(59,139,255,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(59,139,255,0.03) 1px, transparent 1px);
  background-size: 40px 40px;
}
.stApp::after {
  content: '';
  position: fixed; inset: 0; z-index: 0; pointer-events: none;
  background:
    radial-gradient(ellipse 80% 50% at 20% -10%, rgba(59,139,255,0.12) 0%, transparent 60%),
    radial-gradient(ellipse 60% 40% at 80% 110%, rgba(0,229,255,0.08) 0%, transparent 60%);
}

/* ── Navbar ── */
.navbar {
  position: sticky; top: 0; z-index: 1000;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 36px; height: 60px;
  background: rgba(3,6,15,0.85);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
}
.nav-brand { display: flex; align-items: center; gap: 12px; }
.nav-logo {
  width: 34px; height: 34px;
  background: linear-gradient(135deg, var(--blue), var(--cyan));
  border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 0 20px rgba(59,139,255,0.4);
}
.nav-name { font-family: 'Syne', sans-serif; font-size: 17px; font-weight: 800; color: #fff; letter-spacing: -0.3px; }
.nav-tag  { font-size: 9px; font-weight: 500; color: var(--text3); text-transform: uppercase; letter-spacing: 1.5px; margin-top: 1px; }
.nav-right { display: flex; align-items: center; gap: 10px; }
.pill { display: flex; align-items: center; gap: 6px; padding: 5px 13px; border-radius: 999px; font-size: 11px; font-weight: 500; letter-spacing: 0.3px; }
.pill-blue { background: rgba(59,139,255,.1); border: 1px solid rgba(59,139,255,.2); color: var(--blue); }
.pill-live { background: rgba(0,229,255,.06); border: 1px solid rgba(0,229,255,.12); color: var(--cyan); }
.dot-live  { width: 6px; height: 6px; border-radius: 50%; background: var(--cyan); animation: blink 2s infinite; }
@keyframes blink { 0%,100%{opacity:1;box-shadow:0 0 6px var(--cyan)} 50%{opacity:.4;box-shadow:none} }

/* ── Hero ── */
.hero {
  position: relative; z-index: 1;
  padding: 52px 36px 44px;
  border-bottom: 1px solid var(--border);
}
.hero-eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 5px 14px; border-radius: 999px;
  background: rgba(59,139,255,.08); border: 1px solid rgba(59,139,255,.15);
  font-size: 11px; font-weight: 600; color: var(--blue);
  text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 20px;
}
.hero-title {
  font-size: 42px; font-weight: 800; line-height: 1.1;
  letter-spacing: -1px; color: #fff; margin-bottom: 14px;
}
.hero-title .accent {
  background: linear-gradient(135deg, var(--blue), var(--cyan));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-desc {
  font-size: 15px; color: var(--text2); line-height: 1.7;
  max-width: 560px; margin-bottom: 36px; font-weight: 400;
}
.hero-cards { display: flex; gap: 14px; flex-wrap: wrap; }
.hcard {
  display: flex; align-items: center; gap: 14px;
  padding: 16px 20px; border-radius: 16px;
  background: var(--glass); border: 1px solid var(--border);
  backdrop-filter: blur(12px); min-width: 160px;
  transition: border-color .3s, box-shadow .3s;
}
.hcard:hover { border-color: var(--border2); box-shadow: 0 0 24px var(--glow); }
.hcard-icon { width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0; }
.hcard-val { font-family:'Syne',sans-serif; font-size:22px; font-weight:800; color:#fff; line-height:1; }
.hcard-lbl { font-size:10px; color:var(--text3); text-transform:uppercase; letter-spacing:1px; margin-top:3px; font-weight:500; }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
  background: transparent !important;
  border-bottom: 1px solid var(--border) !important;
  padding: 0 36px !important; gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
  background: transparent !important; color: var(--text3) !important;
  font-family: 'DM Sans', sans-serif !important;
  font-size: 13px !important; font-weight: 600 !important;
  padding: 16px 22px !important;
  border-bottom: 2px solid transparent !important;
  transition: color .2s !important;
}
.stTabs [aria-selected="true"] { color: var(--blue) !important; border-bottom: 2px solid var(--blue) !important; }
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] { display: none !important; }

/* ── Page content ── */
.page-content { padding: 28px 36px; position: relative; z-index: 1; }

/* ── Glass cards ── */
.sky-card {
  background: var(--glass); border: 1px solid var(--border);
  border-radius: 18px; padding: 22px; backdrop-filter: blur(16px);
  transition: border-color .3s, box-shadow .3s;
}
.sky-card:hover { border-color: var(--border2); box-shadow: 0 0 32px var(--glow); }

/* ── Metric cards ── */
.metric-card {
  background: var(--glass); border: 1px solid var(--border);
  border-radius: 16px; padding: 18px 20px; backdrop-filter: blur(16px);
  transition: all .3s; position: relative; overflow: hidden;
}
.metric-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(59,139,255,.3), transparent);
}
.metric-card:hover { border-color: var(--border2); transform: translateY(-2px); box-shadow: 0 8px 32px var(--glow); }
.metric-label { font-size: 10px; text-transform: uppercase; letter-spacing: 1.2px; color: var(--text3); margin-bottom: 8px; font-weight: 700; }
.metric-value { font-family:'Syne',sans-serif; font-size:30px; font-weight:800; line-height:1; }
.metric-sub   { font-size: 11px; color: var(--text3); margin-top: 5px; font-weight: 400; }

/* ── Chat ── */
.chat-container {
  display: flex; flex-direction: column; gap: 16px;
  max-height: 460px; overflow-y: auto; padding: 22px;
  background: rgba(3,6,15,0.6); border-radius: 18px;
  border: 1px solid var(--border); margin-bottom: 18px;
  backdrop-filter: blur(12px);
}
.bubble-bot, .bubble-user {
  display: flex; align-items: flex-start; gap: 10px;
  max-width: 84%; animation: slideUp .3s ease;
}
@keyframes slideUp { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:translateY(0)} }
.bubble-user { flex-direction: row-reverse; align-self: flex-end; }
.av-bot {
  width: 32px; height: 32px; border-radius: 10px; flex-shrink: 0;
  background: linear-gradient(135deg, var(--blue), var(--cyan));
  display: flex; align-items: center; justify-content: center;
  font-size: 10px; font-weight: 800; color: #fff;
  box-shadow: 0 0 16px rgba(59,139,255,.35);
}
.av-user {
  width: 32px; height: 32px; border-radius: 10px; flex-shrink: 0;
  background: var(--glass2); border: 1px solid var(--border);
  display: flex; align-items: center; justify-content: center;
  font-size: 10px; color: var(--text2); font-weight: 600;
}
.msg-bot {
  background: var(--glass2); color: var(--text);
  border: 1px solid var(--border);
  padding: 12px 16px; border-radius: 4px 16px 16px 16px;
  font-size: 14px; line-height: 1.65; backdrop-filter: blur(8px);
}
.msg-user {
  background: linear-gradient(135deg, var(--blue2), var(--blue));
  color: #fff; font-weight: 500;
  padding: 12px 16px; border-radius: 16px 4px 16px 16px;
  font-size: 14px; line-height: 1.65;
  box-shadow: 0 4px 16px rgba(59,139,255,.25);
}
.msg-bot b, .msg-bot strong { color: var(--cyan); font-weight: 600; }

/* ── Progress ── */
.pbar-wrap { margin-bottom: 10px; }
.pbar-track { height: 2px; background: var(--border); border-radius: 2px; margin-bottom: 6px; overflow: hidden; }
.pbar-fill {
  height: 100%; background: linear-gradient(90deg, var(--blue), var(--cyan));
  border-radius: 2px; transition: width .6s cubic-bezier(.4,0,.2,1);
  box-shadow: 0 0 8px rgba(59,139,255,.5);
}
.pbar-label { font-size: 11px; color: var(--text3); text-align: right; font-weight: 600; }

/* ── Section header ── */
.sec-head {
  font-family: 'Syne', sans-serif;
  font-size: 10px; font-weight: 700; color: var(--text3);
  text-transform: uppercase; letter-spacing: 1.5px;
  display: flex; align-items: center; gap: 12px;
  margin: 24px 0 16px;
}
.sec-head::after { content: ''; flex: 1; height: 1px; background: linear-gradient(90deg, var(--border), transparent); }

/* ── Table ── */
.sky-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.sky-table thead { background: rgba(3,6,15,0.8); }
.sky-table th {
  padding: 11px 14px; text-align: left; color: var(--text3);
  font-size: 9px; text-transform: uppercase; letter-spacing: 1px;
  border-bottom: 1px solid var(--border); white-space: nowrap; font-weight: 700;
}
.sky-table td {
  padding: 11px 14px; color: var(--text);
  border-bottom: 1px solid rgba(255,255,255,0.03); white-space: nowrap;
}
.sky-table tr:hover td { background: rgba(59,139,255,0.04); }
.sky-table tr:last-child td { border-bottom: none; }

/* ── Badges ── */
.bdg { display:inline-block; padding:4px 12px; border-radius:999px; font-size:10px; font-weight:700; letter-spacing:.5px; }
.bdg-sat { background:rgba(0,229,255,.08); color:var(--cyan); border:1px solid rgba(0,229,255,.15); }
.bdg-dis { background:rgba(255,107,107,.08); color:var(--dis); border:1px solid rgba(255,107,107,.15); }
.stars { color: var(--gold); letter-spacing: 2px; font-size: 11px; }

/* ── Thanks card ── */
.thanks-card {
  background: var(--glass); border: 1px solid rgba(59,139,255,.15);
  border-radius: 24px; padding: 36px 32px; text-align: center;
  max-width: 500px; margin: 0 auto; backdrop-filter: blur(20px);
  box-shadow: 0 16px 48px rgba(0,0,0,.4), 0 0 64px var(--glow);
  position: relative; overflow: hidden;
}
.thanks-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(59,139,255,.4), var(--cyan), rgba(59,139,255,.4), transparent);
}
.check-circle {
  width: 68px; height: 68px;
  background: linear-gradient(135deg, rgba(59,139,255,.2), rgba(0,229,255,.1));
  border-radius: 50%; display: flex; align-items: center;
  justify-content: center; margin: 0 auto 18px; font-size: 28px;
  border: 1px solid rgba(59,139,255,.2); box-shadow: 0 0 32px rgba(59,139,255,.2);
}

/* ── Footer ── */
.sky-footer {
  position: relative; z-index: 1;
  background: rgba(3,6,15,0.8); border-top: 1px solid var(--border);
  backdrop-filter: blur(16px); padding: 18px 36px;
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 48px;
}
.footer-copy { font-size: 12px; color: var(--text3); }
.footer-copy span { color: var(--blue); font-weight: 600; }
.footer-links { display: flex; gap: 8px; }
.flink {
  font-size: 11px; color: var(--text3); text-decoration: none;
  padding: 5px 12px; border-radius: 8px; border: 1px solid var(--border);
  font-weight: 500; transition: all .2s; background: var(--glass);
}
.flink:hover { color: var(--blue); border-color: rgba(59,139,255,.3); background: rgba(59,139,255,.06); }

/* ── Streamlit overrides ── */
.stButton > button {
  background: rgba(59,139,255,.1) !important;
  border: 1px solid rgba(59,139,255,.25) !important;
  color: var(--blue) !important; border-radius: 10px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 600 !important; font-size: 13px !important;
  transition: all .2s !important;
}
.stButton > button:hover {
  background: rgba(59,139,255,.2) !important;
  border-color: rgba(59,139,255,.4) !important;
  box-shadow: 0 0 16px rgba(59,139,255,.2) !important;
  transform: translateY(-1px) !important;
}
.stButton > button[kind="primary"] {
  background: linear-gradient(135deg, var(--blue2), var(--blue)) !important;
  border: none !important; color: #fff !important;
  box-shadow: 0 4px 16px rgba(59,139,255,.3) !important;
}
.stButton > button[kind="primary"]:hover {
  box-shadow: 0 6px 24px rgba(59,139,255,.45) !important;
  transform: translateY(-1px) !important;
}
.stTextInput > div > div > input {
  background: var(--glass) !important; border: 1px solid var(--border) !important;
  color: var(--text) !important; border-radius: 10px !important;
  font-family: 'DM Sans', sans-serif !important;
}
.stTextInput > div > div > input:focus {
  border-color: rgba(59,139,255,.4) !important;
  box-shadow: 0 0 0 3px rgba(59,139,255,.08) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Navbar ──────────────────────────────────────────────
st.markdown("""
<div class="navbar">
  <div class="nav-brand">
    <div class="nav-logo">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="white">
        <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/>
      </svg>
    </div>
    <div>
      <div class="nav-name">SkyRate</div>
      <div class="nav-tag">Airline Intelligence Platform</div>
    </div>
  </div>
  <div class="nav-right">
    <div class="pill pill-blue">✈️ Pre-Flight Analysis</div>
    <div class="pill pill-live"><div class="dot-live"></div>Live</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <div class="hero-eyebrow">
    ⚡ XGBoost · 90.3% Accuracy · Real-Time Prediction
  </div>
  <div class="hero-title">
    Passenger Satisfaction<br><span class="accent">Intelligence System</span>
  </div>
  <div class="hero-desc">
    AI-powered pre-flight feedback platform. Predict passenger satisfaction
    at check-in and enable proactive service recovery — before the aircraft departs.
  </div>
  <div class="hero-cards">
    <div class="hcard">
      <div class="hcard-icon" style="background:rgba(59,139,255,0.12)">🤖</div>
      <div><div class="hcard-val">90.3%</div><div class="hcard-lbl">Accuracy</div></div>
    </div>
    <div class="hcard">
      <div class="hcard-icon" style="background:rgba(0,229,255,0.08)">📋</div>
      <div><div class="hcard-val">{total}</div><div class="hcard-lbl">Responses</div></div>
    </div>
    <div class="hcard">
      <div class="hcard-icon" style="background:rgba(255,209,102,0.08)">😊</div>
      <div><div class="hcard-val">{sat_pct}%</div><div class="hcard-lbl">Satisfied</div></div>
    </div>
    <div class="hcard">
      <div class="hcard-icon" style="background:rgba(255,107,107,0.08)">⚡</div>
      <div><div class="hcard-val">~90s</div><div class="hcard-lbl">Feedback Time</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ─────────────────────────────────────────────────
tab1, tab2 = st.tabs(["🤖  Passenger Feedback", "📊  Airline Dashboard"])

with tab1:
    import pages.chatbot as chatbot
    chatbot.run()

with tab2:
    import pages.dashboard as dashboard
    dashboard.run()

# ── Footer ───────────────────────────────────────────────
st.markdown("""
<div class="sky-footer">
  <div class="footer-copy">
    Built by <span>Kiran U</span> &nbsp;·&nbsp;
    PGP Data Science & GenAI &nbsp;·&nbsp; Great Learning 2026
  </div>
  <div class="footer-links">
    <a class="flink" href="https://www.linkedin.com/in/kiran-u-471818325/" target="_blank">LinkedIn</a>
    <a class="flink" href="https://github.com/KIRAN4003" target="_blank">GitHub</a>
    <a class="flink" href="mailto:kirankiranu791@gmail.com">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)