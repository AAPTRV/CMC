import pandas as pd
day = "d"
week = "w"
month = "m"

schedule = {
    "20% at TGE, 90 days cliff then linear vesting for 12 months": [["0", 0.2],
                                                                    [f"4{month}", 0.066],  # linear vesting (1)
                                                                    [f"1{month}", 0.066],  # linear vesting (2)
                                                                    [f"1{month}", 0.066],  # linear vesting (3)
                                                                    [f"1{month}", 0.066],  # linear vesting (4)
                                                                    [f"1{month}", 0.066],  # linear vesting (5)
                                                                    [f"1{month}", 0.066],  # linear vesting (6)
                                                                    [f"1{month}", 0.066],  # linear vesting (7)
                                                                    [f"1{month}", 0.066],  # linear vesting (8)
                                                                    [f"1{month}", 0.066],  # linear vesting (9)
                                                                    [f"1{month}", 0.066],  # linear vesting (10)
                                                                    [f"1{month}", 0.066],  # linear vesting (11)
                                                                    [f"1{month}", 0.066]],  # linear vesting (12)

    "50% at TGE, 60 days cliff then 5% monthly":                   [["0", 0.2],
                                                                    [f"4{month}", 0.066],  # linear vesting (1)
                                                                    [f"1{month}", 0.066],  # linear vesting (2)
                                                                    [f"1{month}", 0.066],  # linear vesting (3)
                                                                    [f"1{month}", 0.066],  # linear vesting (4)
                                                                    [f"1{month}", 0.066],  # linear vesting (5)
                                                                    [f"1{month}", 0.066],  # linear vesting (6)
                                                                    [f"1{month}", 0.066],  # linear vesting (7)
                                                                    [f"1{month}", 0.066],  # linear vesting (8)
                                                                    [f"1{month}", 0.066],  # linear vesting (9)
                                                                    [f"1{month}", 0.066],  # linear vesting (10)
                                                                    [f"1{month}", 0.066],  # linear vesting (11)
                                                                    [f"1{month}", 0.066]],  # linear vesting (12)

    "Seed Round:10% at TGE, 150 days cliff then linear vesting for 25 Months": [["0", 0.1],
                                                                    [f"150{day}", 0.036],  # linear vesting (1)
                                                                    [f"1{month}", 0.036],  # linear vesting (2)
                                                                    [f"1{month}", 0.036],  # linear vesting (3)
                                                                    [f"1{month}", 0.036],  # linear vesting (4)
                                                                    [f"1{month}", 0.036],  # linear vesting (5)
                                                                    [f"1{month}", 0.036],  # linear vesting (6)
                                                                    [f"1{month}", 0.036],  # linear vesting (7)
                                                                    [f"1{month}", 0.036],  # linear vesting (8)
                                                                    [f"1{month}", 0.036],  # linear vesting (9)
                                                                    [f"1{month}", 0.036],  # linear vesting (10)
                                                                    [f"1{month}", 0.036],  # linear vesting (11)
                                                                    [f"1{month}", 0.036],  # linear vesting (12)
                                                                    [f"1{month}", 0.036],  # linear vesting (13)
                                                                    [f"1{month}", 0.036],  # linear vesting (14)
                                                                    [f"1{month}", 0.036],  # linear vesting (15)
                                                                    [f"1{month}", 0.036],  # linear vesting (16)
                                                                    [f"1{month}", 0.036],  # linear vesting (17)
                                                                    [f"1{month}", 0.036],  # linear vesting (18)
                                                                    [f"1{month}", 0.036],  # linear vesting (19)
                                                                    [f"1{month}", 0.036],  # linear vesting (20)
                                                                    [f"1{month}", 0.036],  # linear vesting (21)
                                                                    [f"1{month}", 0.036],  # linear vesting (22)
                                                                    [f"1{month}", 0.036],  # linear vesting (23)
                                                                    [f"1{month}", 0.036],  # linear vesting (24)
                                                                    [f"1{month}", 0.036]], # linear vesting (25)

    "Public:25% at TGE, then 25% at month 2, 4, and 6":             [["0", 0.25],
                                                                     [f"2{month}", 0.25],  # linear vesting (1)
                                                                     [f"2{month}", 0.25],  # linear vesting (2)
                                                                     [f"2{month}", 0.25]], # linear vesting (3)

    "Public Sale:50% at TGE, 50% release 30 days after":            [["0", 0.5],
                                                                     [f"1{month}", 0.5]],  # linear vesting (1)

    "Public Sale:10% at TGE, 90 days cliff then 5% monthly":       [["0", 0.1],
                                                                    [f"1{month}", 0.05],  # linear vesting (1)
                                                                    [f"1{month}", 0.05],  # linear vesting (2)
                                                                    [f"1{month}", 0.05],  # linear vesting (3)
                                                                    [f"1{month}", 0.05],  # linear vesting (4)
                                                                    [f"1{month}", 0.05],  # linear vesting (5)
                                                                    [f"1{month}", 0.05],  # linear vesting (6)
                                                                    [f"1{month}", 0.05],  # linear vesting (7)
                                                                    [f"1{month}", 0.05],  # linear vesting (8)
                                                                    [f"1{month}", 0.05],  # linear vesting (9)
                                                                    [f"1{month}", 0.05],  # linear vesting (10)
                                                                    [f"1{month}", 0.05],  # linear vesting (11)
                                                                    [f"1{month}", 0.05],  # linear vesting (12)
                                                                    [f"1{month}", 0.05],  # linear vesting (13)
                                                                    [f"1{month}", 0.05],  # linear vesting (14)
                                                                    [f"1{month}", 0.05],  # linear vesting (15)
                                                                    [f"1{month}", 0.05],  # linear vesting (16)
                                                                    [f"1{month}", 0.05],  # linear vesting (17)
                                                                    [f"1{month}", 0.05]], # linear vesting (18)

    "Seed Round:10% at TGE, 60 days cliff then 4.50% monthly": [["0", 0.1],
                                                                    [f"1{month}", 0.045],  # linear vesting (1)
                                                                    [f"1{month}", 0.045],  # linear vesting (2)
                                                                    [f"1{month}", 0.045],  # linear vesting (3)
                                                                    [f"1{month}", 0.045],  # linear vesting (4)
                                                                    [f"1{month}", 0.045],  # linear vesting (5)
                                                                    [f"1{month}", 0.045],  # linear vesting (6)
                                                                    [f"1{month}", 0.045],  # linear vesting (7)
                                                                    [f"1{month}", 0.045],  # linear vesting (8)
                                                                    [f"1{month}", 0.045],  # linear vesting (9)
                                                                    [f"1{month}", 0.045],  # linear vesting (10)
                                                                    [f"1{month}", 0.045],  # linear vesting (11)
                                                                    [f"1{month}", 0.045],  # linear vesting (12)
                                                                    [f"1{month}", 0.045],  # linear vesting (13)
                                                                    [f"1{month}", 0.045],  # linear vesting (14)
                                                                    [f"1{month}", 0.045],  # linear vesting (15)
                                                                    [f"1{month}", 0.045],  # linear vesting (16)
                                                                    [f"1{month}", 0.045],  # linear vesting (17)
                                                                    [f"1{month}", 0.045],  # linear vesting (18)
                                                                    [f"1{month}", 0.045],  # linear vesting (19)
                                                                    [f"1{month}", 0.045]], # linear vesting (20)


}

df = pd.read_csv("/Users/eaxes/DA Projects/CMC/data/collected_data/mined/price_token_test_slug.csv")
print(df.schedule.unique())