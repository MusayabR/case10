# Medical Malpractice Analytics Dashboard

Medical malpractice claims at present times extend from many specialties and insurance types. Medical malpractice has become a problem which has caused many unfortunate people to get affected. Risk analysts and policy teams often need a quick way to explore payouts, identifying which specialties and claim types drive higher financial risk. This project implements a reproducible, containerized analytics dashboard that takes a malpractice claims dataset, computes summary metrics, and visualizes payout trends through an interactive streamlit web application.

The solution demonstrates a complete mini pipeline: data ingestion, cleaning, aggregation, risk scoring, and visualization. The entire system builds deterministically via Docker and runs with a single command on any clean machine.

## Course Concept Used

Data Engineering pipeline + interactive Web Analytics

This project demonstrates transforming raw structured data into high-level analytics and exposing insights through a web application.

The pipeline concepts applied would be:

- Extract and Load: CSV into pandas data frame.
- Transform: aggregations, filtering and risk computations.
- Serve: streamlit as the interactive frontend.
- Deploy: Docker containerization for reproducible executions.

## Architecture Diagram

<img width="970" height="1446" alt="image" src="https://github.com/user-attachments/assets/f136fe44-bc7f-4f50-9bcb-ac7947e8e6d5" />

## Data sources

Dataset: medicalmalpractice.csv

Columns include:

- Amount: dollar payout of the malpractice claim
- Severity: ordinal severity of the claim
- Age: claimant age
- Private Attorney: 0 or 1 indicator
- Marital Status
- Specialty: for example OBGYN, Cardiology, Pediatrics
- Insurance: Private, Medicare or Medicaid, No Insurance
- Gender

## My app is able to compute the:

- Total claims per filter
- Mean payout
- Mean severity
- Risk category
- Payout vs severity trend chart

## How to run local

Install docker desktop.

Run the command:

docker build -t malpractice-dashboard:latest .
docker run --rm -p 8501:8501 malpractice-dashboard:latest


Once running open the http link.

## Design decision

Streamlit for UI because it is simple, lightweight and good for analytics dashboards without frontend overhead.

Pandas for data Pipeline is efficient for filtering, grouping, aggregating, and calculating custom metrics.

## Tradeoffs

Performance-wise I choose in-memory Pandas which is perfect for small datasets.

Cost was perfect because it took only local computing power. No large-scale hosting required.

The complexity was simple as it was just a python pipeline.

Dataset contains no Personal identifiable information, only categorical features such as (age, severity, specialty, and insurance).

No secrets committed to the repo.

.env.example provided for future secure configuration if needed.

## Operations

Docker provides important builds and isolated execution.

Logs appear automatically through Streamlit and container logs.

Limitations can contain having no background jobs or async tasks to overload the computer.

## Results and Evaluation

Add heatmaps comparing specialties vs insurance types.

Introduce time-series analysis (for example by filing year).

## links

my github repo: https://github.com/MusayabR/case10

## credits and license

i used Chatgpt and cursor to assist in this project. It helped analyze how to approach this data base and what charts would work. It helped with coding the front end and showing and teaching how to use streamlit.
