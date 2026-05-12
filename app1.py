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

# ── Custom CSS ──────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* { font-family: 'Inter', sans-serif; box-sizing: border-box; }

/* ── Global ── */
.stApp { background-color: #060E1F; }
section[data-testid="stSidebar"] { display: none; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0B1629; }
::-webkit-scrollbar-thumb { background: #1ECFAA40; border-radius: 4px; }

/* ── Top navigation bar ── */
.topbar {
    display: flex; align-items: center; justify-content: space-between;
    padding: 14px 32px; 
    background: rgba(13,30,56,0.95);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(30,207,170,0.1);
    position: sticky; top: 0; z-index: 999;
}
.logo-wrap { display: flex; align-items: center; gap: 12px; }
.logo-icon {
    width: 36px; height: 36px; 
    background: linear-gradient(135deg, #1ECFAA, #1A8EFF);
    border-radius: 10px; display: flex; align-items: center; justify-content: center;
    box-shadow: 0 0 16px rgba(30,207,170,0.3);
}
.logo-text { font-size: 18px; font-weight: 800; color: #fff; margin: 0; letter-spacing: -0.3px; }
.logo-sub  { font-size: 10px; color: #4A5E7A; text-transform: uppercase;
             letter-spacing: 1px; margin: 0; }
.topbar-right { display: flex; align-items: center; gap: 12px; }
.live-badge {
    display: flex; align-items: center; gap: 6px;
    background: rgba(30,207,170,.1); border: 1px solid rgba(30,207,170,.2);
    border-radius: 20px; padding: 5px 14px; font-size: 12px; color: #1ECFAA;
    font-weight: 500;
}
.stage-badge {
    display: flex; align-items: center; gap: 6px;
    background: rgba(26,142,255,.1); border: 1px solid rgba(26,142,255,.2);
    border-radius: 20px; padding: 5px 14px; font-size: 12px; color: #1A8EFF;
    font-weight: 500;
}
.ldot {
    width: 7px; height: 7px; background: #1ECFAA; border-radius: 50%;
    animation: pulse 1.5s infinite;
}
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.3} }

/* ── Hero Section ── */
.hero {
    background: linear-gradient(135deg, #0D1E38 0%, #0B1629 50%, #0D1E38 100%);
    border-bottom: 1px solid rgba(30,207,170,0.08);
    padding: 40px 32px 32px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; top: -50%; left: -10%;
    width: 40%; height: 200%;
    background: radial-gradient(ellipse, rgba(30,207,170,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.hero::after {
    content: '';
    position: absolute; top: -50%; right: -10%;
    width: 40%; height: 200%;
    background: radial-gradient(ellipse, rgba(26,142,255,0.06) 0%, transparent 70%);
    pointer-events: none;
}
.hero-title {
    font-size: 32px; font-weight: 800; color: #F1F5F9;
    margin: 0 0 8px; letter-spacing: -0.5px; line-height: 1.2;
}
.hero-title span { 
    background: linear-gradient(135deg, #1ECFAA, #1A8EFF);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero-sub {
    font-size: 14px; color: #64748B; margin: 0 0 28px;
    max-width: 520px; line-height: 1.6;
}
.hero-stats {
    display: flex; gap: 24px; flex-wrap: wrap;
}
.hero-stat {
    display: flex; align-items: center; gap: 10px;
    background: rgba(26,39,68,0.6); border: 1px solid #1A2744;
    border-radius: 12px; padding: 12px 16px;
    backdrop-filter: blur(8px);
}
.hero-stat-icon {
    width: 36px; height: 36px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px;
}
.hero-stat-val { font-size: 18px; font-weight: 700; color: #F1F5F9; line-height: 1; }
.hero-stat-lbl { font-size: 10px; color: #4A5E7A; text-transform: uppercase; 
                 letter-spacing: 0.5px; margin-top: 2px; }

/* ── Page content ── */
.page-content { padding: 24px 32px; }

/* ── Cards ── */
.sky-card {
    background: #1A2744; border: 1px solid #253555;
    border-radius: 16px; padding: 20px;
    transition: border-color 0.2s;
}
.sky-card:hover { border-color: rgba(30,207,170,0.2); }

/* ── Metric cards ── */
.metric-card {
    background: linear-gradient(135deg, #1A2744, #162038);
    border: 1px solid #253555;
    border-radius: 14px; padding: 16px 18px;
    transition: all 0.2s;
}
.metric-card:hover { 
    border-color: rgba(30,207,170,0.25);
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
.metric-label { 
    font-size: 10px; text-transform: uppercase;
    letter-spacing: .8px; color: #4A5E7A; margin-bottom: 6px;
    font-weight: 600;
}
.metric-value { font-size: 28px; font-weight: 800; line-height: 1; }
.metric-sub   { font-size: 11px; color: #4A5E7A; margin-top: 4px; }

/* ── Chat bubbles ── */
.chat-container {
    display: flex; flex-direction: column; gap: 14px;
    max-height: 440px; overflow-y: auto;
    padding: 20px; 
    background: linear-gradient(180deg, #0B1629, #060E1F);
    border-radius: 16px; border: 1px solid #1A2744;
    margin-bottom: 16px;
}
.bubble-bot, .bubble-user {
    display: flex; align-items: flex-start; gap: 10px; max-width: 82%;
    animation: fadeIn 0.3s ease;
}
@keyframes fadeIn { from{opacity:0;transform:translateY(8px)} to{opacity:1;transform:translateY(0)} }
.bubble-user { flex-direction: row-reverse; align-self: flex-end; }
.av-bot {
    width: 32px; height: 32px; border-radius: 50%; flex-shrink: 0;
    background: linear-gradient(135deg,#1ECFAA,#1A8EFF);
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; font-weight: 800; color: #0B1629;
    box-shadow: 0 0 12px rgba(30,207,170,0.3);
}
.av-user {
    width: 32px; height: 32px; border-radius: 50%; flex-shrink: 0;
    background: #1A2744; border: 1px solid #253555;
    display: flex; align-items: center; justify-content: center;
    font-size: 10px; color: #94A3B8; font-weight: 600;
}
.msg-bot {
    background: #1A2744; color: #CBD5E1;
    padding: 12px 16px; border-radius: 16px 16px 16px 4px;
    font-size: 14px; line-height: 1.6;
    border: 1px solid #253555;
}
.msg-user {
    background: linear-gradient(135deg, #1ECFAA, #17B899);
    color: #0B1629; font-weight: 600;
    padding: 12px 16px; border-radius: 16px 16px 4px 16px;
    font-size: 14px; line-height: 1.6;
}
.msg-bot b, .msg-bot strong { color: #1ECFAA; }

/* ── Progress bar ── */
.pbar-wrap { margin-bottom: 8px; }
.pbar-track {
    height: 3px; background: #1A2744; border-radius: 2px;
    margin-bottom: 5px; overflow: hidden;
}
.pbar-fill {
    height: 100%;
    background: linear-gradient(90deg, #1ECFAA, #1A8EFF);
    border-radius: 2px; transition: width .5s cubic-bezier(0.4, 0, 0.2, 1);
}
.pbar-label { font-size: 11px; color: #4A5E7A; text-align: right; font-weight: 500; }

/* ── Section header ── */
.sec-head {
    font-size: 11px; font-weight: 700; color: #4A5E7A;
    text-transform: uppercase; letter-spacing: .8px;
    display: flex; align-items: center; gap: 10px;
    margin: 20px 0 14px;
}
.sec-head::after {
    content: ''; flex: 1; height: 1px; 
    background: linear-gradient(90deg, #1A2744, transparent);
}

/* ── Table ── */
.sky-table { width: 100%; border-collapse: collapse; font-size: 12px; }
.sky-table thead { background: #0D1E38; }
.sky-table th {
    padding: 10px 14px; text-align: left; color: #4A5E7A;
    font-size: 10px; text-transform: uppercase; letter-spacing: .6px;
    border-bottom: 1px solid #253555; white-space: nowrap; font-weight: 700;
}
.sky-table td {
    padding: 10px 14px; color: #CBD5E1;
    border-bottom: 1px solid #1A2744; white-space: nowrap;
}
.sky-table tr:hover td { background: rgba(30,207,170,0.04); }
.sky-table tr:last-child td { border-bottom: none; }

/* ── Badges ── */
.bdg { display:inline-block; padding:4px 12px; border-radius:20px;
       font-size:11px; font-weight:700; letter-spacing: 0.3px; }
.bdg-sat { background:#1ECFAA15; color:#1ECFAA; border:1px solid #1ECFAA25; }
.bdg-dis { background:#EF444415; color:#F87171; border:1px solid #EF444425; }
.stars { color: #FCD34D; letter-spacing: 1px; }

/* ── Thanks card ── */
.thanks-card {
    background: linear-gradient(135deg, #1A2744, #162038);
    border: 1px solid rgba(30,207,170,.2);
    border-radius: 20px; padding: 32px; text-align: center;
    max-width: 500px; margin: 0 auto;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
.check-circle {
    width: 64px; height: 64px; 
    background: linear-gradient(135deg, rgba(30,207,170,.2), rgba(30,207,170,.05));
    border-radius: 50%; display: flex; align-items: center;
    justify-content: center; margin: 0 auto 16px;
    font-size: 26px; color: #1ECFAA;
    border: 1px solid rgba(30,207,170,.2);
    box-shadow: 0 0 24px rgba(30,207,170,.15);
}

/* ── Footer ── */
.sky-footer {
    background: #0D1E38;
    border-top: 1px solid rgba(255,255,255,0.05);
    padding: 20px 32px;
    display: flex; align-items: center; justify-content: space-between;
    margin-top: 40px;
}
.footer-left { font-size: 12px; color: #4A5E7A; }
.footer-left span { color: #1ECFAA; font-weight: 600; }
.footer-right { display: flex; gap: 16px; }
.footer-link {
    font-size: 11px; color: #4A5E7A; text-decoration: none;
    padding: 4px 10px; border-radius: 6px;
    border: 1px solid #1A2744;
    transition: all 0.2s;
}
.footer-link:hover { color: #1ECFAA; border-color: rgba(30,207,170,.2); }

/* ── Tab styling ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    border-bottom: 1px solid #1A2744;
    padding: 0 32px;
    gap: 0;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #4A5E7A;
    font-size: 13px; font-weight: 600;
    padding: 14px 20px;
    border-bottom: 2px solid transparent;
}
.stTabs [aria-selected="true"] {
    color: #1ECFAA !important;
    border-bottom: 2px solid #1ECFAA !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-highlight"] { display: none; }
.stTabs [data-baseweb="tab-border"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ── Top bar ─────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="logo-wrap">
    <div class="logo-icon">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="#0B1629">
        <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5z"/>
      </svg>
    </div>
    <div>
      <div class="logo-text">SkyRate</div>
      <div class="logo-sub">Airline Intelligence Platform</div>
    </div>
  </div>
  <div class="topbar-right">
    <div class="stage-badge">✈️ Stage 1 · Pre-Flight</div>
    <div class="live-badge"><div class="ldot"></div>Live System</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Hero Section ─────────────────────────────────────────
total = len(st.session_state.submissions)
sat = sum(1 for s in st.session_state.submissions if s.get("Predicted") == "Satisfied")
sat_pct = round(sat / total * 100) if total > 0 else 0

st.markdown(f"""
<div class="hero">
  <div class="hero-title">Passenger Satisfaction <span>Intelligence</span></div>
  <div class="hero-sub">
    AI-powered real-time prediction system. Identify dissatisfied passengers 
    before they board — powered by XGBoost with 90.3% accuracy.
  </div>
  <div class="hero-stats">
    <div class="hero-stat">
      <div class="hero-stat-icon" style="background:rgba(30,207,170,0.1)">🤖</div>
      <div>
        <div class="hero-stat-val">90.3%</div>
        <div class="hero-stat-lbl">Model Accuracy</div>
      </div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-icon" style="background:rgba(26,142,255,0.1)">📊</div>
      <div>
        <div class="hero-stat-val">{total}</div>
        <div class="hero-stat-lbl">Responses Today</div>
      </div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-icon" style="background:rgba(252,211,77,0.1)">😊</div>
      <div>
        <div class="hero-stat-val">{sat_pct}%</div>
        <div class="hero-stat-lbl">Satisfaction Rate</div>
      </div>
    </div>
    <div class="hero-stat">
      <div class="hero-stat-icon" style="background:rgba(248,113,113,0.1)">⚡</div>
      <div>
        <div class="hero-stat-val">~90s</div>
        <div class="hero-stat-lbl">Feedback Time</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Tab navigation ──────────────────────────────────────
tab1, tab2 = st.tabs(["🤖  Passenger Feedback", "📊  Airline Dashboard"])

with tab1:
    import pages.chatbot as chatbot
    chatbot.run()

with tab2:
    import pages.dashboard as dashboard
    dashboard.run()

# ── Footer ──────────────────────────────────────────────
st.markdown("""
<div class="sky-footer">
  <div class="footer-left">
    Built by <span>Kiran U</span> · PGP Data Science & GenAI · Great Learning 2026
  </div>
  <div class="footer-right">
    <a class="footer-link" href="https://www.linkedin.com/in/kiran-u-471818325/" target="_blank">LinkedIn</a>
    <a class="footer-link" href="https://github.com/KIRAN4003" target="_blank">GitHub</a>
    <a class="footer-link" href="mailto:kirankiranu791@gmail.com">Contact</a>
  </div>
</div>
""", unsafe_allow_html=True)