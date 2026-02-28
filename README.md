<p align="center">
  <img src="./images/banner.png" width="90%"  alt="Project banner" /> 🚧 TODO - add an img
</p>

<h1 align="center">Mood Manager</h1>

<p align="center">
  An interactive predictive web application exploring how lifestyle factors influence mood and stress levels.
</p>

<p align="center">
  <a href="https://www.python.org/">
    <img alt="Python" height="29px" src="./images/python-logo.png" />
  </a>
  <a href="https://www.djangoproject.com/">
    <img alt="Django" height="29px" src="./images/django-logo.png">
  </a>
  <a href="https://getbootstrap.com/">
    <img alt="Bootstrap" height="29px" src="./images/bootstrap-logo.png">
  </a>
  🚧 TODO - add what other ones used for project
  🚧 TODO - add img for each one
</p>

## Overview

**Mood Manager** is a predictive web application that analyzes user-selected lifestyle variables and generates:

- **Predicted Mood score (0–10)**
- **Predicted Stress score (0–10)**

Users adjust on-screen slider controls to simulate behavioural scenarios. Each variable begins at a neutral midpoint and can be increased or decreased to reflect different habits or conditions.

After clicking **Predict**, the system evaluates the selected values and returns quantified results. The application functions as a behavioural simulator, allowing users to explore how changes in lifestyle factors may influence emotional wellbeing.

## Dataset

