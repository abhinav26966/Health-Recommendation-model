import logging
from dotenv import load_dotenv
import streamlit as st
from crewai import Crew, Process
from pypdf import PdfReader

from agents import MedicalAnalysisAgents
from tasks import MedicalAnalysisTasks

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_agents_and_tasks():
    agents_factory = MedicalAnalysisAgents()
    tasks_factory = MedicalAnalysisTasks()

    medical_analyst = agents_factory.medical_analyst()
    health_researcher = agents_factory.health_researcher()
    health_advisor = agents_factory.health_advisor()

    analyze_blood_test = tasks_factory.analyze_blood_test(medical_analyst)
    search_for_articles = tasks_factory.search_for_articles(health_researcher)
    provide_recommendations = tasks_factory.provide_recommendations(health_advisor)

    return [medical_analyst, health_researcher, health_advisor], [analyze_blood_test, search_for_articles, provide_recommendations]

def main():
    st.title("Blood 🩸 Test Report - Health 🩺 Recommendation Model")

    uploaded_file = st.file_uploader("GET FILE", type="pdf")

    if uploaded_file is not None:
        text = ""
        try:
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text()
        except Exception as e:
            st.error(f"FILE READING ERROR : {e}")
            logger.error(f"FILE READING ERROR : {e}")
            return

        if st.button("GET RECOMMENDATIONS"):
            st.write("Interpreting report data. Kindly wait for few minutes.")
            logger.info("⌛️ -> ⏳")

            agents, tasks = initialize_agents_and_tasks()

            crew = Crew(
                agents=agents,
                tasks=tasks,
                process=Process.sequential,
                context="Use the results from the previous task as input for the next task."
            )

            with st.spinner("..."):
                try:
                    result = crew.kickoff(inputs={"text": text})
                    logger.info("✅ -> ✔️")
                except Exception as e:
                    st.error(f"UH OH ERROR OCCURRED : {e}")
                    logger.error(f"UH OH ERROR OCCURRED : {e}")
                    return
                
            st.write(result)
            st.subheader("RECOMMENDATIONS ARE HERE 🥙 : ")
            st.markdown(result)
    else:
        st.write("GIVE PDF :")

if __name__ == "__main__":
    main()