import sys
from typing import Optional

from flask import Flask, abort, jsonify, request

from pkidb.data import Data
from pkidb.db import FileDatabase

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8080

app = Flask(__name__)
db = FileDatabase()


@app.route("/get/", methods=["GET", "POST"])
def get() -> str:
    """Endpoint to get value from database."""
    try:
        data = Data(**request.json)
    except TypeError:
        return abort(400)
    return jsonify(db.get(data.keypath))


@app.route("/set/", methods=["GET", "POST"])
def set() -> str:
    """Endpoint to set value in database."""
    try:
        data = Data(**request.json)
        if not data.value:
            return abort(400)
    except TypeError:
        return abort(400)
    if not data.verify():
        return abort(403)
    db.set(data.keypath, data.value)
    db.set(data.signature_path, data.signature_encoded)
    return jsonify(data.value)


@app.route("/list/")
@app.route("/list/<path:parent>")
def list(parent: Optional[str] = None) -> str:
    """Endpoint to list keys in database."""
    parent = parent or request.args.get("parent")
    if isinstance(parent, str):
        keylist = parent.split("/")
    else:
        keylist = []
    return jsonify(db.list(keylist))


def main() -> None:
    """Parse arguments and start Flask server."""
    fn, *args = sys.argv
    host, port = DEFAULT_HOST, DEFAULT_PORT

    if len(args) == 1:
        port = args[0]
    elif len(args) >= 2:
        host, port = args[0], args[1]

    app.run(host, port)


if __name__ == "__main__":
    main()
