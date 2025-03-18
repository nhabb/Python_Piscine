import matplotlib.pyplot as plt
from load_csv import load


def main():
    """This program loads the CSV files
    and plots the scater graph"""
    try:
        gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy = load("life_expectancy_years.csv")
        plt.scatter(gdp["1900"], life_expectancy["1900"])
        plt.xscale("log")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
