from clickhouse_driver import Client

all = [
    ("ch_master", "91"),
    ("ch-sub-1", "92"),
    ("ch-sub-2", "92"),

]

#SLave###########################################################################################################################3
for alls in all:
    client = Client(alls[0], port=alls[1])

    client.execute("DROP DATABASE wb")

