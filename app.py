
import streamlit as st
from src.pipelines.pipelines import run_search_pipeline


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Research Studio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main Background */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }

    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero Section */
    .hero {
        padding: 40px;
        border-radius: 20px;
        background: linear-gradient(
            135deg,
            #4F46E5,
            #7C3AED,
            #2563EB
        );
        margin-bottom: 30px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    }

    .hero h1 {
        font-size: 48px;
        font-weight: 800;
        margin-bottom: 10px;
        color: white;
    }

    .hero p {
        font-size: 18px;
        opacity: 0.9;
        color: white;
    }

    /* Agent Cards */
    .agent-card {
        background-color: #161B22;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        transition: 0.3s;
        min-height: 150px;
    }

    .agent-card:hover {
        border-color: #6366F1;
        transform: translateY(-3px);
    }

    .agent-icon {
        font-size: 35px;
        margin-bottom: 10px;
    }

    .agent-title {
        font-size: 18px;
        font-weight: 700;
    }

    .agent-description {
        font-size: 14px;
        color: #9CA3AF;
        margin-top: 5px;
    }

    /* Section Titles */
    .section-title {
        font-size: 26px;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    /* Input */
    .stTextInput input {
        border-radius: 12px;
        border: 1px solid #374151;
        padding: 14px;
        font-size: 16px;
    }

    /* Buttons */
    .stButton button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-size: 16px;
        font-weight: 700;
        border: none;
        background: linear-gradient(
            90deg,
            #4F46E5,
            #7C3AED
        );
        color: white;
        transition: 0.3s;
    }

    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0px 5px 20px rgba(124, 58, 237, 0.4);
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 10px;
        padding-left: 20px;
        padding-right: 20px;
    }

    /* Report Container */
    .report-box {
        background-color: #161B22;
        border: 1px solid #30363D;
        border-radius: 15px;
        padding: 25px;
        margin-top: 15px;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #111827;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="hero">

<h1>🧠 AI Research Studio</h1>

<p>
An intelligent multi-agent research system that searches,
scrapes, analyzes, writes, and critiques information automatically.
</p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.title("⚙️ Research Pipeline")

    st.markdown("---")

    st.markdown("### 🤖 Active Agents")

    st.markdown("""
    🔎 **Search Agent**

    Finds reliable information across the web.

    ---

    🌐 **Scraping Agent**

    Extracts useful information from selected sources.

    ---

    ✍️ **Writer Agent**

    Creates a structured research report.

    ---

    🧐 **Critic Agent**

    Reviews and evaluates the final report.
    """)

    st.markdown("---")

    st.caption("AI Research Studio • Multi-Agent System")


# =========================================================
# AGENT OVERVIEW
# =========================================================

st.markdown(
    '<div class="section-title">Research Pipeline</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown("""
    <div class="agent-card">

    <div class="agent-icon">🔎</div>

    <div class="agent-title">
    Search Agent
    </div>

    <div class="agent-description">
    Finds reliable information
    </div>

    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="agent-card">

    <div class="agent-icon">🌐</div>

    <div class="agent-title">
    Scraping Agent
    </div>

    <div class="agent-description">
    Extracts valuable content
    </div>

    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="agent-card">

    <div class="agent-icon">✍️</div>

    <div class="agent-title">
    Writer Agent
    </div>

    <div class="agent-description">
    Generates research reports
    </div>

    </div>
    """, unsafe_allow_html=True)


with col4:

    st.markdown("""
    <div class="agent-card">

    <div class="agent-icon">🧐</div>

    <div class="agent-title">
    Critic Agent
    </div>

    <div class="agent-description">
    Reviews report quality
    </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# RESEARCH INPUT
# =========================================================

st.markdown(
    '<div class="section-title">Start Your Research</div>',
    unsafe_allow_html=True
)


topic = st.text_input(
    "Research Topic",
    placeholder="Example: The impact of Artificial Intelligence on modern healthcare",
    label_visibility="collapsed"
)


# =========================================================
# RUN PIPELINE
# =========================================================

if st.button("🚀 Generate Research Report"):

    if not topic.strip():

        st.warning("⚠️ Please enter a research topic.")

    else:

        try:

            st.markdown("---")

            st.subheader("⚡ AI Agents Working")


            # Agent status area
            status_container = st.empty()

            progress_bar = st.progress(0)


            with st.spinner("Initializing research pipeline..."):

                status_container.info(
                    "🔎 Search Agent is analyzing the web..."
                )

                progress_bar.progress(20)


                # Run pipeline
                result = run_search_pipeline(topic)


                status_container.success(
                    "✅ Research pipeline completed successfully!"
                )

                progress_bar.progress(100)


            st.balloons()


            # =========================================================
            # RESULTS
            # =========================================================

            st.markdown("---")

            st.markdown(
                '<div class="section-title">Research Results</div>',
                unsafe_allow_html=True
            )


            tab1, tab2, tab3, tab4 = st.tabs([
                "🔎 Search",
                "🌐 Scraping",
                "📝 Report",
                "🧐 Critic"
            ])


            # =========================================================
            # SEARCH RESULTS
            # =========================================================

            with tab1:

                st.markdown("### 🔎 Search Agent Results")

                st.markdown(
                    '<div class="report-box">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    result.get(
                        "search_result",
                        "No search results available."
                    )
                )

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


            # =========================================================
            # SCRAPING RESULTS
            # =========================================================

            with tab2:

                st.markdown("### 🌐 Scraped Information")

                st.markdown(
                    '<div class="report-box">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    result.get(
                        "scrape_result",
                        "No scraped information available."
                    )
                )

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


            # =========================================================
            # FINAL REPORT
            # =========================================================

            with tab3:

                st.markdown("### 📝 Final Research Report")

                report = result.get(
                    "report",
                    "No report generated."
                )

                st.markdown(
                    '<div class="report-box">',
                    unsafe_allow_html=True
                )

                st.markdown(report)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown("### 📥 Export Report")

                st.download_button(
                    label="Download Research Report",
                    data=str(report),
                    file_name="ai_research_report.txt",
                    mime="text/plain",
                    use_container_width=True
                )


            # =========================================================
            # CRITIC RESULTS
            # =========================================================

            with tab4:

                st.markdown("### 🧐 Critic Agent Review")

                critic = result.get(
                    "critic",
                    "No critic feedback available."
                )

                st.markdown(
                    '<div class="report-box">',
                    unsafe_allow_html=True
                )

                st.markdown(critic)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


        except Exception as e:

            st.error("❌ Something went wrong while running the research pipeline.")

            with st.expander("View Error Details"):
                st.exception(e)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align: center; color: #9CA3AF;">
        🧠 AI Research Studio • Powered by Multi-Agent AI
    </div>
    """,
    unsafe_allow_html=True
)

