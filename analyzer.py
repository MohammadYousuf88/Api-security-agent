import os
from openai import OpenAI

def evaluate_route_security(endpoints, api_key=None):
    report_results = []
    
    # Initialize OpenAI client if BYOK api_key is provided and valid
    client = None
    if api_key and api_key != "your-openai-key-here":
        try:
            client = OpenAI(api_key=api_key)
        except Exception:
            client = None

    for ep in endpoints:
        status = "SECURE"
        notes = []

        # Rule 1: Check basic authentication rule
        if not ep.has_auth:
            status = "VULNERABLE"
            notes.append("Missing authentication guard (No Auth detected).")
        else:
            notes.append("Authentication guard present.")

        # Rule 2: Live AI Deep Scan via BYOK OpenAI (if a real key is active)
        if client and ep.method in ["POST", "PUT"]:
            try:
                prompt = f"Analyze this API route for security risks. Method: {ep.method}, Path: {ep.path}, Parameters: {ep.parameters}. Give a short 1-sentence risk assessment."
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=60
                )
                ai_insight = response.choices[0].message.content.strip()
                notes.append(f"AI Insight: {ai_insight}")
            except Exception as e:
                notes.append(f"AI Scan skipped (Invalid or unauthorized API key).")
        else:
            if not client:
                notes.append("AI Scan skipped (No OpenAI API key provided - 100% local mode).")

        report_results.append({
            "path": ep.path,
            "method": ep.method,
            "status": status,
            "notes": notes
        })

    return report_results