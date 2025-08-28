import pandas as pd

# Load data
apple = pd.read_excel("data/appl_10k.xlsx")
microsoft = pd.read_excel("data/msft_10k.xlsx")
tesla = pd.read_excel("data/tesla_10k.xlsx")

companies = {
    "apple": apple,
    "microsoft": microsoft,
    "tesla": tesla
}

def simple_chatbot(user_query):
    query = user_query.lower()
    
    if "total revenue" in query:
        for name, df in companies.items():
            if name in query:
                revenue = df.loc[df["Financial Metric"] == "Total Revenue", "Fiscal Year 2024"].values[0]
                return f"{name.title()}'s total revenue in 2024 was ${revenue:,}."
    
    elif "net income" in query and "change" not in query:
        for name, df in companies.items():
            if name in query:
                net_income = df.loc[df["Financial Metric"] == "Net Income", "Fiscal Year 2024"].values[0]
                return f"{name.title()}'s net income in 2024 was ${net_income:,}."
    
    elif "net income" in query and "change" in query:
        for name, df in companies.items():
            if name in query:
                ni_2024 = df.loc[df["Financial Metric"] == "Net Income", "Fiscal Year 2024"].values[0]
                ni_2023 = df.loc[df["Financial Metric"] == "Net Income", "Fiscal Year 2023"].values[0]
                change = ni_2024 - ni_2023
                direction = "increased" if change > 0 else "decreased"
                return f"{name.title()}'s net income {direction} by ${abs(change):,} from 2023 to 2024."
    
    else:
        return "Sorry, I can only provide information on predefined queries."

