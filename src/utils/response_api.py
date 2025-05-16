from flask import jsonify


class ApiResponse:
    @staticmethod
    def response(success: bool, message: str, data=None, status_code: int = None):
        response = {
            "success": success,
            "message": message,
            "data": data,
        }
        return jsonify(response), status_code
