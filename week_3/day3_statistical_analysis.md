# Phase II - Track B: Data Analyst - Week 3 - Day 13: Statistical Analysis Basics

Course Day: Day 13 of 40  
Track: Track B (Data Analyst)  
Focus: Descriptive Statistics, Outlier Detection (IQR), Correlation, and Hypothesis Testing  
Project: Mombasa Microfinance Institution Loan Portfolio & Repayment Analysis  

---

## 1. Core Mathematical and Statistical Principles

Numbers without contextual statistical framing represent noise. In commercial data analytics, executives and board members do not merely require arithmetic averages; they require confirmation of whether operational metrics fall within expected normal bounds or represent abnormal risk exposures.

### Step 1: Descriptive Statistics (Central Tendency and Dispersion)

Descriptive statistics summarize the central location, variability, and shape of a sample distribution.

1. **Arithmetic Mean ($\mu$ or $\bar{x}$)**:
   $$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$
   The arithmetic balance point. It incorporates all values but is sensitive to extreme values (outliers).

2. **Median ($Q_2$ or 50th Percentile)**:
   The physical midpoint of an ordered dataset. It is resistant to skewness and extreme values, representing the typical observation.
   - When $\text{Mean} \approx \text{Median}$, the distribution is roughly symmetric.
   - When $\text{Mean} > \text{Median}$, the distribution is right-skewed (positively skewed), pulled upward by high-value observations.
   - When $\text{Mean} < \text{Median}$, the distribution is left-skewed (negatively skewed).

3. **Sample Standard Deviation ($s$)**:
   $$s = \sqrt{\frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$$
   Quantifies the absolute dispersion or spread around the arithmetic mean in original measurement units. Bessel's correction ($n - 1$) provides an unbiased estimator for sample variance.

4. **Quartiles and Interquartile Range (IQR)**:
   - $Q_1$ (25th percentile): Value below which 25% of observations fall.
   - $Q_3$ (75th percentile): Value below which 75% of observations fall.
   - $\text{IQR} = Q_3 - Q_1$: Captures the middle 50% spread of the data, providing a robust measure of dispersion unaffected by tail extremes.

```python
import pandas as pd

# Extract summary statistics in pandas
summary = df["amount_kes"].describe()
q1 = df["amount_kes"].quantile(0.25)
q3 = df["amount_kes"].quantile(0.75)
iqr = q3 - q1
```

---

### Step 2: Outlier Detection via the Tukey Interquartile Range (IQR) Method

An outlier is a data point located outside the general pattern of a distribution. Outliers stem from genuine high-value transactions, measurement errors, data entry defects, or fraudulent activities.

Under John Tukey's standard boxplot rule, thresholds are established at 1.5 times the Interquartile Range beyond the first and third quartiles:

$$\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}$$
$$\text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$$

Any observation $x_i < \text{Lower Bound}$ or $x_i > \text{Upper Bound}$ is classified as a statistical outlier.

```python
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df["amount_kes"] < lower_bound) | (df["amount_kes"] > upper_bound)]
```

---

### Step 3: Correlation Analysis (Pearson's $r$)

Correlation measures the linear relationship between two continuous variables $X$ and $Y$:

$$r_{xy} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^2}}$$

- Value ranges between $-1.0 \le r \le +1.0$.
- $r > 0$: Positive linear relationship (as $X$ increases, $Y$ tends to increase).
- $r < 0$: Negative linear relationship (as $X$ increases, $Y$ tends to decrease).
- $r = 0$: Absence of linear relationship.
- Rule of thumb for magnitude: $|r| \ge 0.7$ (strong), $0.4 \le |r| < 0.7$ (moderate), $|r| < 0.4$ (weak).

**Crucial Business Distinction**: Correlation measures co-movement, not direct causality. Confounding variables and operational structures must always be examined before claiming causal mechanisms.

```python
correlation = df["amount_kes"].corr(df["days_to_first_repayment"])
```

---

### Step 4: Hypothesis Testing (Independent Samples Two-Tailed t-Test)

When comparing whether differences between groups reflect true operational distinctions or random chance, analysts perform hypothesis testing.

- **Null Hypothesis ($H_0$)**: $\mu_1 = \mu_2$ (no genuine difference between group means).
- **Alternative Hypothesis ($H_a$)**: $\mu_1 \neq \mu_2$ (the groups have statistically significant different means).
- **Significance Threshold ($\alpha$)**: Standard convention is $\alpha = 0.05$.
- **p-value Interpretation**:
  - If $p < 0.05$: Reject $H_0$. The observed difference is statistically significant.
  - If $p \ge 0.05$: Fail to reject $H_0$. The observed variation is consistent with random sample fluctuations.

