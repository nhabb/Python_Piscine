import matplotlib.pyplot as plt
from load_csv import load


def main():
    try:
        """This program loads a csv file
        and plots the life expactncy graph of lebanon"""
        df = load("life_expectancy_years.csv")
        data = df[df['country'] == 'Lebanon']
        data1 = data.melt(id_vars=["country"],
                          var_name="Year", value_name="Life Expectancy")
        data1['Year'] = data1['Year'].astype(int)
        plt.plot(data1["Year"], data1["Life Expectancy"], label="Lebanon")
        plt.title("Lebanon Life Expectancy Over Time")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
