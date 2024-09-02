import plotly.express as px


class Main:
    def __init__(self):
        self.estimation = {
            "2005": 750,
            "2010": 900,
            "2020": 1300,
            "2030": 1800,
            "2040": 2700,
            "2050": 4000,
        }

        self.estimation_no_cat = {
            "2005": 750,
            "2010": 900,
            "2020": 1300,
            "2030": 1800,
            "2040": 2700,
            "2050": 4000,
        }

        self.estimation_no_dog = {
            "2005": 750,
            "2010": 900,
            "2020": 1300,
            "2030": 1800,
            "2040": 2700,
            "2050": 4000,
        }

        self.estimation_no_cat_and_dog = {
            "2005": 750,
            "2010": 900,
            "2020": 1300,
            "2030": 1800,
            "2040": 2700,
            "2050": 4000,
        }

        self.cat_emission = 240
        self.dog_emission = 358
        self.nb_cats = 600000000
        self.nb_dogs = 900000000

    @staticmethod
    def transform_to_million_of_tonnes(value):
        return value / (1000000 * 1000)

    def calculate(self):
        for year, value in self.estimation.items():
            self.estimation_no_cat[year] = value - self.transform_to_million_of_tonnes(
                self.cat_emission * self.nb_cats
            )
            self.estimation_no_dog[year] = value - self.transform_to_million_of_tonnes(
                self.dog_emission * self.nb_dogs
            )
            self.estimation_no_cat_and_dog[year] = (
                value
                - self.transform_to_million_of_tonnes(self.cat_emission * self.nb_cats)
                - self.transform_to_million_of_tonnes(self.dog_emission * self.nb_dogs)
            )

    def display(self):
        fig = px.line(
            x=list(self.estimation.keys()),
            y=[
                list(self.estimation.values()),
                list(self.estimation_no_cat.values()),
                list(self.estimation_no_dog.values()),
                list(self.estimation_no_cat_and_dog.values()),
            ],
            labels={
                "x": "Year",
                "y": "CO2 Emission (in million of tonnes)",
                "color": "Legend",
            },
            title="CO2 Emission with and without cats and dogs",
            color_discrete_map={
                "CO2 Emission": "blue",
                "CO2 Emission without cats": "green",
                "CO2 Emission without dogs": "red",
                "CO2 Emission without cats and dogs": "orange",
            },
        )
        fig.show()


if __name__ == "__main__":
    main = Main()
    main.calculate()
    main.display()
