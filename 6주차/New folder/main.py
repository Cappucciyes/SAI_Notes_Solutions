import pandas as pd

db_cols = ['date', 'produce', 'exported',
           'export_price', 'imported', 'import_price', 'profit']

jejuProduce = {'감귤': 'TG', '브로콜리': 'BC', '무': 'RD', '당근': 'CR', '양배추': 'CB'}

jejuDb = pd.read_csv("open/international_trade.csv", names=db_cols, header=1)
jejuDb["produce"] = jejuDb["produce"].map(jejuProduce)

jejuDb = jejuDb[(jejuDb["produce"] == "TG") | (jejuDb["produce"] == "BC") | (
    jejuDb["produce"] == "RD") | (jejuDb["produce"] == "CR") | (jejuDb["produce"] == "CB")]

jejuDb.insert(loc=jejuDb.columns.get_loc("export_price") + 1, column="export_price_per_kg",
              value=jejuDb.apply(lambda row: (row["export_price"] * 1000) / row["exported"] if row["exported"] != 0 else None, axis=1))
jejuDb.insert(loc=jejuDb.columns.get_loc("import_price") + 1, column="import_price_per_kg",
              value=jejuDb.apply(lambda row: (row["import_price"] * 1000) / row["imported"] if row["imported"] != 0 else None, axis=1))
jejuDb.insert(loc=jejuDb.columns.get_loc("date") + 1, column="year",
              value=jejuDb.apply(lambda row: int(row["date"][:4])))

print(jejuDb)

# jejuDb["import_price_per_kg"] = jejuDb.apply(
#     lambda row: (row["export_price"] * 1000) / row["exported"], axis=1)

# tgDB = jejuDb[(jejuDb["produce"] == "TG")].groupby("date")

# for grouped, db in tgDB:
#     print(db)
