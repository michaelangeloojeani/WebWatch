# WebWatch – Web Vulnerability Scanner

**Final Year Project | B.Sc. (Hons) Software Development**

**Atlantic Technological University (ATU), Galway**

**Student:** Michaelangelo Ojeani
**Supervisor:** Darragh Matthews
**Academic Year:** 2026–2027

## Project Overview

WebWatch is an automated web vulnerability scanner developed as part of my final-year software development project.

The application aims to identify potential security vulnerabilities in web applications by crawling websites, discovering input fields and URL parameters, and performing controlled security assessments.

The project focuses on implementing its own crawling, input discovery, vulnerability assessment and reporting functionality rather than relying entirely on existing security scanning tools.

WebWatch will provide a dashboard that displays scan results, identified vulnerabilities, severity classifications and supporting evidence.

All security assessments will be conducted in controlled environments against deliberately vulnerable applications or systems where testing is explicitly authorized.

## Project Objectives

The main objectives of WebWatch are:

- Develop a web crawler that discovers accessible pages and links.
- Identify HTML forms, input fields and URL parameters.
- Implement controlled detection checks for SQL Injection (SQLi), reflected Cross-Site Scripting (XSS) and potential Cross-Site Request Forgery (CSRF) vulnerabilities.
- Classify identified vulnerabilities according to severity.
- Provide supporting evidence for detected vulnerabilities.
- Develop a web dashboard to display scan progress and results.
- Generate downloadable PDF reports containing findings and recommendations.

## Technologies Used

| Technology              | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| Python                  | Main programming language                |
| Flask                   | Backend web framework                    |
| Requests                | HTTP requests and page retrieval         |
| BeautifulSoup           | HTML parsing and input discovery         |
| HTML, CSS, JavaScript   | Frontend development                     |
| Bootstrap               | Responsive dashboard design              |
| SQLite                  | Database for scan history and findings   |
| ReportLab               | PDF report generation                    |
| Pytest                  | Automated testing                        |
| Git & GitHub            | Version control and issue tracking       |
| OWASP Juice Shop / DVWA | Controlled security testing environments |

## System Architecture

WebWatch will consist of five main components:

1. **Web Interface:** Allows users to initiate scans and view results.
2. **Crawling Engine:** Discovers pages, links and input fields.
3. **Vulnerability Assessment:** Performs controlled checks for potential security weaknesses.
4. **Database:** Stores scan history, discovered inputs and findings.
5. **Reporting Module:** Generates PDF reports containing vulnerability information.

## Installation and Setup

### Prerequisites

- Python 3
- Git
- Visual Studio Code or another suitable IDE

### 1. Clone the Repository

```bash
git clone https://github.com/michaelangeloojeani/WebWatch.git
cd WebWatch
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

Open the application in your browser:

`http://127.0.0.1:5000`

*Note: These instructions apply to the initial Flask application. Additional configuration may be required as development progresses.*

## Development Roadmap

- [ ] Create GitHub repository and configure Python environment
- [ ] Initialise Flask application
- [ ] Design application architecture and database
- [ ] Develop web crawler
- [ ] Implement form and input discovery
- [ ] Develop scan management functionality
- [ ] Implement vulnerability assessment modules
- [ ] Develop dashboard and results visualization
- [ ] Implement PDF reporting
- [ ] Perform automated testing and evaluation

## Testing and Evaluation

WebWatch will be evaluated using deliberately vulnerable applications, such as OWASP Juice Shop or DVWA, in a controlled local environment.

Testing will focus on functionality, detection accuracy, false positives, scan reliability and usability.

## Project Status

**In Development**

This project is being developed incrementally, with regular Git commits and GitHub Issues used to track progress.

## Disclaimer

WebWatch is intended for educational purposes and authorized security assessments only. It must not be used to scan websites or systems without explicit permission.

## Author

**Michaelangelo Ojeani**
B.Sc. (Hons) Software Development
Atlantic Technological University, Galway
