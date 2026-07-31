import pandas as pd
from pathlib import Path

START_DATE=pd.Timestamp("2015-01-01")
END_DATE=pd.Timestamp.today().normalize()

dates=pd.date_range(
    start=START_DATE,
    end=END_DATE,
    freq="D"
)

calendar=pd.DataFrame(
    {"Date":dates}
)

# Generate calendar attributes

calendar["DateId"]=(
    calendar["Date"].dt.strftime("%Y%m%d").astype(int) #string format time
)
calendar["Day"]=calendar["Date"].dt.day
calendar["DayName"]=calendar["Date"].dt.day_name()
calendar["DayOfWeek"]=calendar["Date"].dt.weekday + 1
calendar["WeekOfYear"]=calendar["Date"].dt.isocalendar().week.astype(int)

calendar["Month"]=calendar["Date"].dt.month
calendar["MonthName"]=calendar["Date"].dt.month_name()
calendar["Quarter"]="Q"+calendar["Date"].dt.quarter.astype(str)

calendar["Year"]=calendar["Date"].dt.year
calendar["IsWeekend"]=calendar["DayName"].isin(["Saturday","Sunday"])
calendar["IsWeekend"] = calendar["IsWeekend"].map({
    True: "Yes",
    False: "No"
})
calendar["FinancialYear"] = calendar["Date"].apply(
    lambda x: f"FY{x.year}-{str(x.year + 1)[-2:]}"
    if x.month >= 4
    else f"FY{x.year - 1}-{str(x.year)[-2:]}"
)



calendar = calendar[
    [
        "DateId",
        "Date",
        "Day",
        "DayName",
        "DayOfWeek",
        "WeekOfYear",
        "Month",
        "MonthName",
        "Quarter",
        "Year",
        "IsWeekend",
        "FinancialYear"
    ]
]

project_root = Path(__file__).resolve().parents[2]

#__file__ == my own file
#resolve=Tell me the full address -C:\Users\vamsi\Documents\RetailSphere-Enterprise-Analytics-Platform\rawdata..
#parents=Go backwards

output_path = project_root / "output" / "dimension"
output_path.mkdir(parents=True, exist_ok=True)
#if the folder doens't exist then i can't save the file.
# so Create all missing parent folders too."
#parents=True=Create all missing parent folders too.
# exist_ok=True  == If the folder already exists, don't complain.
calendar.to_csv(
    output_path / "calendar.csv", # 02_Raw_Data/output/dimensions/calendar.csv
    index=False
)

print(f"Calendar generated successfully!")
print(f"Rows created: {len(calendar)}")