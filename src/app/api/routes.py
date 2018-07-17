import logging
from . import api
from flask_restplus import Resource, fields
from flask_restplus import reqparse
from math import sqrt


###  Hypotenuse Calculator API ###

hypotenuse_parser = reqparse.RequestParser()
hypotenuse_parser.add_argument('a', type=int, required=True, help="Side A is mandatory!")
hypotenuse_parser.add_argument('b', type=int, required=True, help="Side B is mandatory!")

@api.route('/hypotenuse')
@api.expect(hypotenuse_parser)
class Hypotenuse(Resource):

    def get(self):
        args = hypotenuse_parser.parse_args()

        # Hypotenuse Equation (or is it...)
        result = sqrt( args['a'] * args['a'] + args['b'] * args['a'])
        
        return { 'result': result }, 200
