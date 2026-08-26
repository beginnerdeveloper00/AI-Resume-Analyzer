import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.matcher import calculate_match
from utils.resume_analyzer import analyze_resume, calculate_resume_quality


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

    .main-title {
        font-size: 45px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 650;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .match-card {
        background-color: #123524;
        border-radius: 10px;
        padding: 15px;
        margin: 8px 0;
        border: 1px solid #1f6b45;
    }

    .missing-card {
        background-color: #3b2025;
        border-radius: 10px;
        padding: 15px;
        margin: 8px 0;
        border: 1px solid #7a303a;
    }

    .info-card {
        background-color: #20212a;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #343541;
        margin-bottom: 15px;
    }

</style>
""", unsafe_allow_html=True)


# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="main-title">📄 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze your resume, compare it with a job description and discover missing skills.</div>',
    unsafe_allow_html=True
)


# =====================================================
# RESUME UPLOAD
# =====================================================

st.markdown(
    '<div class="section-title">📄 Upload Your Resume</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf"]
)


# =====================================================
# JOB DESCRIPTION
# =====================================================

st.markdown(
    '<div class="section-title">💼 Job Description</div>',
    unsafe_allow_html=True
)

job_description = st.text_area(
    "Paste the Job Description here",
    height=250,
    placeholder="Paste the job description here..."
)


# =====================================================
# ANALYZE BUTTON
# =====================================================

analyze_button = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)


# =====================================================
# ANALYSIS
# =====================================================

if analyze_button:

    # -------------------------------------------------
    # VALIDATION
    # -------------------------------------------------

    if uploaded_file is None:

        st.warning(
            "⚠️ Please upload your resume first."
        )

    elif not job_description.strip():

        st.warning(
            "⚠️ Please paste the Job Description first."
        )

    else:

        # -------------------------------------------------
        # EXTRACT AND ANALYZE RESUME
        # -------------------------------------------------

        try:

            with st.spinner("🔍 Analyzing your resume..."):

                resume_text = extract_text_from_pdf(
                    uploaded_file
                )

                resume_results = analyze_resume(
                    resume_text
                )

                quality_score = calculate_resume_quality(
                    resume_results
                )

                score, matching_skills, missing_skills = calculate_match(
                    resume_text,
                    job_description
                )

        except ValueError as error:

            st.error(f"❌ {error}")
            st.stop()

        except Exception:

            st.error(
                "❌ Something went wrong while analyzing your resume. "
                "Please try another PDF file."
            )
            st.stop()

        st.success(
            "✅ Resume analyzed successfully!"
        )


        # =================================================
        # SCORE SECTION
        # =================================================

        st.markdown(
            '<div class="section-title">📊 Resume Scores</div>',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown(
                '<div class="info-card">',
                unsafe_allow_html=True
            )

            st.metric(
                "📋 Resume Quality",
                f"{quality_score}%"
            )

            st.progress(
                min(max(int(quality_score), 0), 100)
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                '<div class="info-card">',
                unsafe_allow_html=True
            )

            st.metric(
                "🎯 ATS Match Score",
                f"{score}%"
            )

            st.progress(
                min(max(int(score), 0), 100)
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


        # =================================================
        # RESUME QUALITY DETAILS
        # =================================================

        st.markdown(
            '<div class="section-title">📋 Resume Quality Details</div>',
            unsafe_allow_html=True
        )

        quality_col1, quality_col2 = st.columns(2)

        sections = list(resume_results.items())

        for index, (section, completed) in enumerate(sections):

            if index % 2 == 0:

                with quality_col1:

                    if completed:

                        st.success(
                            f"✅ {section}"
                        )

                    else:

                        st.warning(
                            f"⚠️ {section}"
                        )

            else:

                with quality_col2:

                    if completed:

                        st.success(
                            f"✅ {section}"
                        )

                    else:

                        st.warning(
                            f"⚠️ {section}"
                        )


        # =================================================
        # MATCHING SKILLS
        # =================================================

        st.markdown(
            '<div class="section-title">✅ Matching Skills</div>',
            unsafe_allow_html=True
        )

        if matching_skills:

            skill_columns = st.columns(3)

            for index, skill in enumerate(matching_skills):

                with skill_columns[index % 3]:

                    st.markdown(
                        f"""
                        <div class="match-card">
                            ✅ <b>{skill.title()}</b>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        else:

            st.info(
                "No matching skills found."
            )


        # =================================================
        # MISSING SKILLS
        # =================================================

        st.markdown(
            '<div class="section-title">❌ Missing Skills</div>',
            unsafe_allow_html=True
        )

        if missing_skills:

            skill_columns = st.columns(3)

            for index, skill in enumerate(missing_skills):

                with skill_columns[index % 3]:

                    st.markdown(
                        f"""
                        <div class="missing-card">
                            ❌ <b>{skill.title()}</b>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        else:

            st.success(
                "🎉 No major missing skills found!"
            )


        # =================================================
        # IMPROVEMENT SUGGESTIONS
        # =================================================

        st.markdown(
            '<div class="section-title">💡 Improvement Suggestions</div>',
            unsafe_allow_html=True
        )

        if missing_skills:

            for skill in missing_skills:

                st.info(
                    f"Consider adding **{skill.title()}** "
                    "to your resume if you have relevant knowledge or experience."
                )

        else:

            st.success(
                "🎉 Your resume covers all major skills "
                "required by this job description."
            )


        # =================================================
        # RESUME QUALITY SUGGESTIONS
        # =================================================

        incomplete_sections = [
            section
            for section, completed in resume_results.items()
            if not completed
        ]

        if incomplete_sections:

            st.markdown(
                '<div class="section-title">⚠️ Resume Sections to Improve</div>',
                unsafe_allow_html=True
            )

            for section in incomplete_sections:

                st.warning(
                    f"Consider improving your **{section}** section."
                )


        # =================================================
        # EXTRACTED RESUME TEXT
        # =================================================

        st.markdown(
            '<div class="section-title">📃 Extracted Resume Text</div>',
            unsafe_allow_html=True
        )

        with st.expander(
            "View extracted resume text"
        ):

            st.text_area(
                "Resume Content",
                resume_text,
                height=500
            )


        # =================================================
        # FINAL MESSAGE
        # =================================================

        st.success(
            "🎯 Analysis complete! Use the missing skills and suggestions above to improve your resume."
        )