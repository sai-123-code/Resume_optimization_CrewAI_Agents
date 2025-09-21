#!/usr/bin/env python
import sys
import warnings

from resume_crew.crew import ResumeCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the resume optimization crew.
    """
    inputs = {
        'job_url': 'https://www.linkedin.com/jobs/view/4289766585',
        'company_name': 'Enculture'
    }
    ResumeCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
