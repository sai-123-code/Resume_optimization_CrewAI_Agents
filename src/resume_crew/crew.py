# import os
# from crewai import Agent, Crew, Process, Task, LLM
# from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool, ScrapeWebsiteTool
# from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
# from .models import (
#     JobRequirements,
#     ResumeOptimization,
#     CompanyResearch
# )
#
#
# @CrewBase
# class ResumeCrew():
#     """ResumeCrew for resume optimization and interview preparation"""
#
#     agents_config = 'config/agents.yaml'
#     tasks_config = 'config/tasks.yaml'
#
#     def __init__(self) -> None:
#         """Sample resume PDF for testing"""
#         # Use a valid OpenAI model name
#         self.llm = LLM(model="gpt-3.5-turbo", temperature=0.7)
#
#         # Initialize knowledge source if PDF exists
#         if os.path.exists("Sai_Varun_Resume_2025.pdf"):
#             self.resume_pdf = PDFKnowledgeSource(file_paths=["Sai_Varun_Resume_2025.pdf"])
#         else:
#             self.resume_pdf = None
#             print("Warning: Resume PDF not found. Agents will work without knowledge source.")
#
#     @agent
#     def resume_analyzer(self) -> Agent:
#         knowledge_sources = [self.resume_pdf] if self.resume_pdf else []
#         return Agent(
#             config=self.agents_config['resume_analyzer'],
#             verbose=True,
#             llm=self.llm,
#             knowledge_sources=knowledge_sources
#         )
# # @CrewBase
# # class ResumeCrew():
# #     """ResumeCrew for resume optimization and interview preparation"""
# #
# #     agents_config = 'config/agents.yaml'
# #     tasks_config = 'config/tasks.yaml'
# #
# #     def __init__(self) -> None:
# #         """Sample resume PDF for testing from https://www.hbs.edu/doctoral/Documents/job-market/CV_Mohan.pdf"""
# #         self.resume_pdf = PDFKnowledgeSource(file_paths="Sai_Varun_Resume_2025.pdf")
# #
# #     @agent
# #     def resume_analyzer(self) -> Agent:
# #         return Agent(
# #             config=self.agents_config['resume_analyzer'],
# #             verbose=True,
# #             llm=LLM(model="gpt-3.5-turbo"),
# #             knowledge_sources=[self.resume_pdf]
# #         )
#
#     @agent
#     def job_analyzer(self) -> Agent:
#         return Agent(
#             config=self.agents_config['job_analyzer'],
#             verbose=True,
#             tools=[ScrapeWebsiteTool()],
#             llm=LLM(model="gpt-3.5-turbo"),
#         )
#
#     @agent
#     def company_researcher(self) -> Agent:
#         return Agent(
#             config=self.agents_config['company_researcher'],
#             verbose=True,
#             tools=[SerperDevTool()],
#             llm=LLM(model="gpt-3.5-turbo"),
#             knowledge_sources=[self.resume_pdf]
#         )
#
#     @agent
#     def resume_writer(self) -> Agent:
#         return Agent(
#             config=self.agents_config['resume_writer'],
#             verbose=True,
#             llm=LLM(model="gpt-3.5-turbo"),
#         )
#
#     @agent
#     def report_generator(self) -> Agent:
#         return Agent(
#             config=self.agents_config['report_generator'],
#             verbose=True,
#             llm=LLM(model="gpt-3.5-turbo"),
#         )
#
#     @task
#     def analyze_job_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['analyze_job_task'],
#             output_file='output/job_analysis.json',
#             output_pydantic=JobRequirements
#         )
#
#     @task
#     def optimize_resume_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['optimize_resume_task'],
#             output_file='output/resume_optimization.json',
#             output_pydantic=ResumeOptimization
#         )
#
#     @task
#     def research_company_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['research_company_task'],
#             output_file='output/company_research.json',
#             output_pydantic=CompanyResearch
#         )
#
#     @task
#     def generate_resume_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_resume_task'],
#             output_file='output/optimized_resume.md'
#         )
#
#     @task
#     def generate_report_task(self) -> Task:
#         return Task(
#             config=self.tasks_config['generate_report_task'],
#             output_file='output/final_report.md'
#         )
#
#     @crew
#     def crew(self) -> Crew:
#         knowledge_sources = [self.resume_pdf] if self.resume_pdf else []
#         return Crew(
#             agents=self.agents,
#             tasks=self.tasks,
#             verbose=True,
#             process=Process.sequential,
#             knowledge_sources=knowledge_sources,
#             # Add embedder configuration for knowledge sources
#             embedder={
#                 "provider": "openai",
#                 "config": {
#                     "model": "text-embedding-3-small"
#                 }
#             } if knowledge_sources else None
#         )
#
#     #
#     # @crew
#     # def crew(self) -> Crew:
#     #     return Crew(
#     #         agents=self.agents,
#     #         tasks=self.tasks,
#     #         verbose=True,
#     #         process=Process.sequential,
#     #         knowledge_sources=[self.resume_pdf]
#     #     )

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from .models import (
    JobRequirements,
    ResumeOptimization,
    CompanyResearch
)
import os