The predictive model was trained using a dataset sourced from [Kaggle](https://www.kaggle.com).

- **Number of records:** 2,000
- **Variables include:** sleep hours, screen time, exercise minutes, pending tasks, interruptions, fatigue level, social hours, coffee consumption, diet quality, and weather conditions.

This dataset provided the basis for weighting the input variables in the scoring logic to generate Mood and Stress predictions.

## Problem

Lifestyle habits such as sleep, workload, fatigue, and social interaction significantly influence emotional wellbeing. However, these relationships are often difficult to interpret without structured feedback.

A simple and interactive system is needed to help visualize how behavioural factors may correlate with mood and stress levels.

## Solution

The application provides a structured interface where users can experiment with lifestyle variables and immediately observe predicted outcomes.

Rather than tracking or storing personal data, the system is designed for exploration — enabling users to simulate different scenarios and reflect on potential behavioural impacts.

## Input Variables

The predictive model evaluates the following factors:

- Sleep hours
- Screen time
- Exercise minutes
- Daily pending tasks
- Interruptions
- Fatigue level
- Social hours
- Coffee cups
- Diet quality
- Weather

These variables are weighted within a structured scoring framework to calculate mood and stress predictions.

## Scoring Logic 🚧 TODO - at the moment some logic not working, lack of sleep didn't affect mood, Rosalie noted and I tested,

> Note: The scoring system is based on the Kaggle dataset’s variable distributions. Some extreme combinations (e.g., zero sleep) may not produce intuitively expected results due to dataset limitations.

The scoring system is rule-based and designed to model plausible behavioural relationships.

Each input variable contributes positively or negatively to Mood and Stress scores based on predefined weightings. Balanced inputs (midpoint values) represent a neutral state, while higher or lower extremes influence predictions proportionally.

Mood and Stress are calculated independently, allowing certain factors to impact stress more heavily than mood.

The final outputs are normalized to a 0–10 scale to provide clear, interpretable results.

The logic is modular, allowing future integration of machine learning models or adaptive weighting mechanisms.

## Features - 🚧 TODO - add features of rest of the site

- Interactive slider-based input system
- Real-time mood and stress prediction
- Immediate results display
- Colour-coded feedback system
- Clean, responsive user interface
- Modular architecture for future expansion

## How It Works

1. User adjusts slider controls representing lifestyle variables
2. Inputs are validated and processed server-side
3. Weighted scoring logic calculates Mood and Stress values
4. Results are displayed instantly with visual feedback

## UI Design and Responsiveness - 🚧 TODO - adjust for colours actually used, is it mobile first approach?

The interface follows a mobile-first design approach using the Bootstrap grid system.

A structured colour system supports clarity and interpretation:

- **Blue** serves as the primary interface colour, providing a calm and neutral interaction environment.
- **Green** highlights positive outcomes (higher mood, lower stress).
- **Red** indicates elevated stress levels, drawing attention to higher-risk states.

This colour hierarchy reinforces meaning without overwhelming the user.

The layout adapts seamlessly across mobile, tablet, and desktop devices. 🚧 TODO - test

Colour-coded results:

- **Green:** High mood / low stress
- **Red:** Low mood / high stress
- **Yellow/Orange:** Intermediate states

## Responsiveness - 🚧 TODO - check, is it mobile first approach, is it bootstrap grid? test again

The application is designed mobile-first using the Bootstrap grid system.  
Layouts adapt seamlessly across:

- **Desktop** – full-width charts and controls
- **Tablet** – stacked elements with preserved spacing
- **Mobile** – single-column layout for easy touch interaction

The input sliders, buttons, and results panels resize dynamically.  
No functionality is lost on smaller screens, ensuring the simulation is usable across devices.

## Technical Architecture - 🚧 TODO - check if correct items listed

### Backend

- Django
- Python

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Database

- SQLite (development)
- PostgreSQL (production-ready)

## Project Structure 🚧 TODO - check if correct items listed

```text
mood/
├── manage.py
├── mood_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dashboard/
│   ├── templates/
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
├── requirements.txt
└── README.md
```

## Installation 🚧 TODO - check if correct items listed

Clone the repository:

```bash
git clone https://github.com/yourusername/mood-manager.git
cd mood-manager
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate    # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations and start the development server:

```bash
python manage.py migrate
python manage.py runserver
```

## Deployment 🚧 TODO - check if correct items listed

Deployed via Render / Heroku / other hosting platform.

Environment variables required:

- SECRET_KEY
- DEBUG
- DATABASE_URL (if using PostgreSQL)

## Ethical Considerations - 🚧 TODO - check if correct items listed

This application provides predictive indicators and does not offer medical or psychological diagnoses.

User inputs are not stored, and the tool is designed for exploratory purposes only.

Future production implementations should include secure authentication, encrypted data handling, and a clear privacy policy.

## Future Improvements - 🚧 TODO - check if correct items listed, other ideas

- Machine learning-based predictive model
- Historical tracking and visual dashboards
- Personalised behavioural recommendations
- User authentication and profile management
- API endpoint for external integrations

## Testing - 🚧 TODO - more testing, edit results

> Testing performed manually by all team members across multiple devices and browsers.

Testing focused on ensuring that user inputs are processed correctly, outputs are meaningful and all parts of the website function, and are relevant to the site.

- **Input validation:** Ensured slider values remain within expected ranges and handle edge cases (e.g., 0 or maximum values).
- **Output checks:** Verified Mood and Stress predictions respond consistently to varying inputs. 🚧 TODO - mood ok when 0 sleep, check more
- **Functional testing:** Confirmed that Predict button triggers calculation and results update correctly.
- **Cross-browser / device checks:** Ensured layout and responsiveness work on desktop, tablet, and mobile screens.
- **Future testing plans:** Unit and integration tests can be added to automate validation as the project evolves.

## Contributors - 🚧 TODO - add names, edit list

- Names – Backend & Architecture
- Names – Frontend & UI
- Names – Testing & Documentation

## Acknowledgements - 🚧 TODO - edit

- **Dataset source:** [Kaggle – Lifestyle Factors Dataset](https://www.kaggle.com) (2,000 records used to train the model)
- **AI assistance:** ChatGPT, for helping with README drafting, structure, and content refinement
- **Technical references:**
  - [Django Documentation](https://docs.djangoproject.com/)
  - [Bootstrap Documentation](https://getbootstrap.com/docs/)
  - [Python Official Documentation](https://www.python.org/)

This section recognises resources, inspiration, and tools that contributed to the development of this project.

- Django Documentation
- Bootstrap Documentation
- Python Official Documentation
- Hackathon Organisers

## License

Specify license here (e.g., MIT License).
