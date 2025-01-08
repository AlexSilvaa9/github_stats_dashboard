
# Github Statistics Dashboard

This project presents a dashboard that displays statistics from your GitHub account using data fetched through the GitHub API. The data includes metrics such as the number of commits, collaborators, stars, forks, and more.

## Technologies

- Python
- GitHub API
- Pandas
- Google Looker Studio for visualization
- HTML & CSS (for dashboard)

## Installation

### 1. Prerequisites

Before getting started, make sure you have Python installed on your machine.

- Python 3.x
- `requests`
- `pandas`

### 2. Install Dependencies

Run the following command to install the required dependencies:

```bash
pip install requests pandas
```

### 3. Set up GitHub Token

This project requires you to use a personal access token from GitHub to interact with the API. To obtain it, follow these steps:

- Go to [GitHub Tokens](https://github.com/settings/tokens) and generate a new token.
- Store the token in your system's environment variables or in a `.env` file.

### 4. Run the Python Script

Once the token is set up, run the Python script to fetch the data and save it into CSV files:

```bash
python main.py
```

This will generate the `repo_metrics.csv` and `language_metrics.csv` files.

### 5. Create a Google Data Studio Report

Now that you have the necessary CSV files, follow these steps to create a Looker Studio (formerly Google Data Studio) report:

1. **Open Looker Studio:**
   - Go to [Looker Studio](https://lookerstudio.google.com) and sign in with your Google account.

2. **Create a New Report:**
   - Click on **Create** in the top left and select **Report**.

3. **Connect the Data:**
   - In the "Add Data to Report" section, choose **File Upload** and upload the `repo_metrics.csv` and `language_metrics.csv` files you generated earlier.
   
4. **Combine the Data Sources:**
   - Once the data sources are added, you can join them by creating a relationship. You can do this by matching common fields such as the repository name (`Repo`) or any other relevant metric.
   
5. **Create Visualizations:**
   - After combining the data, start adding visualizations such as:
     - Tables for repository statistics like stars, forks, and commits.
     - Pie charts to show language distributions.
     - Time series graphs to display commit activity over time.
   
6. **Customize the Dashboard:**
   - Customize the design, layout, and styling of the dashboard. You can apply color schemes that fit your theme, using blue and cyan tones, for example, to match the look and feel of your project.

7. **Share the Report:**
   - Once you’re satisfied with your dashboard, click on **Share** in the top right corner to share the report with others or to generate a public link.

Now you have a fully functional GitHub Statistics Dashboard in Looker Studio that updates dynamically with the data you’ve fetched from the GitHub API.

## Contributing

If you'd like to contribute to this project, please fork it and submit a pull request. Make sure your code is well-documented and follows the project's style.

