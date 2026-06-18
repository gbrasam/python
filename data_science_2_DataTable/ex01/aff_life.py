from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def make_graph(df: pd.DataFrame) -> None:

    year = df.columns[1:]
    life_expectancy = df.iloc[0, 1:]

    plt.plot(year, life_expectancy, label="Spain")
    plt.title("Spain Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.xticks(year[::40])
    plt.legend()
    plt.show()


def main():
    """
    loads life expectancy dataset
    and displays the data for Spain
    (Madrid campus)
    """

    try:
        df = load("../life_expectancy_years.csv")
        if df is None:
            return 0

        spain = df[df["country"] == "Spain"]
        if spain.empty:
            raise ValueError("'Spain' not found in the dataset")

        make_graph(spain)

        return 1

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Error: {error}")

    return 0


if __name__ == "__main__":
    main()
