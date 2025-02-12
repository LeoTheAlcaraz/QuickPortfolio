import os
from jinja2 import Environment, FileSystemLoader

def get_user_input():
    """Collect user input for the portfolio."""
    print("Welcome to the Portfolio Builder!")
    name = input("Enter your name: ").strip()
    bio = input("Enter a short bio: ").strip()
    
    # Collect social media links
    social_links = {}
    print("\nEnter your social media links (type 'done' to finish):")
    while True:
        platform = input("Platform (e.g., GitHub, LinkedIn, Facebook, Instagram, Website): ").strip().lower()
        if platform == 'done':
            break
        link = input(f"Enter your {platform} link: ").strip()
        if platform and link:  # Ensure non-empty input
            social_links[platform] = link
    
    # Collect file upload (resume/CV)
    print("\nUpload your resume/CV (PDF, JPG, etc., max 25MB):")
    resume_path = input("Enter the file path: ").strip()
    if resume_path and os.path.exists(resume_path):
        file_size = os.path.getsize(resume_path) / (1024 * 1024)  # Size in MB
        if file_size > 25:
            print("File size exceeds 25MB. Please upload a smaller file.")
            resume_path = None
    else:
        resume_path = None
    
    # Collect education
    education = []
    print("\nEnter your education (type 'done' to finish):")
    while True:
        institution = input("Institution: ").strip()
        if institution.lower() == 'done':
            break
        degree = input("Degree: ").strip()
        field_of_study = input("Field of Study: ").strip()
        if institution and degree and field_of_study:  # Ensure non-empty input
            education.append({
                'institution': institution,
                'degree': degree,
                'field_of_study': field_of_study
            })
    
    # Collect certifications
    certifications = []
    print("\nEnter your certifications (type 'done' to finish):")
    while True:
        certification_name = input("Certification Name: ").strip()
        if certification_name.lower() == 'done':
            break
        issuing_organization = input("Issuing Organization: ").strip()
        if certification_name and issuing_organization:  # Ensure non-empty input
            certifications.append({
                'name': certification_name,
                'organization': issuing_organization
            })
    
    # Collect skills
    skills = []
    print("\nEnter your skills (type 'done' to finish):")
    while True:
        skill = input("Skill: ").strip()
        if skill.lower() == 'done':
            break
        if skill:  # Ensure non-empty input
            skills.append(skill)
    
    # Collect experience
    experience = []
    print("\nEnter your experience (type 'done' to finish):")
    while True:
        job_title = input("Job Title: ").strip()
        if job_title.lower() == 'done':
            break
        company = input("Company: ").strip()
        duration = input("Duration (e.g., Jan 2020 - Present): ").strip()
        description = input("Description: ").strip()
        if job_title and company and duration:  # Ensure non-empty input
            experience.append({
                'title': job_title,
                'company': company,
                'duration': duration,
                'description': description
            })
    
    # Collect projects
    projects = []
    print("\nEnter your projects (type 'done' to finish):")
    while True:
        project_name = input("Project name: ").strip()
        if project_name.lower() == 'done':
            break
        project_description = input("Project description: ").strip()
        project_link = input("Project link: ").strip()
        if project_name and project_description and project_link:  # Ensure non-empty input
            projects.append({
                'name': project_name,
                'description': project_description,
                'link': project_link
            })
    
    return {
        'name': name,
        'bio': bio,
        'social_links': social_links,
        'resume_path': resume_path,
        'education': education,
        'certifications': certifications,
        'skills': skills,
        'experience': experience,
        'projects': projects
    }

def generate_portfolio(data):
    """Generate the portfolio HTML file."""
    templates_dir = os.path.join(os.getcwd(), 'templates')
    if not os.path.exists(templates_dir):
        os.makedirs(templates_dir)  # Create the templates directory if it doesn't exist
    
    # Set up the Jinja2 environment
    env = Environment(loader=FileSystemLoader(templates_dir))
    
    # Load the template
    try:
        template = env.get_template('portfolio_template.html')
    except Exception as e:
        raise FileNotFoundError("Template file 'portfolio_template.html' not found.") from e
    
    # Render the portfolio HTML
    output = template.render(data)
    
    # Write the rendered output to a file (overwrite if exists)
    output_file = os.path.join(os.getcwd(), 'portfolio.html')
    with open(output_file, 'w') as f:
        f.write(output)
    
    print(f"\nPortfolio generated successfully! Open '{output_file}' to view it.")

if __name__ == "__main__":
    try:
        # Collect user input
        user_data = get_user_input()
        
        # Generate the portfolio
        generate_portfolio(user_data)
    except Exception as e:
        print(f"An error occurred: {e}")