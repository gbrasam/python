from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def make_graph(df: pd.DataFrame) -> None:

    year = df.columns[1:]
    print(year)
    start = year.get_loc("1800")
    print(start)
    end = year.get_loc("2050")
    print(end)
    period = year[start:end + 1]
    print(period)

    rows, cols = df.shape
    for i in range(rows):
        population = df.iloc[i, 1:end]
        country = population["country"]
        plt.plot(period, population, label=country)

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(period[::40])
    plt.legend()
    plt.show()


def main():
    """
    loads population dataset, filters
    and cleans data for Spain vs France,
    and displays the comparison from 1800 to 2050
    """

    try:
        df = load("../population_total.csv")
        if df is None:
            return 0

        subset = df[df["country"].isin(["Spain", "France"])]
        if subset.empty:
            raise ValueError("'Spain' or 'France' not found in the dataset")

        # print(subset.values)
        make_graph(subset)

        return 1

    except ValueError as error:
        print(f"Error: {error}")

    except Exception as error:
        print(f"Error: {error}")

    return 0


if __name__ == "__main__":
    main()
