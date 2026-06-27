# WEEK 2 ASSIGNMENT
## Model Evaluation, Classification & Machine Learning Implementation

**Group Name:** Outliners  
**Group Members:** Nukesh Kumar Sahu, Shreepriya Sahu, Baibhab Nath, Aditi Sahu, Manish Sahu  
**College Name:** Your College Name  
**Branch & Year:** B.Tech Computer Science — 2nd Year  
**Submission:** Sunday, 28-06-2026, 5:00 PM  
**GitHub Repository:** https://github.com/YourUsername/Week2-ML-Projects-Outliners

---

### Task 1: Navigating the Model Evaluation Challenge
When we first started building Machine Learning models, it was tempting to just look at "Accuracy" and call it a day. But as our team quickly learned, evaluating a model is a lot like checking the health of a patient—one metric doesn't tell the whole story! Here’s a breakdown of the five essential evaluation metrics we explored:

**1. Accuracy**
- **What it is:** The percentage of total predictions our model got exactly right. 
- **Why it matters:** It’s a great starting point for a quick reality check. If we’re building a spam filter, knowing that 95% of emails are correctly sorted gives us confidence.
- **Real-world use:** Great for e-commerce recommendations or general retail forecasting where classes are balanced.

**2. Precision**
- **What it is:** Out of everything the model labeled as "positive," how many were actually positive?
- **Why it matters:** We think of Precision as the "Quality over Quantity" metric. If our model flags a bank transaction as fraudulent, we want to be absolutely sure we aren't declining a legitimate customer's card.
- **Real-world use:** Fraud detection and legal document review, where false alarms are incredibly costly.

**3. Recall (Sensitivity)**
- **What it is:** Out of all the true positive cases that exist, how many did our model successfully find?
- **Why it matters:** This is the "Don't Miss Anything" metric. In a hospital, missing a cancer diagnosis is far worse than accidentally flagging a healthy patient for a second screening. 
- **Real-world use:** Disease detection and disaster early warning systems.

**4. F1 Score**
- **What it is:** The harmonic mean between Precision and Recall. It acts as a peacekeeper when the two metrics are at odds.
- **Why it matters:** In real-world data, one class often outnumbers the other. F1 score helps us find a sweet spot so our model doesn't lean too heavily toward being overly cautious or overly trigger-happy.
- **Real-world use:** Credit scoring and text classification.

**5. AUC-ROC Curve**
- **What it is:** A graph showing how well our model can distinguish between two classes across all possible thresholds.
- **Why it matters:** It lets us compare entirely different models fairly, without being locked into a specific cut-off point. 
- **Real-world use:** Facial recognition systems and epidemiology.

**Bonus Question: Would You Deploy This Model in a Hospital?**
*Metrics: Accuracy 99%, Precision 45%, Recall 38%*
**Our Verdict:** Absolutely not! At first glance, 99% accuracy looks amazing, but in a medical setting, it's dangerously misleading. Since rare diseases might only affect 1% of patients, a model could just guess "Healthy" every time and still hit 99%. With a Recall of only 38%, more than 60% of sick patients would be sent home undiagnosed. Our team agreed that medical ethics require prioritizing high Recall to ensure every patient gets the care they need.

---

### Task 2: Building Linear Regression from Scratch
For this task, we decided to get our hands dirty. Instead of relying on pre-built libraries like Scikit-Learn, we built a Linear Regression model using purely Python and NumPy. Our goal was to predict a student's exam score based on how many hours they studied.

We created a dataset of 10 students and manually applied the Ordinary Least Squares formula. First, we calculated the slope (6.27), which told us that every extra hour of studying translated to about 6.27 extra marks. Then we found the intercept (31.0), meaning a student who didn't study at all would likely score around 31. 

By applying our equation `y = 6.27x + 31.0`, we successfully predicted the scores. We also calculated the Mean Squared Error (MSE) to check our work—coming in at a low 2.64, proving our line fit the data beautifully! It was incredibly rewarding for the team to see the math come to life on the scatter plot.

