from ft_filter import ft_filter


def main():
    numbers = [1, 2, 3, 4, 5]

    print(f"ft_filter():\n{ft_filter(lambda x: x % 2 == 0, numbers)}")
    print(f"original:\n{list(filter(lambda x: x % 2 == 0, numbers))}")

    test = [0, 1, "", "hello", False, True]

    print(f"ft_filter():\n{ft_filter(None, test)}")
    print(f"original:\n{list(filter(None, test))}")


if __name__ == "__main__":
    main()
