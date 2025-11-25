import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("environmental indices tables.xlsx")
points=df["point"]
df.columns = df.columns.str.strip()
fig, axs = plt.subplots(3,1,figsize=(10,10))

for ax in axs:
    ax.set_xticks(points)
    ax.set_xticklabels([str(p) for p in points])


#NDVI Plot

axs[0].plot(points,df["NDVI_2015"],color="green",marker="o",label="NDVI_2015")
axs[0].plot(points,df["NDVI_2025"],color="green",marker="^",label="NDVI_2025")
axs[0].set_title("NDVI Comparison (2015 and 2025)")
axs[0].set_ylabel("NDVI Value")
axs[0].set_xlabel("sampling points")
axs[0].set_xticks(points)
axs[0].grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
axs[0].legend()

# NDMI Plot
axs[1].plot(points,df["NDMI_2015"],color="blue",marker="o",label="NDMI_2015")
axs[1].plot(points,df["NDMI_2025"],color="blue",marker="^",label="NDMI_2025")
axs[1].set_title("NDMI Comparison (2015 and2025)")
axs[1].set_ylabel("NDMI Value")
axs[1].set_xlabel("sampling points")
axs[1].set_xticks(points)
axs[1].grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
axs[1].legend()

# NDWI Plot
axs[2].plot(points,df["NDWI_2015"],color="red",marker="o",label="NDWI_2015")
axs[2].plot(points,df["NDWI_2025"],color="red",marker="^",label="NDWI_2025")
axs[2].set_title("NDWI Comparison (2015 and 2025)")
axs[2].set_ylabel("NDWI Value")
axs[2].set_xlabel("sampling points")
axs[2].set_xticks(points)
axs[2].grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)
axs[2].legend()




plt.tight_layout()
plt.show()