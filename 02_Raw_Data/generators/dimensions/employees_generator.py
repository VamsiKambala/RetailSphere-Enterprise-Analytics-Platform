import pandas as pd
import random
from faker import Faker
from pathlib import Path
fake=Faker("en_IN")

NUMBER_OF_EMPLOYEES =2500

project_root=Path(__file__).resolve().parents[2]
stores_path=project_root/"output"/"dimensions"/"stores.csv"
stores=pd.read_csv(stores_path)

DEPARTMENTS={
    "Sales": 40,
    "Billing": 20,
    "Inventory": 15,
    "Customer Support": 10,
    "Security": 10,
    "HR": 5
}
DESIGNATIONS = {
    "Associate": 60,
    "Senior Associate": 20,
    "Supervisor": 12,
    "Assistant Manager": 5,
    "Manager": 3
}
SALARY_RANGE = {
    "Associate": (22000,32000),
    "Senior Associate": (32000,45000),
    "Supervisor": (45000,65000),
    "Assistant Manager": (65000,90000),
    "Manager": (90000,140000)
}

EMPLOYMENT_TYPE = {
    "Full-Time":85,
    "Part-Time":10,
    "Contract":5
}
SHIFTS = {
    "Morning":45,
    "Evening":40,
    "Night":15
}
ACTIVE_STATUS={
    "Yes":98,
    "No":2
}
employees=[]
for i in range(1,NUMBER_OF_EMPLOYEES+1):
    employee_id=f"EMP{i:06}"
    store_id=random.choice(stores["StoreID"])
    gender = random.choice(["Male", "Female"])
    if gender == "Male":
        employee_name = fake.name_male()
    else:
        employee_name = fake.name_female()
    department=random.choices(
        population=list(DEPARTMENTS.keys()),
        weights=list(DEPARTMENTS.values()),
        k=1
    )[0]
    designation = random.choices(
    population=list(DESIGNATIONS.keys()),
    weights=list(DESIGNATIONS.values()),
    k=1
    )[0]
    min_salary,max_salary=SALARY_RANGE[designation]
    salary=random.randint(min_salary,max_salary)
    joining_date = fake.date_between(
    start_date="-15y",
    end_date="today"
    )   
    employment_type = random.choices(
    population=list(EMPLOYMENT_TYPE.keys()),
    weights=list(EMPLOYMENT_TYPE.values()),
    k=1
    )[0]
    shift = random.choices(
    population=list(SHIFTS.keys()),
    weights=list(SHIFTS.values()),
    k=1
    )[0]
    email = f"{employee_id.lower()}@retailsphere.com"
    phone_number = f"9{random.randint(100000000,999999999)}"
    is_active = random.choices(
    population=list(ACTIVE_STATUS.keys()),
    weights=list(ACTIVE_STATUS.values()),
    k=1
    )[0]
    employee = {
    "EmployeeID": employee_id,
    "StoreID": store_id,
    "EmployeeName": employee_name,
    "Gender": gender,
    "Department": department,
    "Designation": designation,
    "Salary": salary,
    "JoiningDate": joining_date,
    "EmploymentType": employment_type,
    "Shift": shift,
    "Email": email,
    "PhoneNumber": phone_number,
    "IsActive": is_active
    }
    employees.append(employee)

employees_df=pd.DataFrame(employees)
output_path=project_root/"output"/"dimensions"
output_path.mkdir(parents=True,exist_ok=True)
employees_df.to_csv(output_path/"employees.csv",index=False)

print("Data Loaded Successfully")
print(employees_df.head())

print(f"Rows Created: {len(employees_df)}")

print(employees_df["EmployeeID"].duplicated().sum())

print(employees_df.isnull().sum())

print(employees_df["Department"].value_counts())

print(employees_df["Designation"].value_counts())

print(employees_df["EmploymentType"].value_counts())

print(employees_df["Shift"].value_counts())

print(employees_df["IsActive"].value_counts())