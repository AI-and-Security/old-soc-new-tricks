from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, WebsiteSearchTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class Ti:
    """Ti crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def osint_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["osint_researcher"],
            verbose=True,
            allow_delegation=False,
            tools=[SerperDevTool()],
        )

    @agent
    def web_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config["web_scraper"],
            verbose=True,
            allow_delegation=False,
            tools=[WebsiteSearchTool()],
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
            verbose=True,
        )

    @task
    def osint_task(self) -> Task:
        return Task(config=self.tasks_config["osint_task"])

    @task
    def scraper_task(self) -> Task:
        return Task(config=self.tasks_config["scraper_task"])

    @task
    def writer_task(self) -> Task:
        return Task(config=self.tasks_config["writer_task"])

    @crew
    def crew(self) -> Crew:
        """Creates the Ti crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