![Linear Regression Output](screenshots/linear_regression_output.png)

---

### Task 3: The Classification Sprint (Diabetes Prediction)
Next, we tackled a classification problem using the famous Pima Indians Diabetes Dataset. We chose Logistic Regression because it's fast, interpretable, and perfect for binary classification (Diabetes vs. No Diabetes). 

One hurdle we immediately faced was class imbalance—about 73% of our dataset didn't have diabetes. To fix this, we used stratified splitting and feature scaling. Our final model achieved a solid **85% Accuracy**, but more importantly, it hit a **95.5% Recall**! This means our model is excellent at catching patients who actually have diabetes, which aligns perfectly with our ethical discussion from Task 1.

![Classification Output](screenshots/classification_output.png)

---

### Task 4: Our Model Selection Strategy
Choosing the right algorithm is half the battle. Here is a quick cheat sheet our team put together:
- **Linear Regression:** Great for predicting continuous numbers (like house prices). It's fast but struggles with complex, non-linear patterns.
- **Logistic Regression:** Our go-to for binary classification (like approving a loan). It gives probabilities, not just hard labels.
- **KNN (K-Nearest Neighbours):** Simple and intuitive (great for product recommendations), but it gets very slow with massive datasets.
- **SVM (Support Vector Machine):** A powerhouse for high-dimensional data (like cancer gene classification), but requires careful tuning.
- **Naive Bayes:** Extremely fast and handles text beautifully. We'd use this to build a spam filter for our inboxes.

---

### Task 5: Making Sense of Explainable AI (XAI)
As a team, we realized that building an accurate model isn't enough; we have to be able to explain it. Feature Importance helps us rank which variables had the biggest impact (e.g., Blood Sugar vs. Age). 

**Why does this matter?** Because in fields like banking and healthcare, "black-box" models are a liability. If a bank rejects a loan, the law requires them to explain why. If a doctor administers chemotherapy based on an AI's advice, they need to know the reasoning. 

We looked into **SHAP values**, a game-theory approach that breaks down exactly how much each feature pushed a prediction up or down. If a credit card transaction is flagged for fraud, SHAP can tell the analyst: *"This was flagged because the purchase was 900 miles away at 3:00 AM."* It perfectly bridges the gap between cold algorithms and human judgment.

---

### Task 6: GitHub Portfolio Submission
We successfully compiled our code and uploaded it to our team GitHub.
**Repository Name:** Week2-ML-Projects-Outliners
**Link:** https://github.com/YourUsername/Week2-ML-Projects-Outliners

---

### Task 7: Team Collaboration Reflection

**How We Divided the Work:**
- **Nukesh Kumar Sahu:** Led the research on evaluation metrics and wrote our stance on the hospital deployment scenario.
- **Shreepriya Sahu:** Handled the heavy math, successfully implementing Linear Regression from scratch and generating the visual plots.
- **Baibhab Nath:** Took charge of the Classification task, building the Logistic Regression model and analyzing the confusion matrix.
- **Aditi Sahu:** Created our model selection strategy table and broke down the complex concepts of SHAP and Explainable AI.
- **Manish Sahu:** Orchestrated the GitHub repository, formatted our final README, and compiled this very report.

**Challenges We Faced:**
Working as a team is always a learning curve! Finding time to meet across different schedules was tough, and some of us were stronger in theory while others preferred coding. We tackled this by pairing up on video calls so we could learn from each other. We also had a healthy debate over which dataset to use for classification before finally agreeing on the Diabetes dataset due to its clean, understandable features. Oh, and resolving our first GitHub merge conflicts was definitely a character-building experience!

**What We Learned:**
This project opened our eyes to the reality of data science. It’s not just writing code in a basement—it’s about documentation, version control, and clear communication. Dividing the tasks allowed us to play to our strengths, but reviewing each other's work ensured we all grew our skill sets. We walk away from this assignment understanding that a model is only as good as our ability to explain it, trust it, and maintain it as a team.
