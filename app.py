from api import db, app
from api import models
from ariadne import ObjectType, load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, \
    graphql_sync
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries import get_employees_resolver, get_employee_by_id_resolver
from api.mutations import create_employee_resolver


query = ObjectType("Query")
query.set_field("getEmployees", get_employees_resolver)
query.set_field("getEmployeeByID", get_employee_by_id_resolver)


mutation = ObjectType("Mutation")
mutation.set_field("createEmployee", create_employee_resolver)

# Load GraphQL schema
type_defs = load_schema_from_path("schema.graphql")

# Make executable schema by binding python snake case to schema and query. ex. "True id" -> "true_id"
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=['GET'])     # Loads up GraphQL UI for us
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=['POST'])    # Handling POST Request
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
