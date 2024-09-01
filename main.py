import pandas as pd
from sqlalchemy import create_engine, text
import plotly.express as px


class Main:
    def __init__(self):
        self.result = None
        self.connection = None

        self.engine = create_engine("sqlite:///my_database.db", echo=False)
        self.df = pd.read_csv("website_wata.csv")
        self.df.to_sql("website_data", self.engine, index=False, if_exists="append")
        self.get_data()
        self.transform_data()
        self.display_graph()


    def get_data(self):
        self.connection = self.engine.connect()
        query = text("SELECT Page_Views, Time_on_Page FROM website_data")
        self.result = self.connection.execute(query).fetchall()

    def transform_data(self):
        for i in range(len(self.result)):
            self.result[i] = list(self.result[i])


    def display_graph(self):
        fig = px.scatter(
            self.result, x=0, y=1, title=""
        )
        fig.show()


Main()