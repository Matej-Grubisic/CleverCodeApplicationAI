import json
import flet as ft
from Agent import run_agent

def main(page: ft.Page):
    page.title = "Code Generator and Translator"
    page.theme_mode = "light"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    page.padding = 20

    # Dropdown for language selection
    languages = ["Python", "JavaScript", "Java", "C++", "TypeScript", "Go"]
    language_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(lang) for lang in languages],
        label="Select Language",
        width=200,
    )

    # Text field for code description
    code_description = ft.TextField(
        label="Describe the code you want to generate",
        multiline=True,
        min_lines=2,
        max_lines=5,
        width=400,
    )

    # Text field for code snippet input
    code_input = ft.TextField(
        label="Enter your code snippet",
        multiline=True,
        min_lines=4,
        max_lines=10,
        width=400,
    )

    # Text field for target language
    target_language_dropdown = ft.Dropdown(
        options=[ft.dropdown.Option(lang) for lang in languages],
        label="Select Target Language",
        width=200,
    )

    # Output fields
    output_description = ft.Text("", width=400, selectable=True)
    output_explanation = ft.Text("", width=400, selectable=True)
    output_translation = ft.Text("", width=400, selectable=True)
    output_quality_analysis = ft.Text("", width=400, selectable=True)

    # Settings
    settings_indentation = ft.TextField(label="Indentation (e.g., 4 spaces)", width=200)
    settings_naming_convention = ft.TextField(label="Naming Convention (e.g., camelCase)", width=200)

    # Function to generate code
    def generate_code(e):
        description = code_description.value
        language = language_dropdown.value
        inputs = json.dumps({"request": description, "language": language})

        generated_code = run_agent("generate_code", inputs)
        code_text = generated_code["code"]
        formatted_text = code_text.replace("<think>", "").replace("</think>", "").strip()
        formatted_text = "\n".join([line.strip() for line in formatted_text.split("\n") if line.strip()])
        output_description.value = formatted_text
        page.update()

    # Function to explain code
    def explain_code(e):
        code = code_input.value
        inputs = json.dumps({"code": code})

        explanation = run_agent("explain_code", inputs)
        text = explanation["explanation"]
        formatted_text = text.replace("<think>", "").replace("</think>", "").strip()
        formatted_text = "\n".join([line.strip() for line in formatted_text.split("\n") if line.strip()])
        output_explanation.value = formatted_text
        page.update()

    def check_language(e):
        code = code_input.value
        inputs = json.dumps({"code": code})

        language = run_agent("language_check", inputs)
        text = language["language"]
        formatted_text = text.replace("<think>", "").replace("</think>", "").strip()
        formatted_text = "\n".join([line.strip() for line in formatted_text.split("\n") if line.strip()])
        output_translation.value = formatted_text
        page.update()

    # Function to analyze code quality
    def analyze_code_quality(e):
        code = code_input.value
        inputs = json.dumps({"code": code})

        analysis_result = run_agent("code_quality", inputs)
        text = analysis_result["code_quality_analysis"]
        formatted_text = text.replace("<think>", "").replace("</think>", "").strip()
        formatted_text = "\n".join([line.strip() for line in formatted_text.split("\n") if line.strip()])
        output_quality_analysis.value = formatted_text
        page.update()

    # Function to save settings
    def save_settings(e):
        # Save settings (placeholder)
        indentation = settings_indentation.value
        naming_convention = settings_naming_convention.value
        print(f"Settings saved: Indentation={indentation}, Naming Convention={naming_convention}")
        page.update()

    # Function to handle navigation bar changes
    def on_nav_change(e):
        selected_index = e.control.selected_index
        update_page_content(selected_index)
        page.update()

    # Navigation Bar
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.CODE, label="Generate Code"),
            ft.NavigationBarDestination(icon=ft.icons.HELP_OUTLINE, label="Explain Code"),
            ft.NavigationBarDestination(icon=ft.icons.TRANSLATE, label="Check Code Language"),
            ft.NavigationBarDestination(icon=ft.icons.ASSESSMENT, label="Code Quality"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Settings"),
        ],
        selected_index=0,  # Default to the first page
        on_change=on_nav_change,
    )

    # Page content container
    page_content = ft.Container(
        width=page.width,
        padding=20,
    )

    # Function to update page content based on selected index
    def update_page_content(selected_index):
        if selected_index == 0:  # Generate Code
            page_content.content = ft.Column(
                [
                    ft.Text("Code Generator", size=24, weight="bold"),
                    code_description,
                    language_dropdown,
                    ft.ElevatedButton("Generate Code", on_click=generate_code),
                    output_description,
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,  # Allow the column to expand and take available space
            )
        elif selected_index == 1:  # Explain Code
            page_content.content = ft.Column(
                [
                    ft.Text("Code Explanation", size=24, weight="bold"),
                    code_input,
                    ft.ElevatedButton("Explain Code", on_click=explain_code),
                    output_explanation,
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            )
        elif selected_index == 2:
            page_content.content = ft.Column(
                [
                    ft.Text("Language Checker", size=24, weight="bold"),
                    code_input,
                    ft.ElevatedButton("Check Language", on_click=check_language),
                    output_translation,
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            )
        elif selected_index == 3:  # Code Quality Analysis
            page_content.content = ft.Column(
                [
                    ft.Text("Code Quality Analysis", size=24, weight="bold"),
                    code_input,
                    ft.ElevatedButton("Analyze Code Quality", on_click=analyze_code_quality),
                    output_quality_analysis,
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            )
        elif selected_index == 4:  # Settings
            page_content.content = ft.Column(
                [
                    ft.Text("Settings", size=24, weight="bold"),
                    settings_indentation,
                    settings_naming_convention,
                    ft.ElevatedButton("Save Settings", on_click=save_settings),
                ],
                spacing=20,
                scroll=ft.ScrollMode.AUTO,
                expand=True,
            )
        page.update()

    # Initialize the page content
    update_page_content(0)  # Default to the first page

    # Add navigation bar and page content to the page
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=page_content,
                    expand=True,  # Allow the container to expand and take available space
                ),
                nav_bar,
            ],
            expand=True,
        )
    )

ft.app(target=main)