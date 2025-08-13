# Data Sources

This document records the sources of all learning materials used in **FinWise** and how they are stored in the project.

---

## 1. Zerodha Varsity

**Source:** [https://zerodha.com/varsity/](https://zerodha.com/varsity/)  
**Description:** Comprehensive modules covering stock markets, trading, investing, risk management, and personal finance.

**Downloaded Modules:**  
(Modules without official PDFs — 12, 15, 16, 17 — were skipped)

| Module No. | Title                                               | Filename                                                      |
|------------|-----------------------------------------------------|--------------------------------------------------------------|
| 01         | Introduction to Stock Markets                       | `varsity_module01_introduction_to_stock_markets.pdf`         |
| 02         | Technical Analysis                                   | `varsity_module02_technical_analysis.pdf`                    |
| 03         | Fundamental Analysis                                 | `varsity_module03_fundamental_analysis.pdf`                  |
| 04         | Futures Trading                                      | `varsity_module04_futures_trading.pdf`                       |
| 05         | Options Theory for Professionals                     | `varsity_module05_options_theory_for_professionals.pdf`      |
| 06         | Option Strategies                                    | `varsity_module06_option_strategies.pdf`                     |
| 07         | Market Sensibility                                   | `varsity_module07_market_sensibility.pdf`                    |
| 08         | Currency Trading                                     | `varsity_module08_currency_trading.pdf`                      |
| 09         | Commodity Trading                                    | `varsity_module09_commodity_trading.pdf`                     |
| 10         | Risk Management and Trading Psychology               | `varsity_module10_risk_management_and_trading_psychology.pdf`|
| 11         | Personal Finance – Mutual Funds                      | `varsity_module11_personal_finance_mutual_funds.pdf`         |
| 13         | Financial Modelling                                  | `varsity_module13_financial_modelling.pdf`                   |
| 14         | Personal Finance – Insurance                         | `varsity_module14_personal_finance_insurance.pdf`            |

**Folder:**  
```

data/raw/varsity/

```

---

## 2. SEBI Investor Education Materials

**Source:** [https://investor.sebi.gov.in/iematerial.html](https://investor.sebi.gov.in/iematerial.html)  
**Description:** Official investor education PDFs from the Securities and Exchange Board of India.

**Downloaded Files:**  

| Filename |
|----------|
| sebi_buy_sell_shares.pdf |
| sebi_buyback_open_offer.pdf |
| sebi_corporate_actions.pdf |
| sebi_depository_services.pdf |
| sebi_derivative_segment.pdf |
| sebi_etfs_intro.pdf |
| sebi_how_to_invest_ipo.pdf |
| sebi_how_to_invest_rights_issue.pdf |
| sebi_introduction_to_commodity_derivatives_market.pdf |
| sebi_invit_intro.pdf |
| sebi_kyc_procedure.pdf |
| sebi_mutual_funds_advance.pdf |
| sebi_mutual_funds_beginner.pdf |
| sebi_mutual_funds_intermediate.pdf |
| sebi_mutual_funds_intro.pdf |
| sebi_nri_investments.pdf |
| sebi_online_dispute_resolution.pdf |
| sebi_reits_intro.pdf |
| sebi_safeguard_frauds.pdf |
| sebi_sebi_complaints_redressal.pdf |
| sebi_securities_market_booklet.pdf |
| sebi_securities_market_level1.pdf |

**Folder:**  
```

data/raw/sebi\_education/

```

---

## Notes
- Large PDF files are **not committed** to the GitHub repository.  
- These files are listed in `.gitignore` to keep the repo lightweight.  
- Naming conventions are lowercase, words separated by underscores, and prefixed by source (`varsity_` or `sebi_`).  
```
