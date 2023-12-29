from typing import Optional

from flask import Flask, abort, jsonify, request

from pkidb.data import Data
from pkidb.db import FileDatabase

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


if __name__ == "__main__":
    app.run()
