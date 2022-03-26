import pandas as pd
from pandera import Check, Column, DataFrameSchema

# Note that ints with possible values are cast as float this is consistent
# with how pandas handle missing values. This requires setting coerce=True.
# Otherwise, we get an error when an integer column that previously had NaNs
# has no NaNs in a fresh dataset -- we'll get an error when a pure int column
# is validated as float. We define a helper function which checks if such a
# column has actual integer contents.


def nullable_int_column(x: pd.Series) -> pd.Series:
    return x.dropna().astype(int) == x.dropna()


HouseDataInputSchema = DataFrameSchema(
    {
        "Alley": Column(str, Check.isin(["Grvl", "Pave", "NA"])),
        "BedroomAbvGr": Column(int, Check.ge(0)),
        "BldgType": Column(
            str, Check.isin(["1Fam", "2FmCon", "Duplx", "TwnhsE", "TwnhsI"])
        ),
        "BsmtCond": Column(str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po", "NA"])),
        "BsmtExposure": Column(
            str, Check.isin(["Gd", "Av", "Mn", "No", "NA"]), nullable=True
        ),
        "BsmtFinSF1": Column(float, Check.ge(0)),
        "BsmtFinSF2": Column(float, Check.ge(0)),
        "BsmtFinType1": Column(
            str,
            Check.isin(["GLQ", "ALQ", "BLQ", "Rec", "LwQ", "Unf", "NA"]),
            nullable=True,
        ),
        "BsmtFinType2": Column(
            str, Check.isin(["GLQ", "ALQ", "BLQ", "Rec", "LwQ", "Unf", "NA"])
        ),
        "BsmtFullBath": Column(int, Check.ge(0)),
        "BsmtHalfBath": Column(int, Check.ge(0)),
        "BsmtQual": Column(
            str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po", "NA"]), nullable=True
        ),
        "BsmtUnfSF": Column(int, Check.ge(0)),
        "CentralAir": Column(str, Check.isin(["N", "Y"])),
        "Condition1": Column(
            str,
            Check.isin(
                [
                    "Artery",
                    "Feedr",
                    "Norm",
                    "RRNn",
                    "RRAn",
                    "PosN",
                    "PosA",
                    "RRNe",
                    "RRAe",
                ]
            ),
        ),
        "Condition2": Column(
            str,
            Check.isin(
                [
                    "Artery",
                    "Feedr",
                    "Norm",
                    "RRNn",
                    "RRAn",
                    "PosN",
                    "PosA",
                    "RRNe",
                    "RRAe",
                ]
            ),
        ),
        "Electrical": Column(
            str, Check.isin(["SBrkr", "FuseA", "FuseF", "FuseP", "Mix"])
        ),
        "EnclosedPorch": Column(int, Check.ge(0)),
        "ExterCond": Column(str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po"])),
        "ExterQual": Column(str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po"])),
        "Exterior1st": Column(
            str,
            Check.isin(
                [
                    "AsbShng",
                    "AsphShn",
                    "BrkComm",
                    "BrkFace",
                    "CBlock",
                    "CemntBd",
                    "HdBoard",
                    "ImStucc",
                    "MetalSd",
                    "Other",
                    "Plywood",
                    "PreCast",
                    "Stone",
                    "Stucco",
                    "VinylSd",
                    "Wd Sdng",
                    "WdShing",
                ]
            ),
        ),
        "Exterior2nd": Column(
            str,
            Check.isin(
                [
                    "AsbShng",
                    "AsphShn",
                    "BrkComm",
                    "BrkFace",
                    "CBlock",
                    "CemntBd",
                    "HdBoard",
                    "ImStucc",
                    "MetalSd",
                    "Other",
                    "Plywood",
                    "PreCast",
                    "Stone",
                    "Stucco",
                    "VinylSd",
                    "Wd Sdng",
                    "WdShing",
                ]
            ),
        ),
        "Fence": Column(str, Check.isin(["GdPrv", "MnPrv", "GdWo", "MnWw", "NA"])),
        "FireplaceQu": Column(
            str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po", "NA"]), nullable=True
        ),
        "Fireplaces": Column(int, Check.ge(0)),
        "Foundation": Column(
            str, Check.isin(["BrkTil", "CBlock", "PConc", "Slab", "Stone", "Wood"])
        ),
        "FullBath": Column(int, Check.ge(0)),
        "Functional": Column(
            str,
            Check.isin(["Typ", "Min1", "Min2", "Mod", "Maj1", "Maj2", "Sev", "Sal"]),
        ),
        "GarageArea": Column(int, Check.ge(0)),
        "GarageCars": Column(int, Check.ge(0)),
        "GarageCond": Column(str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po", "NA"])),
        "GarageFinish": Column(
            str, Check.isin(["Fin", "RFn", "Unf", "NA"]), nullable=True
        ),
        "GarageQual": Column(str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po", "NA"])),
        "GarageType": Column(
            str,
            Check.isin(
                ["2Types", "Attchd", "Basment", "BuiltIn", "CarPort", "Detchd", "NA"]
            ),
        ),
        "GarageYrBlt": Column(int, Check.ge(1800)),
        "GrLivArea": Column(int, Check.ge(0)),
        "HalfBath": Column(int, Check.ge(0)),
        "Heating": Column(
            str, Check.isin(["Floor", "GasA", "GasW", "Grav", "OthW", "Wall"])
        ),
        "HeatingQC": Column(str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po"])),
        "HouseStyle": Column(
            str,
            Check.isin(
                [
                    "1Story",
                    "1.5Fin",
                    "1.5Unf",
                    "2Story",
                    "2.5Fin",
                    "2.5Unf",
                    "SFoyer",
                    "2Lvl",
                ]
            ),
        ),
        "Id": Column(int, Check.ge(1)),
        "KitchenAbvGr": Column(int, Check.ge(0)),
        "KitchenQual": Column(str, Check.isin(["Ex", "Gd", "TA", "Fa", "Po"])),
        "LandContour": Column(str, Check.isin(["Lvl", "Bnk", "HLS", "Low"])),
        "LandSlope": Column(str, Check.isin(["Gtl", "Mod", "Sev"])),
        "LotArea": Column(int, [Check.ge(0), Check.le(10000)]),
        "LotConfig": Column(
            str, Check.isin(["Inside", "Corner", "CulDSac", "FR2", "FR3"])
        ),
        "LotFrontage": Column(
            float, [Check.ge(10), Check(nullable_int_column)], nullable=True
        ),
        "LotShape": Column(str, Check.isin(["Reg", "IR1", "IR2", "IR3"])),
        "LowQualFinSF": Column(int, Check.ge(0)),
        "MSSubClass": Column(
            str,
            Check.isin([str(s) for s in range(20, 200, 5)]),
        ),
        "MSZoning": Column(
            str, Check.isin(["A", "C (all)", "FV", "I", "RH", "RL", "RP", "RM"])
        ),
        "MasVnrArea": Column(int, [Check.ge(0), Check.le(10000)]),
        "MasVnrType": Column(
            str, Check.isin(["BrkCmn", "BrkFace", "CBlock", "None", "Stone"])
        ),
        "MiscFeature": Column(
            str, Check.isin(["Elev", "Gar2", "Othr", "Shed", "TenC", "NA"])
        ),
        "MiscVal": Column(int, Check.ge(0)),
        "MoSold": Column(int, Check.isin(range(1, 13))),
        "Neighborhood": Column(
            str,
            Check.isin(
                [
                    "Blmngtn",
                    "Blueste",
                    "BrDale",
                    "BrkSide",
                    "ClearCr",
                    "CollgCr",
                    "Crawfor",
                    "Edwards",
                    "Gilbert",
                    "IDOTRR",
                    "MeadowV",
                    "Mitchel",
                    "NAmes",
                    "NoRidge",
                    "NPkVill",
                    "NridgHt",
                    "NWAmes",
                    "OldTown",
                    "SWISU",
                    "Sawyer",
                    "SawyerW",
                    "Somerst",
                    "StoneBr",
                    "Timber",
                    "Veenker",
                ]
            ),
        ),
        "OpenPorchSF": Column(int, [Check.ge(0), Check.le(10000)]),
        "OverallCond": Column(int, [Check.ge(1), Check.le(10)]),
        "OverallQual": Column(int, [Check.ge(1), Check.le(10)]),
        "PavedDrive": Column(str, Check.isin(["Y", "P", "N"])),
        "PoolArea": Column(int, [Check.ge(0), Check.le(10000)]),
        "PoolQC": Column(str, Check.isin(["Ex", "Gd", "TA", "Fa", "NA"])),
        "RoofMatl": Column(
            str,
            Check.isin(
                [
                    "ClyTile",
                    "CompShg",
                    "Membran",
                    "Metal",
                    "Roll",
                    "Tar&Grv",
                    "WdShake",
                    "WdShngl",
                ]
            ),
        ),
        "RoofStyle": Column(
            str, Check.isin(["Flat", "Gable", "Gambrel", "Hip", "Mansard", "Shed"])
        ),
        "SaleCondition": Column(
            str,
            Check.isin(["Normal", "Abnorml", "AdjLand", "Alloca", "Family", "Partial"]),
        ),
        "SaleType": Column(
            str,
            Check.isin(
                [
                    "WD",
                    "CWD",
                    "VWD",
                    "New",
                    "COD",
                    "Con",
                    "ConLw",
                    "ConLI",
                    "ConLD",
                    "Oth",
                ]
            ),
        ),
        "ScreenPorch": Column(int, [Check.ge(0), Check.le(10000)]),
        "Street": Column(str, Check.isin(["Grvl", "Pave"])),
        "TotRmsAbvGrd": Column(int, [Check.ge(0), Check.le(20)]),
        "TotalBsmtSF": Column(int, [Check.ge(0), Check.le(10000)]),
        "Utilities": Column(str, Check.isin(["AllPub", "NoSewr", "NoSewa", "ELO"])),
        "WoodDeckSF": Column(int, [Check.ge(0), Check.le(10000)]),
        "YearBuilt": Column(int, [Check.ge(1800), Check.le(2030)]),
        "YearRemodAdd": Column(int, [Check.ge(1900), Check.le(2030)]),
        "YrSold": Column(int, Check.ge(0)),
        "FirstFlrSF": Column(int, Check.ge(0)),
        "SecondFlrSF": Column(int, Check.ge(0)),
        "ThreeSsnPortch": Column(int, Check.ge(0)),
    },
    strict=True,  # Data columns == schema columns
    coerce=True,
)
