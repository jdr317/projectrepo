# The Setup

Your CFO appears at your workspace, visibly frustrated and worried. The manual process of reporting spending for various GCP vendors like NetApp, Inc. is not just slow, but also error-prone. The finance team is bogged down with laborious data manipulation to aggregate spending across different vendors, and errors often slip through. For example, they often have to sift through extensive line-by-line expenditures to group all spending from GCP NetApp products, Inc. services under a single "GCP NetApp" category.

The CFO is not happy with the inefficiency, errors, and delays this causes in financial reporting. He is keen on leveraging technology to solve this issue and looks to you for a solution.

---

# The Request

The CFO has two main objectives:

1. Eliminate the manual work and errors associated with the current process.
2. Use the aggregated data to accurately allocate spending among vendors and, hopefully, derive additional financial insights.

### Generalize the methodology for similar projects

To achieve these goals, the CFO wants you to develop an automated reporting tool with the following features:

- **Run Automatically**: The tool should run automatically at the end of each week.
- **Data Collection**: Pull in raw spending data for different GCP vendors. The data for this project was pre-aggregated from parquet files stored in a datalake.
- **Data Aggregation**: Aggregate the spending for each Seller (e.g., group all GCP NetApp, Inc. spending under "GCP NetApp"). Group all related Seller names and normalize to a canonical name (either defined by you or publicly known). For example, there are multiple spellings of ‘Center for Internet Security’ in the data. The final spend should be aggregated by those canonical Seller names. Feel free to utilize Product column as well to guide you. 
- **Report Generation**: Generate a summarized report that breaks down the spending by vendor. You can include a section for additional insights.

---

# Additional Guidelines

- **Libraries**: Use any libraries that strike your fancy.
- **Time Limit**: Please limit the time you spend on the test to under 4 hours. If you spend more time than that, please let us know.
- **Simplifying Assumptions**: Feel free to make any simplifying assumptions to help you get to an MVP in under 4 hours.

---

# What We Want to See

- How you approach the problem is more important than the final product given the 4-hour time constraint.
- We expect to see python code and data outputs.
- Feel free to call out additional steps you would want to explore/take if you had more time.

---