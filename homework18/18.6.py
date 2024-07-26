def generate_report(title, author, *, date='Unknown', summary=None):
    print(f"Report:\nTitle: {title}\nAuthor: {author}\nDate: {date}\nSummary: {summary}")



generate_report(
    title = "Market Analysis Report",
    author = "Jenny Mayer",
    date = "25-07-2024",
    summary = "This report covers the performance of the fiancial market over the past year."
)
