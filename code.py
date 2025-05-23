import tkinter as tk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


analyzer = SentimentIntensityAnalyzer()


sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}
comments_list = []

def analyze_sentiment():
    comment = entry.get()
    if not comment.strip():
        return

    score = analyzer.polarity_scores(comment)
    compound = score["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
        color = "#00FF00"  
    elif compound <= -0.05:
        sentiment = "Negative"
        color = "#FF4C4C"  
    else:
        sentiment = "Neutral"
        color = "#CCCCCC"  

    comments_list.append((comment, sentiment))
    sentiments[sentiment] += 1

    label_result.config(text=f"Sentiment: {sentiment}", fg=color)
    entry.delete(0, tk.END)

def show_chart():
    labels = list(sentiments.keys())
    values = list(sentiments.values())

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values, color=['#00FF00', '#00FF00', '#00FF00'])  
    plt.title("Sentiment Summary", fontsize=14, fontweight='bold')
    plt.xlabel("Sentiment", fontsize=12)
    plt.ylabel("Number of Comments", fontsize=12)
    plt.tight_layout()
    plt.show()


window = tk.Tk()
window.title("🎯 Sentiment Analyzer")
window.geometry("450x320")
window.configure(bg="#000000")  


font_heading = ("Helvetica", 16, "bold")
font_label = ("Helvetica", 12)
font_button = ("Helvetica", 10, "bold")


label_title = tk.Label(window, text="Sentiment Analyzer", font=font_heading, fg="#00FF00", bg="#000000")
label_title.pack(pady=10)

label_prompt = tk.Label(window, text="Enter comment or review:", font=font_label, bg="#000000", fg="#FFFFFF")
label_prompt.pack(pady=5)

entry = tk.Entry(window, width=50, font=("Helvetica", 10), bg="#222222", fg="#FFFFFF", insertbackground="white")
entry.pack(pady=5)


analyze_button = tk.Button(
    window,
    text="Analyze",
    command=analyze_sentiment,
    bg="#FF0000",          
    fg="black",             
    activebackground="#FF85C1",
    activeforeground="black",
    font=font_button,
    width=20,
    relief="flat"
)
analyze_button.pack(pady=8)

label_result = tk.Label(window, text="", font=("Helvetica", 12, "bold"), bg="#000000")
label_result.pack(pady=10)

show_chart_button = tk.Button(
    window,
    text="Visualize Summary",
    command=show_chart,
    bg="#FF69B4",           
    fg="black",             
    activebackground="#FF85C1",
    activeforeground="black",
    font=font_button,
    width=20,
    relief="flat"
)
show_chart_button.pack(pady=10)

window.main
