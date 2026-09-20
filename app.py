import html

import streamlit as st

from skill import review_resume


st.set_page_config(
    page_title="مساعد السيرة الذاتية",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        :root {
            --navy: #12305f;
            --blue: #2563eb;
            --mist: #f6f9ff;
            --line: #d9e6f7;
            --ink: #172b4d;
            --muted: #5f7393;
            --white: #ffffff;
        }

        .stApp { direction: rtl; background: var(--mist); color: var(--ink); }
        .block-container { max-width: 1280px; padding-top: 2.4rem; padding-bottom: 3rem; }
        h1, h2, h3, p, label, div[data-testid="stMarkdownContainer"] { direction: rtl; text-align: right; }
        h1, h2, h3 { color: var(--navy) !important; }

        .hero-card {
            background: var(--white); border: 1px solid var(--line); border-top: 5px solid var(--blue);
            border-radius: 18px; box-shadow: 0 12px 30px rgba(18, 48, 95, 0.08);
            margin: 0 auto 2rem; max-width: 900px; padding: 1.6rem 2rem; text-align: center;
        }
        .hero-card h1 { font-size: clamp(1.75rem, 3vw, 2.45rem); letter-spacing: -0.02em; margin: 0.65rem 0 0.4rem; text-align: center; }
        .hero-card p { color: var(--muted); font-size: 1rem; margin: 0; text-align: center; }
        .hero-badge, .skill-badge {
            display: inline-block; background: #e3efff; border: 1px solid #bcd7ff; border-radius: 999px;
            color: #1d4ed8; font-size: 0.82rem; font-weight: 700; padding: 0.32rem 0.75rem;
        }
        .column-title { color: var(--navy); font-size: 1.15rem; font-weight: 800; margin: 0 0 0.8rem; }

        div[data-testid="stTextArea"] textarea {
            background: var(--white) !important; border: 1px solid #c9dbf2 !important; border-radius: 12px !important;
            box-shadow: 0 3px 12px rgba(18, 48, 95, 0.04); color: var(--ink) !important;
            direction: rtl !important; line-height: 1.8; padding: 1rem !important; text-align: right !important;
        }
        div[data-testid="stTextArea"] textarea:focus {
            border-color: var(--blue) !important; box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.14) !important;
        }

        .stButton > button { border-radius: 10px; font-weight: 700; min-height: 2.7rem; transition: background 0.18s ease, transform 0.18s ease, box-shadow 0.18s ease; }
        .stButton > button[kind="secondary"] { background: var(--white); border: 1px solid #c9dbf2; color: #24519a; }
        .stButton > button[kind="primary"] { background: var(--blue); border: 1px solid var(--blue); box-shadow: 0 7px 15px rgba(37, 99, 235, 0.22); color: var(--white); }
        .stButton > button:hover { transform: translateY(-1px); }
        .stButton > button[kind="primary"]:hover { background: #1d4ed8; }
        .stButton > button:focus-visible { outline: 3px solid #93c5fd; outline-offset: 2px; }

        .metric-card { background: #f1f6ff; border: 1px solid #d4e3f8; border-radius: 12px; padding: 0.85rem 1rem; text-align: center; }
        .metric-card span { color: var(--muted); font-size: 0.82rem; }
        .metric-card strong { color: var(--navy); display: block; font-size: 1.45rem; margin-top: 0.15rem; }
        .result-card { background: var(--white); border: 1px solid var(--line); border-radius: 14px; box-shadow: 0 7px 18px rgba(18, 48, 95, 0.05); margin-top: 1rem; padding: 1.2rem; }
        .result-card h3 { font-size: 1rem; margin: 0 0 0.8rem; }
        .skills-list { display: flex; flex-wrap: wrap; gap: 0.55rem; }
        .empty-state { color: var(--muted); margin: 0; }
        .recommendation { background: #f3f7ff; border-right: 4px solid #60a5fa; border-radius: 8px; color: var(--ink); margin-top: 0.55rem; padding: 0.7rem 0.85rem; }
        .quality-card { background: linear-gradient(135deg, #12305f, #1e4f9f); border-radius: 14px; color: var(--white); padding: 1.2rem; }
        .quality-card h3, .quality-card p { color: var(--white) !important; margin: 0; }
        .quality-card p { font-size: 0.88rem; opacity: 0.8; margin-top: 0.25rem; }
        .quality-track { background: rgba(255, 255, 255, 0.22); border-radius: 999px; height: 9px; margin-top: 1rem; overflow: hidden; }
        .quality-fill { background: #93c5fd; border-radius: inherit; height: 100%; }
        .quality-score { float: left; font-size: 1.35rem; font-weight: 800; }
        div[data-testid="stAlert"] { border-radius: 10px; }
        @media (max-width: 700px) { .block-container { padding: 1rem; } .hero-card { padding: 1.25rem 1rem; } }
        @media (prefers-reduced-motion: reduce) { .stButton > button { transition: none; } }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="hero-card">
        <span class="hero-badge">تحليل واضح لسيرتك الذاتية</span>
        <h1>مساعد السيرة الذاتية</h1>
        <p>اكتشف مهاراتك التقنية واحصل على ملاحظات عملية لتحسين سيرتك.</p>
    </section>
    """,
    unsafe_allow_html=True,
)

sample_cv = """أحمد محمد
مطور برمجيات بخبرة 3 سنوات في تطوير تطبيقات الويب.

المهارات: Python، Streamlit، JavaScript، SQL، Git، تحليل البيانات.
الخبرات: تطوير لوحات معلومات تفاعلية وتحسين أداء التطبيقات."""

if "cv_text" not in st.session_state:
    st.session_state.cv_text = sample_cv
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

# في RTL يُعرض العمود الأول في الجهة اليمنى.
input_col, results_col = st.columns((1.05, 0.95), gap="large")

with input_col:
    st.markdown('<p class="column-title">📝 أدخل السيرة الذاتية</p>', unsafe_allow_html=True)
    load_col, quick_col = st.columns(2)
    with load_col:
        load_sample = st.button("تحميل سيرة ذاتية تجريبية", use_container_width=True)
    with quick_col:
        analyze_sample = st.button("تحليل المثال فوراً", use_container_width=True)

    if load_sample or analyze_sample:
        st.session_state.cv_text = sample_cv
        if load_sample:
            st.session_state.analysis_result = None

    cv_text = st.text_area(
        "نص السيرة الذاتية", height=355, placeholder="الصق نص سيرتك الذاتية هنا…",
        key="cv_text", label_visibility="collapsed",
    )
    analyze_cv = st.button("تحليل السيرة الذاتية", type="primary", use_container_width=True)

    if analyze_cv or analyze_sample:
        if cv_text.strip():
            st.session_state.analysis_result = review_resume(cv_text)
        else:
            st.session_state.analysis_result = None
            st.error("أدخل نص السيرة الذاتية أولاً ثم أعد التحليل.")

with results_col:
    st.markdown('<p class="column-title">📊 نتائج التحليل</p>', unsafe_allow_html=True)
    result = st.session_state.analysis_result

    if result:
        skills = result.get("extracted_skills", [])
        suggestions = result.get("suggestions", [])
        quality_score = min(95, 42 + len(skills) * 11)
        st.markdown(
            f"""<section class="quality-card"><span class="quality-score">{quality_score}%</span>
            <h3>مؤشر جودة السيرة الذاتية</h3><p>تقدير مبدئي مبني على حضور المهارات التقنية المعروفة.</p>
            <div class="quality-track"><div class="quality-fill" style="width: {quality_score}%"></div></div></section>""",
            unsafe_allow_html=True,
        )

        skills_metric, suggestions_metric = st.columns(2)
        with skills_metric:
            st.markdown(f'<div class="metric-card"><span>المهارات المكتشفة</span><strong>{len(skills)}</strong></div>', unsafe_allow_html=True)
        with suggestions_metric:
            st.markdown(f'<div class="metric-card"><span>الملاحظات</span><strong>{len(suggestions)}</strong></div>', unsafe_allow_html=True)

        skills_content = "".join(f'<span class="skill-badge">{html.escape(skill)}</span>' for skill in skills)
        if not skills_content:
            skills_content = '<p class="empty-state">لم نكتشف مهارات من القائمة الحالية.</p>'
        st.markdown(
            f'<section class="result-card"><h3>المهارات المكتشفة</h3><div class="skills-list">{skills_content}</div></section>',
            unsafe_allow_html=True,
        )

        recommendations = "".join(f'<div class="recommendation">{html.escape(suggestion)}</div>' for suggestion in suggestions)
        st.markdown(
            f'<section class="result-card"><h3>التوصيات والملاحظات</h3>{recommendations}</section>',
            unsafe_allow_html=True,
        )
    else:
        st.info("ضع سيرتك الذاتية في الحقل المقابل، ثم اختر «تحليل السيرة الذاتية» لعرض النتائج.")
