
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
    "Public:25% at TGE, then 25% at month 2, 4, and 6":             [["0", 0.25],
                                                                     [f"2{month}", 0.25],  # linear vesting (1)
                                                                     [f"2{month}", 0.25],  # linear vesting (2)
                                                                     [f"2{month}", 0.25]] # linear vesting (3)

}