@CrewBase
class ResumeCrew():
    """ResumeCrew for resume optimization and interview preparation"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        """Sample resume PDF for testing"""
        # Use a valid OpenAI model name
        self.llm = LLM(model="gpt-3.5-turbo", temperature=0.7)

        # Initialize knowledge source if PDF exists
        if os.path.exists("Sai_Varun_Resume_2025.pdf"):
            self.resume_pdf = PDFKnowledgeSource(file_paths=["Sai_Varun_Resume_2025.pdf"])
        else:
            self.resume_pdf = None
            print("Warning: Resume PDF not found. Agents will work without knowledge source.")

    @agent
    def resume_analyzer(self) -> Agent:
        # Only add knowledge_sources if resume_pdf exists
        agent_config = {
            'config': self.agents_config['resume_analyzer'],
            'verbose': True,
            'llm': self.llm
        }

        if self.resume_pdf is not None:
            agent_config['knowledge_sources'] = [self.resume_pdf]

        return Agent(**agent_config)

    @agent
    def job_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['job_analyzer'],
            verbose=True,
            tools=[ScrapeWebsiteTool()],
            llm=self.llm
        )

    @agent
    def company_researcher(self) -> Agent:
        # Only add knowledge_sources if resume_pdf exists
        agent_config = {
            'config': self.agents_config['company_researcher'],
            'verbose': True,
            'tools': [SerperDevTool()],
            'llm': self.llm
        }

        if self.resume_pdf is not None:
            agent_config['knowledge_sources'] = [self.resume_pdf]

        return Agent(**agent_config)

    @agent
    def resume_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['resume_writer'],
            verbose=True,
            llm=self.llm
        )

    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['report_generator'],
            verbose=True,
            llm=self.llm
        )

    @task
    def analyze_job_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_job_task'],
            output_file='output/job_analysis.json',
            output_pydantic=JobRequirements
        )

    @task
    def optimize_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_resume_task'],
            output_file='output/resume_optimization.json',
            output_pydantic=ResumeOptimization
        )

    @task
    def research_company_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_company_task'],
            output_file='output/company_research.json',
            output_pydantic=CompanyResearch
        )

    @task
    def generate_resume_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_resume_task'],
            output_file='output/optimized_resume.md'
        )

    @task
    def generate_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_report_task'],
            output_file='output/final_report.md'
        )

    @crew
    def crew(self) -> Crew:
        # Only add knowledge_sources and embedder if resume_pdf exists
        crew_config = {
            'agents': self.agents,
            'tasks': self.tasks,
            'verbose': True,
            'process': Process.sequential
        }

        if self.resume_pdf is not None:
            crew_config['knowledge_sources'] = [self.resume_pdf]
            crew_config['embedder'] = {
                "provider": "openai",
                "config": {
                    "model": "text-embedding-3-small"
                }
            }

        return Crew(**crew_config)