```python
from scipy import stats

t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

---

## 2. Practical Case Study: Mombasa Microfinance Institution

### The Business Context
A microfinance institution (MFI) operating across Mombasa, Kilifi, and Kwale counties required a quantitative loan portfolio analysis for its upcoming quarterly board meeting.

The board raised two primary operational concerns:
1. Is the reported portfolio average loan size inflated by high-value commercial outliers rather than micro-borrowers?
2. Does increasing loan size delay initial borrower repayment schedules, exposing the institution to heightened liquidity strain?

### Dataset Structure (`mombasa_mfi_loans.csv`)
- **Total Facilities ($N$)**: 150 active loans.
- **Attributes**: `loan_id`, `amount_kes`, `days_to_first_repayment`, `county`.
- **Geographic Footprint**: Mombasa (68 loans), Kilifi (43 loans), Kwale (39 loans).

---

## 3. Executive Report and Board Briefing

### Required Board One-Sentence Plain Finding
> "Borrowers taking larger loans take moderately longer to make their first repayment (correlation = 0.57, p < 0.001), indicating that larger working capital disbursements require a longer initial operational ramp-up period before cash returns begin."

---

## 4. Quantitative Portfolio Findings

| Metric | Computed Value | Analytical Interpretation |
|:---|:---|:---|
| **Portfolio Count** | 150 facilities | Comprehensive sample across Coast Region branches |
| **Typical Loan (Median)** | **KES 32,750.00** | True baseline typical micro-borrower facility size |
| **Arithmetic Mean** | **KES 40,176.67** | Inflated by +KES 7,426.67 due to high-value commercial facilities |
| **Standard Deviation** | KES 36,149.96 | High dispersion across diverse borrowing tiers |
| **Minimum Loan** | KES 10,000.00 | Standard micro-enterprise entry credit |
| **25th Percentile ($Q_1$)** | KES 24,625.00 | Lower quartile threshold |
| **75th Percentile ($Q_3$)** | KES 42,750.00 | Upper quartile threshold |
| **Interquartile Range (IQR)** | KES 18,125.00 | Middle 50% core customer borrowing band |
| **Outlier Threshold** | **> KES 69,937.50** | $Q_3 + 1.5 \times \text{IQR}$ upper boundary |
| **Outlier Accounts** | **8 loans (5.3%)** | Non-standard commercial credit exposures |
| **Pearson Correlation ($r$)** | **0.570** ($p = 2.59 \times 10^{-14}$) | Statistically significant positive relationship |

---

## 5. Identified Outlier Loan Accounts

The following 8 accounts exceed the KES 69,937.50 upper limit and represent commercial scale lending:

| Loan ID | County | Loan Amount (KES) | Days to 1st Repayment |
|:---|:---|:---:|:---:|
| **LN-1089** | Mombasa | KES 290,000.00 | 54 days |
| **LN-1043** | Mombasa | KES 240,000.00 | 53 days |
| **LN-1135** | Mombasa | KES 220,000.00 | 60 days |
| **LN-1016** | Kwale | KES 185,000.00 | 47 days |
| **LN-1114** | Kwale | KES 99,500.00 | 24 days |
| **LN-1126** | Mombasa | KES 88,000.00 | 34 days |
| **LN-1107** | Mombasa | KES 77,000.00 | 38 days |
| **LN-1032** | Mombasa | KES 75,500.00 | 22 days |

---

## 6. Visual Artifact

The publication-grade distribution visualization is saved at [`loan_amount_distribution.png`](file:///home/mwaniasamuel/AI-masterclass2/week_3/loan_amount_distribution.png):

- **Teal Bars**: Core distribution of standard micro-loans within regular bounds.
- **Red Bars**: Outlier loan facilities extending past KES 69,937.50.
- **Green Dashed Line**: Median loan amount (KES 32,750.00), demonstrating the true typical customer level.
- **Blue Dash-Dot Line**: Arithmetic mean (KES 40,176.67), highlighting rightward skew caused by commercial accounts.
- **Red Dotted Line**: The $1.5 \times \text{IQR}$ cutoff boundary (KES 69,937.50).

---

## 7. Actionable Recommendations for Board Governance

1. **Dual Credit Underwriting Policy**:
   - Establish separate credit guidelines for loans above KES 70,000. Facilities under KES 70,000 follow standard micro-credit scoring, while loans above KES 70,000 should require commercial cash flow projections and collateral appraisal.

2. **Tailored Grace Period Schedules**:
   - Because larger loans correlate with longer ramp-up durations ($r = 0.57$), require structured 30 to 45 day grace periods for commercial loans rather than penalizing borrowers under standard 14-day micro-loan rules.

3. **Risk Exposure Concentration**:
   - Outliers constitute only 5.3% of borrower accounts but represent 21.0% of total loan capital deployed. Risk management committees must monitor these 8 accounts individually.
