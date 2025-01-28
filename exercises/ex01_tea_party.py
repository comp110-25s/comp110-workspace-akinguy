""" Tea Party Planner! """

__author__ = "730710295"


def main_planner(guests: int) -> None:
    """Main Planner for TeaParty and Produces Output"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Compute Number of Teabags Needed"""
    return people * 2


def treats(people: int) -> int:
    """Compute Number of Treats Needed Per Teabag"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Compute Total Cost of Treats and Teabags"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
