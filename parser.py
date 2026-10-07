import json
import yaml
from pathlib import Path
from typing import List, Dict, Any, Union
from pydantic import BaseModel

class RouteEndpoint(BaseModel):
    path: str
    method: str
    has_auth: bool
    parameters: List[Dict[str, Any]]

def parse_openapi_file(file_path: Union[Path, str]) -> List[RouteEndpoint]:
    """Reads JSON or YAML OpenAPI files and extracts endpoint metadata."""
    path_str = str(file_path)
    
    with open(path_str, 'r') as f:
        if path_str.endswith('.json'):
            spec = json.load(f)
        else:
            spec = yaml.safe_load(f)

    global_security = bool(spec.get('security', []))
    parsed_routes = []

    for path, methods in spec.get('paths', {}).items():
        for method, details in methods.items():
            if method.lower() not in ['get', 'post', 'put', 'delete', 'patch']:
                continue
            
            # Check route-level security or fall back to global security
            route_security = details.get('security', None)
            has_auth = bool(route_security) if route_security is not None else global_security
            
            parameters = details.get('parameters', [])
            
            parsed_routes.append(
                RouteEndpoint(
                    path=path,
                    method=method.upper(),
                    has_auth=has_auth,
                    parameters=parameters
                )
            )

    return parsed_routes