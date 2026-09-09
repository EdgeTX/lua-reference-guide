#!/usr/bin/env python3

import json
from datetime import datetime, UTC
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


DECISIONS_PATH = Path("docs-system/generated/review-decisions.json")
TYPE_OPTIONS_PATH = Path("docs-system/review-type-options.json")
TYPE_DEFINITIONS_PATH = Path("docs-system/type-definitions.json")


def read_decisions() -> dict:
    if not DECISIONS_PATH.exists():
        return {}
    return json.loads(DECISIONS_PATH.read_text(encoding="utf-8"))


def write_decisions(data: dict) -> None:
    DECISIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    DECISIONS_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def read_type_options() -> dict:
    if not TYPE_OPTIONS_PATH.exists():
        return {"common_types": [], "custom_types": []}
    return json.loads(TYPE_OPTIONS_PATH.read_text(encoding="utf-8"))


def write_type_options(data: dict) -> None:
    TYPE_OPTIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    TYPE_OPTIONS_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def read_type_definitions() -> dict:
    if not TYPE_DEFINITIONS_PATH.exists():
        return {}
    return json.loads(TYPE_DEFINITIONS_PATH.read_text(encoding="utf-8"))


def write_type_definitions(data: dict) -> None:
    TYPE_DEFINITIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
    TYPE_DEFINITIONS_PATH.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def maybe_record_custom_types(payload: dict) -> None:
    type_options = read_type_options()
    type_definitions = read_type_definitions()
    common = set(type_options.get("common_types", []))
    custom = list(type_options.get("custom_types", []))
    seen = set(custom)
    for bucket in ("params", "returns"):
        for type_name in payload.get(bucket, {}).values():
            if not type_name or type_name == "TODO" or type_name in common or type_name in seen:
                continue
            custom.append(type_name)
            seen.add(type_name)
            type_definitions.setdefault(
                type_name,
                {
                    "luals_alias_of": "any",
                    "description": f"Custom semantic Lua API type: {type_name}",
                },
            )
    type_options["custom_types"] = custom
    write_type_options(type_options)
    write_type_definitions(type_definitions)


class Handler(BaseHTTPRequestHandler):
    def _send_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:
        self._send_json(200, {"ok": True})

    def do_GET(self) -> None:
        if self.path == "/healthz":
            self._send_json(200, {"ok": True})
            return
        if self.path == "/decisions":
            self._send_json(200, read_decisions())
            return
        if self.path == "/types":
            self._send_json(200, read_type_options())
            return
        self._send_json(404, {"error": "not found"})

    def do_POST(self) -> None:
        if self.path != "/decisions/save":
            self._send_json(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(length) or b"{}")
        item_id = payload.get("item_id")
        if not item_id:
            self._send_json(400, {"error": "missing item_id"})
            return
        decisions = read_decisions()
        decisions[item_id] = {
            "params": payload.get("params", {}),
            "returns": payload.get("returns", {}),
            "updated_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        }
        write_decisions(decisions)
        maybe_record_custom_types(decisions[item_id])
        self._send_json(200, {"ok": True, "item_id": item_id})


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8123), Handler)
    print("Review decision server listening on http://127.0.0.1:8123")
    server.serve_forever()
