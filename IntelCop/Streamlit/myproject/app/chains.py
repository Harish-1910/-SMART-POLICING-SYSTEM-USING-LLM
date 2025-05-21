import os
import pandas as pd
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="deepseek-r1-distill-llama-70b")
        self.df = pd.read_csv("crime_data_india.csv")

    def analyze_crime_data(self, user_query):
        """Analyze crime data based on user queries, including date-based queries."""

        # Extract date from user query
        extracted_date = self.extract_date(user_query)

        if extracted_date:
            filtered_data = self.df[self.df["Date"] == extracted_date]

            if filtered_data.empty:
                return f"No crime data available for {extracted_date}."

            crime_details = "\n".join(
                f"- On {row['Date']} in {row['Region']}, {row['Number of Cases']} {row['Crime Type']} cases occurred at {row['Time of Day']}. Severity: {row['Severity']}."
                for _, row in filtered_data.iterrows()
            )
            return crime_details

        # Generate summary for general crime queries
        crime_data_summary = self.df.describe(include="all").to_string()

        prompt = PromptTemplate.from_template(
            """
            ### CONTEXT:
            You are an AI crime analyst providing insights based on recorded crime data in India.

            ### USER QUERY:
            {user_query}

            ### DATA SUMMARY:
            {crime_data_summary}

            ### INSTRUCTION:
            - Provide factual insights based on the dataset.
            - If a date is mentioned, extract crime events for that date.
            - Keep responses concise and data-driven.
            """
        )

        chain = prompt | self.llm
        response = chain.invoke({"crime_data_summary": crime_data_summary, "user_query": user_query})
        return response.content

    def extract_date(self, user_query):
        """Extracts a date from the user's query if present."""
        import re
        match = re.search(r"\d{4}-\d{2}-\d{2}", user_query)  # Matches YYYY-MM-DD format
        return match.group(0) if match else None


if __name__ == "__main__":
    chain = Chain()
    print(chain.analyze_crime_data("What happened on 2024-01-15?"))
