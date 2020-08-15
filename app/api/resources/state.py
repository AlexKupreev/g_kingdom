from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from app.api.schemas import StateSchema
from app.models import State, Settings, State
from app.extensions import db
from app.commons.pagination import paginate


class StateResource(Resource):
    """Single object resource
    ---
    get:
      tags:
        - api
      parameters:
        - in: path
          name: state_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  state: StateSchema
        404:
          description: state does not exist
    put:
      tags:
        - api
      parameters:
        - in: path
          name: state_id
          schema:
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              StateSchema
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: state updated
                  state: StateSchema
        404:
          description: state does not exists
    delete:
      tags:
        - api
      parameters:
        - in: path
          name: state_id
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: state deleted
        404:
          description: state does not exist
    """

    # method_decorators = [jwt_required]

    def get(self, state_id):
        schema = StateSchema()
        state = State.query.get_or_404(state_id)
        return {"state": schema.dump(state)}

    def put(self, state_id):
        schema = StateSchema(partial=True)
        state = State.query.get_or_404(state_id)
        state = schema.load(request.json, instance=state)

        db.session.commit()

        return {"msg": "state updated", "state": schema.dump(state)}

    def delete(self, state_id):
        state = State.query.get_or_404(state_id)
        db.session.delete(state)
        db.session.commit()

        return {"msg": "state deleted"}


class StateList(Resource):
    """Creation and get_all
    ---
    get:
      tags:
        - api
      responses:
        200:
          content:
            application/json:
              schema:
                allOf:
                  - $ref: '#/components/schemas/PaginatedResult'
                  - type: object
                    properties:
                      results:
                        type: array
                        items:
                          $ref: '#/components/schemas/StateSchema'
    post:
      tags:
        - api
      requestBody:
        content:
          application/json:
            schema:
              StateSchema
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: state created
                  state: StateSchema
    """

    # method_decorators = [jwt_required]

    def get(self):
        schema = StateSchema(many=True)
        query = State.query
        return paginate(query, schema)

    def post(self):
        """User move
        * if no existing state
        """
        state = State()


        db.session.add(state)
        db.session.commit()

        return {"msg": "state created", "state": schema.dump(state)}, 201
