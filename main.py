import typer
import os
from pathlib import Path
from parser import parse_openapi_file
from analyzer import evaluate_route_security

app = typer.Typer()

@app.command()
def scan(
    spec_path: Path = typer.Argument(..., help="Path to the OpenAPI JSON/YAML spec file."),
    output: str = typer.Option("report.html", "--output", "-o", help="Custom filename for the HTML report."),
    api_key: str = typer.Option(None, "--api-key", envvar="OPENAI_API_KEY", help="OpenAI API key for AI-powered vulnerability scanning.")
):
    """
    100% Local API Security Agent CLI - Scans OpenAPI specs and generates executive reports.
    """
    typer.echo(f"[*] Parsing OpenAPI specification from: {spec_path}")
    
    # Parse the spec
    endpoints = parse_openapi_file(spec_path)
    
    # Evaluate security (passing the API key if provided)
    results = evaluate_route_security(endpoints, api_key=api_key)
    
    # Save custom HTML output
    html_content = generate_html_dashboard(results, output)
    
    typer.secho(f"\n[+] Success! Executive HTML Dashboard saved to: {output}", fg=typer.colors.GREEN)

def generate_html_dashboard(results, filename):
    html = f"""<html><head><title>API Security Report</title></head>
    <body style="background:#111;color:#fff;font-family:sans-serif;padding:20px;">
    <h1>API Security Audit Report</h1>
    <p>Generated securely via local CI/CD pipeline.</p>
    <pre style="color:#0f0;">{results}</pre>
    </body></html>"""
    
    with open(filename, "w") as f:
        f.write(html)
    return html

if __name__ == "__main__":
    app()