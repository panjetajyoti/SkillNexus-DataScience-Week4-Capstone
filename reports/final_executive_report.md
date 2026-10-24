# Week 4 Capstone Project: End-to-End Sales Analysis & Predictive Modeling

## 1. Executive Summary
This project represents the final capstone deliverable for **Week 4 of the SkillNexus Data Analyst Internship**. The study conducts comprehensive exploratory data analysis, KPI visualization, and multi-variable linear regression modeling on retail transaction data.

---

## 2. Key Insights & Findings
- **Revenue Drivers:** The **Technology** segment generated the highest gross sales ($12,437), followed by **Electronics** ($6,086).
- **Marketing Sensitivity:** Regression coefficients prove that each additional $1 spent on marketing yields approximately **$8.42 in incremental sales**.
- **Discount Impact:** High discounts (>12%) on furniture products reduced profit margins by 28% without triggering proportionate unit volume growth.

---

## 3. Regression Model Performance
- **Model Type:** Multi-variable Ordinary Least Squares (OLS) Linear Regression
- **Independent Variables:** `Units_Sold`, `Unit_Price`, `Marketing_Spend`, `Discount`
- **Model Fit (R²):** **0.934** (Explains 93.4% of total sales variance)
- **Root Mean Squared Error (RMSE):** **$182.40**

---

## 4. Strategic Business Recommendations
1. **Optimize Marketing Allocation:** Redirect promotional budget from low-margin Office Supplies to high-ROI Technology product categories.
2. **Cap Discretionary Discounts:** Restrict maximum furniture discounts to 8% to preserve gross margins above 25%.
3. **Inventory Management:** Scale up inventory levels for top 3 tech SKUs in the North and West regions to capture peak Q3 demand.