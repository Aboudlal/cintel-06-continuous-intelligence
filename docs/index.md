# Continuous Intelligence

This site provides documentation for this project.
Use the navigation to explore module-specific materials.

## How-To Guide

Many instructions are common to all our projects.

See
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to get these projects running on your machine.

## Project Documentation Pages (docs/)

- **Home** - this documentation landing page
- **Project Instructions** - instructions specific to this module
- **Glossary** - project terms and concepts

## Additional Resources

- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
## Custom Project

### Dataset
The dataset contains system metrics such as requests, errors, and total latency in milliseconds. Each row represents one observation of system activity.

### Signals
I used the original signals error_rate and avg_latency_ms. I also created a new signal called performance_score, which measures the percentage of successful requests.

### Experiments
I modified the original pipeline by creating a custom file and adding a new signal called performance_score. I also used this new signal in anomaly detection and in the final system assessment.

### Results
The modified project produced a system assessment that included average requests, average errors, average error rate, average latency, and average performance score. The new signal helped provide a clearer picture of how efficiently the system was performing.

### Interpretation
This project shows that system health is not only about errors and latency. Performance score adds another useful view by showing how many requests were handled successfully. This gives better business intelligence for monitoring and decision-making.
