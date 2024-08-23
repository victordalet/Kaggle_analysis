import pandas as pd
from sqlalchemy import create_engine, text
import plotly.express as px


class Main:
    def __init__(self):
        self.result = None
        self.connection = None

        self.engine = create_engine("sqlite:///my_database.db", echo=False)
        self.df = pd.read_csv("amazon_product.csv")
        self.df.to_sql("products", self.engine, index=False, if_exists="append")

        self.get_data()
        self.transform_data()
        self.display_graph()
        self.get_data_number_start_and_price()
        self.transform_data()
        self.display_graph()
        self.get_data_number_start_and_start()
        self.display_graph()

    def get_data(self):
        self.connection = self.engine.connect()
        query = text(
            "SELECT product_price, product_star_rating FROM products where product_price != '$0.00'"
        )
        self.result = self.connection.execute(query).fetchall()

    def get_data_number_start_and_price(self):
        query = text(
            "SELECT product_price, product_num_ratings FROM products where product_price != '$0.00'"
        )
        self.result = self.connection.execute(query).fetchall()

    def get_data_number_start_and_start(self):
        query = text(
            "SELECT product_star_rating, product_num_ratings FROM products where product_price != '$0.00'"
        )
        self.result = self.connection.execute(query).fetchall()
        for i in range(len(self.result)):
            self.result[i] = [self.result[i][0], self.result[i][1]]

    def transform_data(self):
        for i in range(len(self.result)):
            self.result[i] = [float(self.result[i][0].split("$")[1]), self.result[i][1]]

    def display_graph(self):
        fig = px.scatter(
            self.result, x=0, y=1, title="Amazon Product Price vs Star Rating"
        )
        fig.show()


Main()
