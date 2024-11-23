# Portfolio Project - Sample Code
# This script dynamically generates a project card for your portfolio.

def generate_project_card(title, description, technologies, link):
    """
    Generate a formatted project card for the portfolio.

    Args:
        title (str): The name of the project.
        description (str): A brief description of the project.
        technologies (list): A list of technologies used in the project.
        link (str): A link to the live project or repository.

    Returns:
        str: A formatted project card as a string.
    """
    tech_list = ", ".join(technologies)
    card = f"""
    ---------------------------------
    Project Title: {title}
    Description: {description}
    Technologies: {tech_list}
    Link: {link}
    ---------------------------------
    """
    return card

# Example usage
if __name__ == "__main__":
    # Example project details
    project_title = "My Portfolio Website"
    project_description = "A responsive portfolio website showcasing my projects and skills."
    project_technologies = ["HTML", "CSS", "JavaScript", "Python"]
    project_link = "https://github.com/username/portfolio"

    # Generate and display the project card
    project_card = generate_project_card(project_title, project_description, project_technologies, project_link)
    print(project_card)
