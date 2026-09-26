import pandas as pd
import matplotlib.pyplot as plt

# Veriyi yükle
data = pd.read_csv("data/sample_work_data.csv")

# Tarih sütunlarını tarih formatına çevir
data["Start_Date"] = pd.to_datetime(data["Start_Date"])
data["Planned_End_Date"] = pd.to_datetime(data["Planned_End_Date"])
data["Actual_End_Date"] = pd.to_datetime(data["Actual_End_Date"])

# Departmanlara göre çalışma saatleri
department_hours = data.groupby("Department")["Working_Hours"].sum()

print("\nDepartment Working Hours:")
print(department_hours)

# Çalışanlara göre fazla mesai
employee_overtime = data.groupby("Employee")["Overtime_Hours"].sum()

print("\nEmployee Overtime:")
print(employee_overtime)

# Geciken işler
data["Delay_Days"] = (
    data["Actual_End_Date"] - data["Planned_End_Date"]
).dt.days

delayed_tasks = data[data["Delay_Days"] > 0]

print("\nDelayed Tasks:")
print(delayed_tasks[["Project_ID", "Task", "Delay_Days"]])

# Fazla mesai grafiği
plt.figure(figsize=(10, 6))
employee_overtime.sort_values(ascending=False).plot(kind="bar")

plt.title("Employee Overtime Analysis")
plt.xlabel("Employee")
plt.ylabel("Overtime Hours")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/charts/employee_overtime.png")
plt.show()

# Departman çalışma saati grafiği
plt.figure(figsize=(10, 6))
department_hours.sort_values(ascending=False).plot(kind="bar")

plt.title("Working Hours by Department")
plt.xlabel("Department")
plt.ylabel("Working Hours")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("outputs/charts/department_working_hours.png")
plt.show()

print("\nAnalysis completed successfully.")