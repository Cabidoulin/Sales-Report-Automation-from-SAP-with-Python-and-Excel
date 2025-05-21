
import pandas as pd

# Cargar el archivo simulado exportado desde SAP
df = pd.read_excel("Reporte_Ventas_SAP_Simulado.xlsx")

# Mostrar resumen general
print("Resumen general:")
print(df.describe())

# Total de ventas por cliente
ventas_cliente = df.groupby("Cliente")["Total USD"].sum().sort_values(ascending=False)
print("\nVentas por cliente:")
print(ventas_cliente)

# Total de ventas por producto
ventas_producto = df.groupby("Producto")["Total USD"].sum().sort_values(ascending=False)
print("\nVentas por producto:")
print(ventas_producto)

# Ventas por mes
df["Mes"] = pd.to_datetime(df["Fecha Pedido"]).dt.to_period("M")
ventas_mes = df.groupby("Mes")["Total USD"].sum()
print("\nVentas por mes:")
print(ventas_mes)
