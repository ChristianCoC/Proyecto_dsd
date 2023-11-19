# %%
# Realizamos las importaciones necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Creamos el dataframe a partir del archivo .xlsx
ruta_archivo = "formularios\ganancias-gastos.xlsx"
df_ganancias_gastos = pd.read_excel(ruta_archivo)
print(df_ganancias_gastos)

# %%
# Creamos 4 gráficos con los datos del dataframe
# Gráfico 1: Ganancias por mes

personas = df_ganancias_gastos["Nombre"]
ganancias = df_ganancias_gastos["Ganancias por Mes"]

plt.figure(figsize=(16, 8))

plt.xlabel("Ganancias por mes")
plt.ylabel("Personas")

plt.title("Ganancias por Mes de 20 personas al azar")

plt.scatter(ganancias, personas, color="red", s=50)

plt.xticks(df_ganancias_gastos["Ganancias por Mes"])

plt.grid()

plt.savefig("graficos\grafico_1.png")
plt.show()

# %%
# Gráfico 2: Gastos por mes

gastos = df_ganancias_gastos["Gastos por Mes"]

plt.figure(figsize=(16, 8))

plt.xlabel("Gastos por mes")
plt.ylabel("Personas")

plt.title("Gastos por Mes de 20 personas al azar")

plt.scatter(gastos, personas, color="blue", s=50)

plt.xticks(df_ganancias_gastos["Gastos por Mes"])

plt.grid()

plt.savefig("graficos\grafico_2.png")
plt.show()

# %%
# Gráfico 3: Ganancias por gasto

plt.figure(figsize=(12, 6))

plt.ylabel("Gastos y Ganancias")

plt.title("Ganancias y Gastos por Mes")

plt.plot(ganancias, color="green")
plt.plot(gastos, color="red")

plt.xticks(range(len(personas)))

plt.grid()

plt.legend(["Ganancias", "Gastos"])

plt.savefig("graficos\grafico_3.png")
plt.show()

# %%
# Gráfico 4: Promedio de Gastos y Ganancias

promedio_ganancias = df_ganancias_gastos["Ganancias por Mes"].mean()
promedio_gastos = df_ganancias_gastos["Gastos por Mes"].mean()

plt.figure(figsize=(8, 6))

plt.ylabel("Promedio de Ganancias y Gastos")

plt.title("Promedio de Ganancias y Gastos por Mes")

plt.bar(
    ["Ganancias", "Gastos"],
    [promedio_ganancias, promedio_gastos],
    color=["green", "red"],
    width=0.4,
)

plt.grid()

plt.savefig("graficos\grafico_4.png")
plt.show()