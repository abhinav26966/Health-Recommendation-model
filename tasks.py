from crewai import Task

class MedicalAnalysisTasks:
    @staticmethod
    def analyze_blood_test(agent):
        return Task(
            description='Details of patient on the top then analyze the extracted text from the blood test report and provide a summary.',
            expected_output='Details of patient on the top, summary of the blood test in simple terms.',
            agent=agent
        )

    @staticmethod
    def search_for_articles(agent):
        return Task(
            description='Search the web for articles relevant to the health issues identified in the blood test summary.',
            expected_output='A list of articles with URLs and a brief description of each.',
            agent=agent
        )

    @staticmethod
    def provide_recommendations(agent):
        return Task(
            description='''
                Provide health recommendations based on the articles and blood test summary.
                Give health recommendations and provide links to the relevant articles.
            ''',
            expected_output='''
                A short and concise paragraph summary of the blood report in simple easy-to-understand terms 
                followed by a bullet list of actionable health recommendations, with each bullet point containing 
                links to its source.

                ## Summary
                [Provide a simple short summary of the blood report here]

                ## Recommendations
                - [Recommendation 1](https://source1.com)
                - [Recommendation 2](https://source2.com)
                - [Recommendation 3](https://source3.com)
            ''',
            agent=agent
        )