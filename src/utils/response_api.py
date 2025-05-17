from flask import jsonify


class ApiResponse:
    @staticmethod
    def response(success, message, data=None, status=200):
        return {
            "success": success,
            "message": message,
            "data": data,
        }, status
