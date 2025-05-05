from crewai import Crew, Task
from agents.symptom_collector import symptom_collector

def create_crew():
    collector = symptom_collector()

    task = Task(
        description=(
            "Converse com o paciente e colete todas as informações importantes sobre seus sintomas, "
            "incluindo localização da dor, duração, intensidade, e qualquer outro detalhe relevante."
        ),
        expected_output="Lista organizada de sintomas com suas características",
        agent=collector
    )

    return Crew(
        agents=[collector],
        tasks=[task],
        verbose=True
    )
